# client1/main.py
import streamlit as st
import requests
import numpy as np
from concrete import fhe
import os

FHE_SERVER_URL = os.environ.get("FHE_SERVER_URL", "http://localhost:8000")
CLIENT_ID = "client1"

st.set_page_config(page_title="Client 1 - KYC Registry", layout="centered")
st.title("🔐 Client 1 - UID Registry Provider")

# 載入 client1.txt 作為 UID 清單
uid_file_path = "client1.txt"
if not os.path.exists(uid_file_path):
    st.error("❌ UID 檔案不存在，請放置 'client1.txt'")
    st.stop()

uids = [int(line.strip()) for line in open(uid_file_path)]
st.success(f"已載入 {len(uids)} 組 UID")

if st.button("📤 回傳加密 UID 給 FHE Server"):
    res = requests.post(f"{FHE_SERVER_URL}/api/upload_encrypted_uids", json={
        "client_id": CLIENT_ID,
        "uids": uids
    })
    if res.ok:
        st.success("✅ 成功上傳加密 UID 給 FHE Server")
    else:
        st.error(f"❌ 上傳失敗：{res.text}")
