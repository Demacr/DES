from pyDes import *

#data = "Please encrypt my data"
#k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
# For Python3, you'll need to use bytes, i.e.:
data = b"Please encrypt my datb"
k = des(b"DESCRYPT", CFB, b"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
d = k.encrypt(data)
print ("Encrypted: %r" % d)
print ("Decrypted: %r" % k.decrypt(d))
assert k.decrypt(d, padmode=PAD_PKCS5) == data

h = des_hash(b"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
print (h.calc_hash(data))
