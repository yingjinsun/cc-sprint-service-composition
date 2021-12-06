import grequests
from django.http import HttpResponse
import json
from ResponseUtil import Response

urls = [
    'http://3.95.6.253:8000/infos/users',
    'http://3.95.6.253:8000/infos/addresses',
    'http://34.205.127.101:8000/infos/orders',
    'http://ccsprintproduct.us-east-1.elasticbeanstalk.com/infos/products'
]


def t1():
    rs = (grequests.get(u) for u in urls)
    x = grequests.map(rs)

    res = []
    for r in x:
        tmp = r.content.decode('utf8')
        tmp = json.loads(tmp)
        res.append(tmp["data"])
    return res

def index(request):
    if request.method == 'GET':
        total = t1()
        resp = Response().success(total)
        return HttpResponse(json.dumps(resp), content_type="application/json")
    # elif request.method == "GET":
    #     return HttpResponse(json.dumps(resp), content_type="application/json")




