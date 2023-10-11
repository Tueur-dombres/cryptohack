from pwn import * # pip install pwntools
import json
from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import codecs


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

r = remote('socket.cryptohack.org', 13377)
for i in range(100):
    received = json_recv()

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])

    if received["type"] == "rot13":
        ret = codecs.encode(received["encoded"], 'rot_13')
    elif received["type"] == "utf-8":
        ret = "".join(chr(int(e)) for e in received["encoded"])
    elif received["type"] == "bigint":
        ret = str(long_to_bytes(int(received["encoded"],16)))[2:-1]
    elif received["type"] == "hex":
        ret = "".join(chr(int(received["encoded"][i:i+2],16)) for i in range(0,len(received["encoded"]),2))
    elif received["type"] == "base64":
        ret = str(base64.b64decode(received["encoded"]))[2:-1]
    print("Return decoded value:")
    print(ret)

    to_send = {
        "decoded": ret
    }
    json_send(to_send)

received = json_recv()
print(received["flag"])