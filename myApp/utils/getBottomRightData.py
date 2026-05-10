from .getPublicData import *
import json
import time
import re

def getRankData():
    cars = list(getAllCars())
    carData = []
    for i in cars:
        price = re.findall(r'\d+\.?\d*', i.price)
        price = '-'.join(price)
        carData.append({
            "price": price,
            "carImg":i.carImg,
            "insure":i.insure,
            "marketTime":i.marketTime,
            "brand":i.brand,
            "rank":i.rank,
            "manufacturer":i.manufacturer,
            "saleVolume":i.saleVolume,
            "carModel":i.carModel,
            "carName":i.carName
        })
    return carData