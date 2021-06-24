import os
import web
import json
import uuid
from paddleocr import PaddleOCR

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
japanOcr = PaddleOCR(use_angle_cls=True, use_gpu=False, lang="japan")
urls = (
    '/ocr/api', 'OcrServer'
)
app = web.application(urls, globals())


class MyApplication(web.application):

    def run(self, port=8080, *middleware):

        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))


class OcrServer() :

    # 失败的返回
    def jsonFail(self, message):
        post_data = {
            "Code": -1,
            "Message": str(message),
            "RequestId": str(uuid.uuid4())
        }
        return json.dumps(post_data)


    # 成功的返回
    def jsonSuccess(self, data):
        post_data = {
            "Code": 0,
            "Message": "Success",
            "RequestId": str(uuid.uuid4()),
            "Data": data
        }
        return json.dumps(post_data)

    # ocr解析
    def ocrProccess(self, imgPath, language):

        if language == "japan":
            result = japanOcr.ocr(imgPath, cls=True)
        else:
            return

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

        return resMapList


    def POST(self) :

        postData = json.loads(web.data())
        ImagePath = postData["ImagePath"]
        Language = postData["Language"]

        try:
            res = self.ocrProccess(ImagePath, Language)
            return self.jsonSuccess(res)

        except Exception as err:
            return self.jsonFail(err)


if __name__ == "__main__":

    app = MyApplication(urls, globals())
    app.run(port=6666)