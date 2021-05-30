import base64
pas="1234567899"
passw=pas.encode("ascii")
encri=base64.b64encode(passw)
hash=encri.decode("ascii")
print(hash)