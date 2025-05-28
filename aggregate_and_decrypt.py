from concrete.ml import fhe

# 載入 OR 閘 circuit
@fhe.compiler({"a": "encrypted", "b": "encrypted"})
def or_gate(a, b):
    return a | b

or_circuit = or_gate.compile()

# 讀取三家結果
with open("result_a.bin", "rb") as f:
    r_a = or_circuit.client.deserialize_input(f.read())
with open("result_b.bin", "rb") as f:
    r_b = or_circuit.client.deserialize_input(f.read())
with open("result_c.bin", "rb") as f:
    r_c = or_circuit.client.deserialize_input(f.read())

# 聚合 OR
res_ab = or_circuit.run(r_a, r_b)
res_all = or_circuit.run(res_ab, r_c)

# 解密結果
client = or_circuit.client
final = client.decrypt(res_all)

print("🔍 是否曾在任一機構註冊過？", "✅ 是" if final else "❌ 否")