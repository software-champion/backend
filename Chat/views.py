import erniebot
import numpy as np
from PIL import Image
from django.http import JsonResponse
from paddleocr import PaddleOCR


def getPolish(request):
    content = "帮我润色下面这段话:" + request.POST.get("content")
    erniebot.access_token = request.POST.get("key")
    try:
        response = erniebot.ChatCompletion.create(
            model='ernie-bot',
            messages=[{'role': 'user', 'content': content}],
        )
        result = response['result']
        return JsonResponse({'result': result}, status=200)
    except Exception as e:
        return JsonResponse("error", status=500)


def getContinuation(request):
    content = "帮我续写下面这段话:" + request.POST.get("content")
    erniebot.access_token = request.POST.get("key")
    try:
        response = erniebot.ChatCompletion.create(
            model='ernie-bot',
            messages=[{'role': 'user', 'content': content}],
        )
        result = response['result']
        return JsonResponse({'result': result}, status=200)
    except Exception as e:
        return JsonResponse("error", status=500)

def getOCR(request):
    image = request.FILES.get('image')
    pil_image = Image.open(image)
    np_image = np.array(pil_image)
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")
    result = ocr.ocr(np_image, cls=True)[0]
    text = []
    for line in result:
        text.append(line[1][0])
    return JsonResponse({'text': text}, status=200)
