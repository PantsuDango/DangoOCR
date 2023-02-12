# -*- mode: python ; coding: utf-8 -*-
import os
import sys
import glob
import paddle

block_cipher = None

sys.path.insert(0, 'paddleocr')
sys.path.insert(0, 'paddleocr/ppocr/utils/e2e_utils')
sys.path.insert(0, 'paddleocr/ppocr/postprocess')


paddle_module_dir = os.path.abspath(os.path.dirname(paddle.__file__))


a = Analysis(
    ['package.py'],
    pathex=[],
    binaries=[(dll, '.') for dll in glob.glob(os.path.join(paddle_module_dir, 'libs', '*.dll'))],
    datas=[],
    hiddenimports=[
        'opencv-python',
        'skimage.filters.edges',
        'tools', # paddleocr.tools
        'ppocr', # paddleocr.ppocr
        'ppstructure', # paddleocr.ppstructure
        'extract_textpoint_slow', # paddleocr.ppocr.utils.e2e_utils.extract_textpoint_slow
        'extract_textpoint_fast', # paddleocr.ppocr.utils.e2e_utils.extract_textpoint_fast
        'picodet_postprocess', # paddleocr.ppocr.postprocess.picodet_postprocess
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# not safe for closed source app
# paddle_tree = Tree(paddle_module_dir, prefix='paddle', excludes=['__pycache__'])
paddle_proto_tree = Tree(os.path.join(paddle_module_dir, 'fluid', 'proto'), prefix='paddle/fluid/proto', excludes=['__pycache__'])
a.datas += paddle_proto_tree

# pretrained models
models_tree = Tree('whl', prefix='whl')
a.datas += models_tree

# ppocr dict
a.datas += Tree('paddleocr', prefix='paddleocr', excludes=['*.py','*.pyc','__pycache__'])


pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
