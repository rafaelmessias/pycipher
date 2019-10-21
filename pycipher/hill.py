import numpy as np
import re
import sys
from pycipher.base import Cipher

def to_num(text):
    return [(ord(c)-ord('a'))%26 for c in re.sub(' ', '', text.lower())]

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def mod_mat_inv(X, m=26):
    inv_X = np.linalg.inv(X)
    det = round(np.linalg.det(X))
    inv_det = modinv(det, m)
    inv_X = np.mod(np.round(det * inv_X) * inv_det, m)
    return inv_X.astype(np.int)

class Hill(Cipher):
    def __init__(self, key):
        n = int(np.sqrt(len(key)))
        if n ** 2 != len(key):
            raise Exception("The key cannot be turned into a square matrix.")
        key_num = to_num(key)
        key = np.array(key_num).reshape(n, n)
        if np.linalg.cond(key) > 1/sys.float_info.epsilon:       
            raise Exception("The key (matrix) is not invertible.")
        self.key = key
        self.inv_key = mod_mat_inv(self.key)
        if not np.all(np.mod(np.dot(self.key, self.inv_key), 26) == np.identity(n)):
            raise Exception("Error when computing inverse key.")

    def encipher(self, message, dec=False):
        key = self.inv_key if dec else self.key
        msg_num = to_num(message)
        msg_vector = np.array(msg_num).reshape(-1, key.shape[0]).T
        cip_vector = np.mod(np.dot(key, msg_vector), 26).T.reshape(1, -1)
        ciphertext = ''.join(chr(x % 26 + ord('a')) for x in list(cip_vector[0]))
        return ciphertext
        
    def decipher(self, ciphertext):
        return self.encipher(ciphertext, dec=True)
