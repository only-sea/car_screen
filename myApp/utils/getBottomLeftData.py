from .getPublicData import *
import json
import time

def getSquareData():
    cars = list(getAllCars())
    carVolumes = {}
    for i in cars:
        if i.brand not in carVolumes:
            carVolumes[i.brand] = int(i.saleVolume)
        else:
            carVolumes[i.brand] += int(i.saleVolume)
    carVolumes = sorted(carVolumes.items(), key=lambda x: x[1], reverse=True)
    brandlist = []
    volumelist = []
    pricelist = []
    for name, volume in carVolumes:
        brandlist.append(name)
        volumelist.append(volume)
    for brand in brandlist:
        min_price = float('inf')
        for j in cars:
            if j.brand == brand:
                price = json.loads(j.price)[0]
                if price < min_price:
                    min_price = price
        pricelist.append(min_price)
    return brandlist[:15], volumelist[:15], pricelist[:15]
