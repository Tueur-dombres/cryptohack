import pwn
import base64
from Crypto.Util.number import *

"""
print("".join(chr(e) for e in [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]))

print(bytes.fromhex("63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"))

print(base64.b64encode(bytes.fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")))

print(long_to_bytes(11515195063862318899931685488813747395775516287289682636499965282714637259206269))

print(pwn.xor("label",13))

KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
KEY2_KEY3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
FLAG_KEY1_KEY3_KEY2 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
a=pwn.xor(KEY2_KEY3,KEY1,FLAG_KEY1_KEY3_KEY2).hex()
print("".join(chr(int(a[i:i+2],16)) for i in range(0,len(a),2)))

for e in range(1,255):
    a=pwn.xor(bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"),e.to_bytes()).hex()
    print("".join(chr(int(a[i:i+2],16)) for i in range(0,len(a),2)))

b=pwn.xor(bytes.fromhex("0e0b213f26041e04"),bytes.fromhex("".join([hex(ord(e))[2:] for e in "crypto{}"])))
print(b)
print(bytes.fromhex("".join([hex(ord(e))[2:] for e in "crypto{}"])))
a=pwn.xor(bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"),b).hex()
print("".join(chr(int(a[i:i+2],16)) for i in range(0,len(a),2)))
"""

