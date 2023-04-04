import argparse

import flask
import paddleocr.paddleocr
from paddleocr.paddleocr import PaddleOCR
from flask import Flask, request, jsonify
from traceback import print_exc
import json
import uuid

# 2.3版本可用
paddleocr.paddleocr.BASE_DIR = "./"

japOcr = PaddleOCR(use_angle_cls=False, use_gpu=False, lang="japan", enable_mkldnn=True)
engOcr = PaddleOCR(use_angle_cls=False, use_gpu=False, lang="en", enable_mkldnn=True)
korOcr = PaddleOCR(use_angle_cls=False, use_gpu=False, lang="korean", enable_mkldnn=True)
ruOcr = PaddleOCR(use_angle_cls=False, use_gpu=False, lang="ru", enable_mkldnn=True)
zhOcr = PaddleOCR(use_angle_cls=False, use_gpu=False, lang="ch", enable_mkldnn=True)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

enable_image_path = True


# 失败的返回
def jsonFail(message):
    post_data = {
        "Code": -1,
        "Message": str(message),
        "RequestId": str(uuid.uuid4())
    }
    return jsonify(post_data)


# 成功的返回
def jsonSuccess(data):
    post_data = {
        "Code": 0,
        "Message": "Success",
        "RequestId": str(uuid.uuid4()),
        "Data": data
    }
    return jsonify(post_data)


def ocrResultSort(ocr_result):
    ocr_result.sort(key=lambda x: x[0][0][1])

    # 二次根据纵坐标数值分组（分行）
    all_group = []
    new_group = []
    flag = ocr_result[0][0][0][1]
    pram = max([int((i[0][3][1] - i[0][0][1]) / 2) for i in ocr_result])

    for sn, i in enumerate(ocr_result):
        if abs(flag - i[0][0][1]) <= pram:
            new_group.append(i)
        else:
            all_group.append(new_group)
            flag = i[0][0][1]
            new_group = [i]
    all_group.append(new_group)

    # 单行内部按左上点横坐标排序
    all_group = [sorted(i, key=lambda x: x[0][0][0]) for i in all_group]
    # 去除分组，归一为大列表
    all_group = [ii for i in all_group for ii in i]
    # 列表输出为排序后txt
    all_group = [ii for ii in all_group]

    return all_group


# ocr解析
def ocrProcess(img, language):
    if language == "JAP":
        result = japOcr.ocr(img, cls=False)
    elif language == "ENG":
        result = engOcr.ocr(img, cls=False)
    elif language == "KOR":
        result = korOcr.ocr(img, cls=False)
    elif language == "RU":
        result = ruOcr.ocr(img, cls=False)
    elif language == "ZH":
        result = zhOcr.ocr(img, cls=False)
    else:
        result = japOcr.ocr(img, cls=False)

    try:
        result = ocrResultSort(result)
    except Exception:
        pass

    resMapList = []
    for line in result:
        try:
            print(line[1][0])
        except Exception:
            pass
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
    print()

    return resMapList


# 接收请求
def handle_request():

    # 客户端检测是否运行
    if request.method == "HEAD":
        return flask.Response(headers={
            "Dango-OCR": "OK",
        })

    try:
        if request.mimetype == "multipart/form-data":
            post_data = request.form
            image = request.files["Image"].stream.read()
        else:
            if not enable_image_path:
                return jsonFail("Disable image path")
            post_data = request.get_data()
            post_data = json.loads(post_data.decode("utf-8"))
            image = post_data["ImagePath"]
        language = post_data["Language"]

        language_list = ["JAP", "ENG", "KOR", "RU", "ZH"]
        if language not in language_list:
            return jsonFail("Language {} doesn't exist".format(language))

        res = ocrProcess(image, language)
        return jsonSuccess(res)

    except Exception as err:
        print_exc()
        return jsonFail(err)


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 6666
    path = "/ocr/api"
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-h", "--host", type=str, default=host, help="监听的主机。默认：\"%s\"" % host)
    parser.add_argument("-p", "--port", type=int, default=port, help="监听的端口。默认：%d" % port)
    parser.add_argument("-P", "--path", type=str, default=path, help="监听的路径。默认：\"%s\"" % path)
    parser.add_argument("-d", "--disable-image-path", action="store_true", help="禁止图片路径。")
    parser.add_argument('--help', action='help', help='打印帮助。')
    args = parser.parse_args()

    host = args.host
    port = args.port
    path = args.path
    enable_image_path = not args.disable_image_path

    print('是否允许图片路径：%s' % enable_image_path)
    print("接口：http://%s:%d%s" % (host, port, path))
    app.add_url_rule(path, view_func=handle_request, methods=["POST", "HEAD"])
    app.run(debug=False, host=host, port=port, threaded=False)
