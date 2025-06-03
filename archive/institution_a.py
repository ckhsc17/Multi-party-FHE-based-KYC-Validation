from concrete.ml import fhe

with open("enc_uid.bin", "rb") as f:
    enc_bytes = f.read()

circuit = fhe.load("circuit_a.zip")
enc_uid = circuit.client.deserialize_input(enc_bytes)
enc_result = circuit.run(enc_uid)

with open("result_a.bin", "wb") as f:
    f.write(enc_result.serialize())

print("✅ 機構 A 已完成密文判斷並儲存結果")