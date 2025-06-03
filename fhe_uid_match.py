from concrete import fhe
import numpy as np

# 定義：比較兩個 UID 是否一致
@fhe.compiler({"x": "encrypted", "y": "encrypted"})
def is_equal(x, y):
    return x == y

# 提供範例輸入給 compiler（inputset）
example_input = (np.array([12345], dtype=np.uint16), np.array([54321], dtype=np.uint16))
compiled_circuit = is_equal.compile(inputset=[example_input])

# 模擬兩家機構的 UID hash
uid_hash_a = np.array([12345], dtype=np.uint16)
uid_hash_b = np.array([12345], dtype=np.uint16)

# 加密並執行比對
enc_a = compiled_circuit.encrypt(uid_hash_a)
enc_b = compiled_circuit.encrypt(uid_hash_b)
enc_result = compiled_circuit.run(enc_a, enc_b)
result = compiled_circuit.decrypt(enc_result)

print("✅ 是否為相同 UID：", bool(result[0]))
