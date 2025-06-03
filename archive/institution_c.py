from concrete.ml import fhe

with open("enc_uid.bin", "rb") as f:
    enc_bytes = f.read()

circuit = fhe.load("circuit_c.zip")
enc_uid = circuit.client.deserialize_input(enc_bytes)
enc_result = circuit.run(enc_uid)

with open("result_c.bin", "wb") as f:
    f.write(enc_result.serialize())

print("✅ 機構 C 已完成密文判斷並儲存結果")