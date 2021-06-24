from paddleocr import PaddleOCR
import time

japanOcr = PaddleOCR(use_angle_cls=True, use_gpu=False, lang="japan")

start = time.time()
result = japanOcr.ocr("image.jpg", cls=True)
resMapList = []
for line in result:
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
print(resMapList)
print("Time: ", time.time()-start)