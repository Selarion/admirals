import json

from django.http import HttpResponse
from .models import Category


def set_categories(request):
    js_req = json.loads(request.body.decode('utf-8'))
    if Category.check_unique_name(js_req):
        return HttpResponse(json.dumps({'success': False}))
    return HttpResponse(json.dumps(Category.recursively_insert(js_req)))


def get_categories(request, id):
    response = Category.get_info(id)
    return HttpResponse(json.dumps(response))
