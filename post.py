import requests
import time
import json


url = 'http://127.0.0.1:6666/ocr/api'
data = {
    'ImagePath': "image.jpg",
    'Language': "japan"
}

start = time.time()
res = requests.post(url, data=json.dumps(data))
res.encoding = "utf-8"
print(res.text)
print("Time: ", time.time()-start)