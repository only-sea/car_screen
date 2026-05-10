import json
import time
from .getPublicData import *

def getCarVolume_PrinceData():
    cars = list(getAllCars())
    pricelist = {"0-5w":0,"5-10w":0,"10-20w":0,"20-30w":0,"30w以上":0}
    for i in cars:
        price = json.loads(i.price)[0]
        if price < 5:
            pricelist["0-5w"] += 1
        elif 5 <= price < 10:
            pricelist["5-10w"] += 1
        elif 10 <= price < 20:
            pricelist["10-20w"] += 1
        elif 20 <= price < 30:
            pricelist["20-30w"] += 1
        else:
            pricelist["30w以上"] += 1
    price_list = []
    for k, v in pricelist.items():
        price_list.append({
            "name": k,
            "value": v
        })
    return price_list