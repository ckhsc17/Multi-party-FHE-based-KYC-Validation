# 安裝 concrete-ml 的指令（在這裡僅列出，不實際執行）
installation_instructions = """
!pip install concrete-ml
"""

# 建立金鑰與驗證 circuit 的 Python 程式碼
from concrete.ml import fhe

# 模擬三家機構的已知 UID（這是使用者雜湊後的值）
KNOWN_UID_A = 123456789
KNOWN_UID_B = 987654321
KNOWN_UID_C = 111111111

# 為每家機構建立對應的 FHE 判斷函數（只看是否相等）
@fhe.compiler({"x": "encrypted"})
def check_uid_a(x):
    return x == KNOWN_UID_A

@fhe.compiler({"x": "encrypted"})
def check_uid_b(x):
    return x == KNOWN_UID_B

@fhe.compiler({"x": "encrypted"})
def check_uid_c(x):
    return x == KNOWN_UID_C

# 編譯 circuits（實際會花些時間）
circuit_a = check_uid_a.compile()
circuit_b = check_uid_b.compile()
circuit_c = check_uid_c.compile()

# 儲存 public key 給使用者加密使用，保存私鑰供最終解密
client = circuit_a.client
client.save("client.zip")  # 包含 public key
circuit_a.save("circuit_a.zip")
circuit_b.save("circuit_b.zip")
circuit_c.save("circuit_c.zip")

"✅ 已完成金鑰與三家機構的 FHE circuit 編譯與保存。"
