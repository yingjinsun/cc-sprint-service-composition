import grequests
from datetime import datetime
import json



urls = [
    'http://3.95.6.253:8000/infos/users',
    'http://3.95.6.253:8000/infos/addresses',
    'http://34.205.127.101:8000/infos/orders',
    'http://ccsprintproduct.us-east-1.elasticbeanstalk.com/infos/products'
]


def t1():
    s = datetime.now()
    rs = (grequests.get(u) for u in urls)
    x = grequests.map(rs)
    e = datetime.now()

    res = []
    for r in x:
        tmp = r.content.decode('utf8')
        tmp = json.loads(tmp)
        res.append(tmp["data"])
t1()