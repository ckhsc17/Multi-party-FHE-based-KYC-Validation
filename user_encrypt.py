# user_encrypt.py
import hashlib
import numpy as np
from concrete.ml.sklearn import LogisticRegression

# 模擬使用者輸入
uid_raw = "Alice_19900101_0912345678"
uid_hash = int(hashlib.sha256(uid_raw.encode()).hexdigest(), 16) % (2**16)
X = np.array([[uid_hash]])

# 載入已編譯模型
model = LogisticRegression.load("fhe_model")

# FHE 預測（會自動加密推論再解密）
y_pred = model.predict(X, execute_in_fhe=True)

print(f"✅ UID 加密預測完成，使用者風險等級為: {y_pred[0]}（由 hash={uid_hash} 對應）")
