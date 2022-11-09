import requests
import time
import json
import os
import cv2
from traceback import print_exc

URL = "http://127.0.0.1:6666/ocr/api"
IMAGE_NAME = "JAP.jpg"
LANGUAGE = "JAP"


def post() :
    data = {
        "ImagePath": os.path.join(os.getcwd(), IMAGE_NAME),
        "Language": LANGUAGE
    }
    proxies = {"http": None, "https": None}
    try :
        res = requests.post(URL, data=json.dumps(data), proxies=proxies)
        res.encoding = "utf-8"
        result = json.loads(res.text)
        content = ""
        for val in result["Data"]:
            content += val["Words"] + " "
        print(content)
    except Exception :
        print(result["Message"])


def main() :

    number = 10
    timeCount = 0
    for num in range(number) :
        start = time.time()
        post()
        end = time.time()
        timeCount += end - start
        print("time: {}\n".format(end - start))
    print("avg time: {}".format(timeCount / number))


if __name__ == "__main__" :

	main()
	