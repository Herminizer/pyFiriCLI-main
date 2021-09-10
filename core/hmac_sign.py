import time
import json
import hmac
import hashlib 


secret = b'd81fc006d75a5b755bb2e3a9c231869003b10fa75670b3a695c80e7b8b999378'
epoch = {
    'timestamp': int(time.time()),
    'validity': 2000
    }

json_obj = json.dumps(epoch).encode('utf-8')

signature = hmac.new(secret, json_obj, hashlib.sha256).hexdigest()

#print(signature)