from PIL import Image
import requests
import time
import json
import os


def processImage(filename, mwidth=400, mheight=400):

    image = Image.open(filename)
    w, h = image.size

    if w <= mwidth and h <= mheight:
        return

    if (1.0 * w / mwidth) > (1.0 * h / mheight):
        scale = 1.0 * w / mwidth
        new_im = image.resize((int(w / scale), int(h / scale)), Image.ANTIALIAS)
    else:
        scale = 1.0 * h / mheight
        new_im = image.resize((int(w / scale), int(h / scale)), Image.ANTIALIAS)

    imagePath = os.path.join(os.getcwd(), "new-"+filename)
    new_im.save(imagePath)
    new_im.close()

    return imagePath


def post(changeSize=False) :

    url = 'http://127.0.0.1:6666/ocr/api'
    filename = "image.jpg"
    if changeSize == True :
        imagePath = processImage(filename, 400, 400)
    else :
        imagePath = os.path.join(os.getcwd(), filename)

    data = {
        'ImagePath': imagePath,
        'Language': "JAP"
    }

    res = requests.post(url, data=json.dumps(data))
    res.encoding = "utf-8"
    print(json.loads(res.text))


def main() :

    number = 10
    timeCount = 0
    for num in range(number) :
        start = time.time()
        post(changeSize=False)
        end = time.time()
        timeCount += end - start
        print("time: {}\n".format(end - start))

    print("avg time: {}".format(timeCount / number))


if __name__ == "__main__" :

    main()