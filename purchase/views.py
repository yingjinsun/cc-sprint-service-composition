from django.http import HttpResponse
import json
from ResponseUtil import Response
import requests
from ConstantUtil import Constant

def index(request):
    userPath = 'http://3.95.6.253:8000/infos/users'
    productPath = 'http://ccsprintproduct.us-east-1.elasticbeanstalk.com/infos/products'
    orderPath = 'http://34.205.127.101:8000/infos/orders'

    if request.method == 'POST':
        requestDict = eval(request.body)
        if requestDict:
            # User info
            userID = str(requestDict.get('userID'))
            user = requests.get(userPath+'/'+userID)
            # Product info
            productID = str(requestDict.get('productID'))
            product = requests.get(productPath+'/'+productID)

            # Check user and product if request fail, return not found
            if user.status_code != 200 or product.status_code != 200:
                resp = Response().failed()
                return HttpResponse(json.dumps(resp), content_type="application/json", status=404)

            # Check stock if it is less than demand, return bad data
            stock = product.json()["data"]["amount"]
            quantity = requestDict.get('quantity')
            if stock < quantity:
                resp = Response().resp(Constant().BAD_DATA, "Out of stock")
                return HttpResponse(json.dumps(resp), content_type="application/json", status=400)

            # Place order
            order = requests.post(orderPath, data=json.dumps(requestDict))

            # Update stock
            productInfo = product.json()["data"]
            productInfo["amount"] = productInfo["amount"] - quantity
            del productInfo['product_id']
            requests.put(productPath+'/'+productID, data=json.dumps(productInfo))

            response = Response().resp(Constant().POST, order.json()['data'])
            return HttpResponse(json.dumps(response), content_type="application/json", status=201)
        resp = Response().failed()
        return HttpResponse(json.dumps(resp), content_type="application/json", status=404)