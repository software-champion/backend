from django.urls import path
from Chat.views import *

urlpatterns = [
    path('polish', getPolish),
    path('continuation', getContinuation),
    path('ocr', getOCR),
]