import csv
from io import TextIOWrapper
from django.http import HttpResponse, JsonResponse
from . import models
import json 


# Create your views here.
def getStocksDetails(request):
    req_body = request.body.decode('utf-8')
    req = json.loads(req_body)
    symbol = req["symbol"]
    stocksData = models.Symbol.objects.filter(symbol__id=symbol)
    stocksDataList = []
    for data in stocksData:
        stocksDataList.append({

        })
    return JsonResponse({'data':stocksDataList},status=201)
    