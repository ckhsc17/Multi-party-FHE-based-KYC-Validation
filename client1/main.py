# client1/main.py
import streamlit as st
import requests
import os
from utils import load_circuit, encrypt_uid

FHE_SERVER_URL = os.getenv("FHE_SERVER_URL", "http://localhost:8000")
CLIENT_ID = "client1"
UID_FILE = "client1.txt"

st.set_page_config(page_title="Client 1", layout="centered")
st.title("🔐 Client 1 - Secure UID Module")

# 載入 FHE 電路
circuit = load_circuit()

# --- 上傳欲查詢的 UID ---
st.header("📤 傳送查詢 UID（加密）")
uid_to_check = st.number_input("輸入欲查詢的 UID", min_value=0, step=1)

if st.button("🔐 加密並傳送"):
    try:
        encrypted_uid = encrypt_uid(uid_to_check, circuit)
        res = requests.post(f"{FHE_SERVER_URL}/query_uid", json={
            "client_id": CLIENT_ID,
            "enc_uid": encrypted_uid,
        })
        if res.ok:
            st.success(f"✅ 查詢請求已傳送")
        else:
            st.error(f"❌ 傳送失敗: {res.text}")
    except Exception as e:
        st.exception(e)

# --- 接收 FHE Server 請求白名單時使用 ---
st.header("📥 等待 FHE Server 索取白名單")

if st.button("📤 回傳本地 UID 清單"):
    try:
        with open(UID_FILE, "r") as f:
            uids = [int(line.strip()) for line in f if line.strip().isdigit()]
        res = requests.post(f"{FHE_SERVER_URL}/fetch_whitelist", json={
            "client_id": CLIENT_ID,
            "uids": uids
        })
        if res.ok:
            st.success("✅ 成功上傳白名單 UID 給 FHE Server")
        else:
            st.error(f"❌ 上傳失敗: {res.text}")
    except Exception as e:
        st.exception(e)


# --- 回傳加密白名單 ---
st.header("📥 等待 FHE Server 索取白名單")

if st.button("📤 加密後回傳 UID 清單"):
    try:
        with open(UID_FILE, "r") as f:
            raw_uids = [int(line.strip()) for line in f if line.strip().isdigit()]
        encrypted_list = [circuit.client.serialize_input(circuit.encrypt(np.uint16(uid))) for uid in raw_uids]

        res = requests.post(f"{FHE_SERVER_URL}/fetch_whitelist", json={
            "client_id": CLIENT_ID,
            "encrypted_uids": encrypted_list  # 所有加密後的密文
        })
        if res.ok:
            st.success("✅ 成功上傳【加密白名單】給 FHE Server")
        else:
            st.error(f"❌ 上傳失敗: {res.text}")
    except Exception as e:
        st.exception(e)
