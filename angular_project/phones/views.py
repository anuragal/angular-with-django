# Create your views here.
from django.http import HttpResponse

import json

def get_phone_json(request):
    json_file = open("media/phones.json")
    return HttpResponse(json_file, mimetype='application/json')

def render_json_response(result=None):
    response_dict = {}
    response_dict.update({'response':result})
    response = HttpResponse(json.dumps(response_dict), mimetype='application/json')
    return response