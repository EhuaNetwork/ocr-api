# ocr-api
基于paddleOCR+django的api实现

安装PaddlePaddle
```
python3 -m pip install paddlepaddle-gpu -i https://mirror.baidu.com/pypi/simple
python3 -m pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
```
安装PaddleOCR whl包
```
pip install "paddleocr>=2.0.1" # 推荐使用2.0.1+版本
```

启动环境
```
adduser user
passwd user
su user
export PATH=$PATH:/www/server/pyporject_evn/versions/3.7.9/bin
python3.7 manage.py  runserver 0.0.0.0:8000
```


相关文档：https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/doc/doc_ch/quickstart.md#22
