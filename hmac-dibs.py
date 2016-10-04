import hmac, hashlib

key = "6f2d303f5a325f4744427d35342c515a66384f7864702e5a316b43377b322d70485236717d264a25472c446844763a734d357b4761562945462a442e4d533837"
#data = "amount=100&currency=EUR"
data = "acceptReturnUrl=http://localhost:8000/receipt&amount=20250&cancelreturnurl=http://localhost:8000/cancel&currency=978&language=en&merchant=90181972&oiRow0=1;Hoodies;St.Grays;16200;8;2500&oiTypes=QUANTITY;UNITCODE;DESCRIPTION;AMOUNT;ITEMID;VATPERCENT&orderId=O-147556288173011&payType=VISA,MC&s_userID=null&test=1"

# hex to string
print key.decode('hex')

print hmac.new(key.decode('hex'), data, digestmod=hashlib.sha256).hexdigest()

