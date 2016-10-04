#!/usr/bin/env python
#
# ./HMAC-MD5.py "The quick brown fox jumps over the lazy dog"
# 80070713463e7749b90c2dc24911e275
import sys 
from hashlib import md5 
 
trans_5C = "".join(chr(x ^ 0x5c) for x in xrange(256))
trans_36 = "".join(chr(x ^ 0x36) for x in xrange(256))
blocksize = md5().block_size
 
def hmac_md5(key, msg):
    if len(key) > blocksize:
        key = md5(key).digest()
    key += chr(0) * (blocksize - len(key))
    o_key_pad = key.translate(trans_5C)
    i_key_pad = key.translate(trans_36)
    return md5(o_key_pad + md5(i_key_pad + msg).digest())

if (len(sys.argv) == 2):
    k = sys.argv[1]
    h = hmac_md5("superuser", k)
    print h.hexdigest()  
else:
  print "You have to provide a string argument 'the key..'"