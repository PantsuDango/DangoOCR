from paddleocr import PaddleOCR
from PIL import Image
import os
import time


japanOcr = PaddleOCR(use_angle_cls=True, use_gpu=False, lang="japan", enable_mkldnn=True)


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

    imagePath = os.path.join(os.getcwd(), "new-" + filename)
    new_im.save(imagePath)
    new_im.close()

    return imagePath


def ocrProccess(imgPath, language) :

    if language == "japan" :
        result = japanOcr.ocr(imgPath, cls=True)
    else :
        return

    resMapList = []
    for line in result :
        resMap = {
            "Coordinate": {
                "UpperLeft": line[0][0],
                "UpperRight": line[0][1],
                "LowerRight": line[0][2],
                "LowerLeft": line[0][3]
            },
            "Words": line[1][0],
            "Score": float(line[1][1])
        }
        resMapList.append(resMap)

    return resMapList


def main() :

    filename = "image.jpg"
    language = "japan"
    imagePath = os.path.join(os.getcwd(), filename)
    number = 10

    timeCount = 0
    for num in range(number) :
        start = time.time()
        # imagePath = processImage(filename, 400, 400)
        resMapList = ocrProccess(imagePath, language)
        print(resMapList)
        end = time.time()
        timeCount += end - start
        print("time: {}\n".format(end-start))

    print("avg time: {}".format(timeCount/number))


if __name__ == "__main__" :

    main()
