from concrete.ml.crypto import EncryptionClient
import hashlib

# 模擬使用者輸入個資後做 hash
uid_raw = "Alice_19900101_0912345678"
uid_hash = int(hashlib.sha256(uid_raw.encode()).hexdigest(), 16) % (2**16)

# 載入金鑰加密
client = EncryptionClient.load("client.zip")
enc_uid = client.encrypt(uid_hash)

# 儲存密文
with open("enc_uid.bin", "wb") as f:
    f.write(enc_uid.serialize())

print(f"✅ 使用者密文 UID 已儲存（hash={uid_hash}）")