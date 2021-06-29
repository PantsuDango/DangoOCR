from paddleocr import PaddleOCR
from flask import Flask, request, jsonify

from traceback import print_exc
import json
import uuid
import logging
import os


japanOcr = PaddleOCR(use_angle_cls=True, use_gpu=False, lang="japan", enable_mkldnn=True)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


def setLog() :

    filePath = os.path.join(os.getcwd(), "logs", "log.txt")
    try :
        os.mkdir("logs")
    except :
        pass
    else :
        open(filePath, "a", encoding="utf-8")

    logging.basicConfig(filename=filePath,
                        format='%(acstime)s%(levelname)s:%(meaasge)s',
                        level=logging.DEBUG)


# 失败的返回
def jsonFail(message) :

    post_data = {
        "Code": -1,
        "Message": str(message),
        "RequestId": str(uuid.uuid4())
    }
    return jsonify(post_data)


# 成功的返回
def jsonSuccess(data) :

    post_data = {
        "Code": 0,
        "Message": "Success",
        "RequestId": str(uuid.uuid4()),
        "Data": data
    }
    return jsonify(post_data)


# ocr解析
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


# 接收请求
@app.route("/ocr/api", methods=["POST"])
def getPost() :

    try:
        post_data = request.get_data()
        post_data = json.loads(post_data.decode("utf-8"))
        res = ocrProccess(post_data["ImagePath"], post_data["Language"])
        logging.info(res)
        return jsonSuccess(res)

    except Exception as err:
        print_exc()
        logging.error(err)
        return jsonFail(err)


if __name__ == "__main__" :

    setLog()
    app.run(debug=False, host="0.0.0.0", port=6666)