from django.http import HttpResponse
import json
from ResponseUtil import Response

def index(request):
        resp = Response().success("Set token Successfully!")
        return HttpResponse(json.dumps(resp), content_type="application/json")




