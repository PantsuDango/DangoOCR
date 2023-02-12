'''PyInstaller的打包入口'''

# hack openkmp duplicate_lib error
import os
import shutil
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'


# hack paddle dataset subprocess check cv2 error
import subprocess
popen_init = subprocess.Popen.__init__
def __init__(self, args, *argv, **kwargs):
    if isinstance(args, list) and len(args) > 2:
        if args[1] == "-c" and args[2] == "import cv2":
            self.communicate = lambda: (None, None)
            self.poll = lambda: 0
    else:
        popen_init(self, args, *argv, **kwargs)
subprocess.Popen.__init__ = __init__


# hack paddle ocr importlib import module error
import importlib
importlib_module = importlib.import_module
def import_module(name, package=None):
    if name == '.' and package == 'tools':
        from paddleocr import tools
        return tools
    if name == '.' and package == 'ppocr':
        from paddleocr import ppocr
        return ppocr
    if name == '.' and package == 'ppstructure':
        from paddleocr import ppstructure
        return ppstructure
    return importlib_module(name, package)
importlib.import_module = import_module


# hack to copy models first
import paddleocr
model_dir = os.path.abspath(os.path.join(os.path.dirname(paddleocr.__file__), '..', 'whl'))
if not os.path.exists('whl'):
    shutil.copytree(model_dir, './whl')


from app import app

if __name__ == "__main__" :
    app.run(debug=False, host="0.0.0.0", port=6666, threaded=False)
