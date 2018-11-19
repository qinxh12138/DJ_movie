import datetime
import decimal
from collections import Iterable

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from apps.movies.models import TFilm


def find(request):
    tf = TFilm.objects.all()
    print(tf)
    return HttpResponse('呵呵')


def movies(request):
    try:
        films = TFilm.objects.all()
        result = to_list(films)
        data = {
            'status': 200,
            'msg': 'success',
            'data': result
        }
    except:
        data = {'status': 404, 'msg': 'error'}
    response = JsonResponse(data)
    response["Access-Control-Allow-Headers"] = "content-type"
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    return response


# 将对象转化成字典对象
def obj_to_dict(obj):
    result = {}
    if obj:
        # 将对象所有属性值,转化成字典形式
        keys = vars(obj).keys()
        if keys:
            for key in keys:
                if not key.startswith('_'):
                    value = getattr(obj, key)

                    if isinstance(value, datetime.datetime):
                        value = value.strftime('%Y-%m-%d %H:%i:%s ')
                    elif isinstance(value, datetime.date):
                        value = value.strftime('%Y-%m-%d')
                    elif isinstance(value, decimal.Decimal):
                        value = float(value)
                    result[key] = value
    return result


# 将QuerySet对象转化列表套字典
def to_list(objects):
    li = []
    if objects and isinstance(objects, Iterable):
        for obj in objects:
            li.append(obj_to_dict(obj))
    return li
