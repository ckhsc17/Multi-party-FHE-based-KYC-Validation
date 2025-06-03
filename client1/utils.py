# client1/utils.py
import numpy as np
from concrete import fhe

def load_circuit():
    return fhe.load("circuit.zip")

def encrypt_uid(uid, circuit):
    enc = circuit.encrypt(np.uint16(uid))
    return circuit.client.serialize_input(enc)
