from paddleocr import PaddleOCR
from flask import Flask, request, jsonify

from traceback import print_exc
import json
import uuid


japOcr = PaddleOCR(use_angle_cls=True, use_gpu=False, lang="japan", enable_mkldnn=True)
engOcr = PaddleOCR(use_angle_cls=True, use_gpu=False, lang="en", enable_mkldnn=True)
korOcr = PaddleOCR(use_angle_cls=True, use_gpu=False, lang="korean", enable_mkldnn=True)


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

    if language == "jap" :
        result = japOcr.ocr(imgPath, cls=True)
    elif language == "eng" :
        result = engOcr.ocr(imgPath, cls=True)
    elif language == "kor":
        result = korOcr.ocr(imgPath, cls=True)
    else :
        result = japOcr.ocr(imgPath, cls=True)

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

        languageList = ["jap", "eng", "kor"]
        if post_data["Language"] not in languageList :
            return jsonFail("Language {} doesn't exist".format(post_data["Language"]))

        res = ocrProccess(post_data["ImagePath"], post_data["Language"])
        return jsonSuccess(res)

    except Exception as err:
        print_exc()
        return jsonFail(err)


if __name__ == "__main__" :

    app.run(debug=False, host="0.0.0.0", port=6666)