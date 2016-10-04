#!/usr/bin/python
#
# md 5 digest 

import md5 

m = md5.new()
m.update("Nobody inspects")
m.update(" the spammish repetition")
p = m.digest()
print p