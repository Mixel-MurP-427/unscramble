from base_after_base import hexadecimal, binary, base_to_base
from hashlib import md5

message = md5("Braden Jay Mullarky".encode()).hexdigest().upper()

print(message)

myBinary = base_to_base(message, hexadecimal, binary).zfill(128)

for i in range(0, len(myBinary), 8): # prints one byte at a time.
    print(myBinary[i:i+8])

assert len(myBinary) == 128 #an MD5 hash always returns 128 bits