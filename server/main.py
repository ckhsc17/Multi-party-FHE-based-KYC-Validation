from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
from concrete import fhe

# 初始化 FastAPI
app = FastAPI()

# 定義 allowlist 與 FHE 計算模型
ALLOWLIST = [1111, 2222, 3333, 4444, 5555]

def uid_in_allowlist(uid):
    return sum([uid == np.uint16(x) for x in ALLOWLIST]) > 0

compiler = fhe.Compiler(uid_in_allowlist, {"uid": "encrypted"})
inputset = [(np.uint16(x),) for x in ALLOWLIST]
circuit = compiler.compile(inputset)
circuit.keygen()

# 定義請求模型
class UIDRequest(BaseModel):
    uid: int

# API endpoint: 驗證 UID 是否在白名單中
@app.post("/check_uid")
def check_uid(request: UIDRequest):
    try:
        uid = np.uint16(request.uid)
        enc_uid = circuit.encrypt(uid)
        enc_result = circuit.run(enc_uid)
        result = circuit.decrypt(enc_result)
        return {"is_in_allowlist": bool(result)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
