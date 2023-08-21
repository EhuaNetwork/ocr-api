
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, HttpResponse
from django.http import request
from paddleocr import PaddleOCR, draw_ocr
import json

def ocr(request):

    # ocr = PaddleOCR(use_angle_cls=True, lang="ch", show_log=False)
    # img_path = './1.png'
    # result = ocr.ocr(img_path, cls=True)
    # json.dumps(result)
    # print(result)
    
   # 获取上传的文件
    file = request.FILES['image']
    
    # 读取内存中的上传文件内容
    file_content = file.read()
    
    # 进行 OCR 处理
    ocr = PaddleOCR(use_angle_cls=True, lang="ch", show_log=False)
    result = ocr.ocr(file_content, cls=True)

    # 将结果转换为 JSON 字符串并返回
    result_json = json.dumps(result)
    
    result=success(result_json)
    return HttpResponse(result, content_type='application/json')
    
def success(data, msg='success', code=200):
    res = {
        'message': msg,
        'code': code,
        'data': data,
    }
    response = JsonResponse(res, status=200)
    return response