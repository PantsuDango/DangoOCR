import requests
import time
import json
import os


def post() :

    start = time.time()

    url = 'http://127.0.0.1:6666/ocr/api'
    filename = "image.jpg"
    imagePath = os.getcwd() + "/" + filename
    data = {
        'ImagePath': imagePath,
        'Language': "japan"
    }

    res = requests.post(url, data=json.dumps(data))
    res.encoding = "utf-8"
    print(json.loads(res.text))
    print("Time: ", time.time()-start)


def main() :

    number = 1
    for num in range(number) :
        post()


if __name__ == "__main__" :

    main()