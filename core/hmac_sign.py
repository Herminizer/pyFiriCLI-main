import time
import json
import hmac
import hashlib 


secret = b'your secret key'
epoch = {
    'timestamp': int(time.time()),
    'validity': 2000
    }

json_obj = json.dumps(epoch).encode('utf-8')

signature = hmac.new(secret, json_obj, hashlib.sha256).hexdigest()

#print(signature)
