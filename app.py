from paddleocr import PaddleOCR
from flask import Flask, request, jsonify
import json
import uuid
import os
from traceback import print_exc

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
japanOcr = PaddleOCR(use_angle_cls=True, use_gpu=False, lang="japan")

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


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
        return jsonSuccess(res)

    except Exception as err:
        print_exc()
        return jsonFail(err)


if __name__ == "__main__" :

    app.run(debug=False, host="0.0.0.0", port=6666)