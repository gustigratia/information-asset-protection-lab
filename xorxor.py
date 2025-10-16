k1_hex     = "3c3f0193af37d2ebbc50cc6b91d27cf61197"
k21_hex    = "ff76edcad455b6881b92f726987cbf30c68c"
k23_hex    = "611568312c102d4d921f26199d39fe973118"
k1234_hex  = "91ec5a6fa8a12f908f161850c591459c3887"
f45_hex    = "0269dd12fe3435ea63f63aef17f8362cdba8"

hx = lambda s: bytes.fromhex(s)

k1 = hx(k1_hex)
k21 = hx(k21_hex)
k23 = hx(k23_hex)
k1234 = hx(k1234_hex)
f45 = hx(f45_hex)

bxor = lambda a,b: bytes(x ^ y for x,y in zip(a,b))

k2 = bxor(k21, k1)
k3 = bxor(k23, k2)
k4 = bxor(bxor(bxor(k1234, k1), k2), k3)
f5 = bxor(f45, k4)

prefix = b"cry{"
key5_bytes = bytes([f5[i] ^ prefix[i] for i in range(4)])

key_len = len(key5_bytes)
flag_buffer = bytearray(len(f5))
for i in range(len(f5)):
    key_byte = key5_bytes[i % key_len]   
    flag_buffer[i] = f5[i] ^ key_byte
flag = bytes(flag_buffer)

print(flag.decode())