from django.http import HttpResponse
import json
from ResponseUtil import Response

def index(request):
    if request.method == 'POST':
        resp = Response().success("Set token Successfully!")
        return HttpResponse(json.dumps(resp), content_type="application/json")
    elif request.method == "GET":
        return HttpResponse(json.dumps(resp), content_type="application/json")




