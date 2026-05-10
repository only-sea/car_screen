import json
import time
from .getPublicData import *

def getBaseData():
    cars = list(getAllCars())
    #车辆总数
    sumCar = len(cars)
    #车辆最高销售
    highVolume = cars[0].saleVolume
    #销售最多汽车
    topCar = cars[0].carName
    #销售最多类型
    carModels = {}
    for i in cars:
        if carModels.get(i.carModel,-1) == -1:
            carModels[str(i.carModel)] = int(i.saleVolume)
        else:
            carModels[str(i.carModel)] += int(i.saleVolume)
    carModels = sorted(carModels.items(), key=lambda x: x[1], reverse=True)
    mostModel = carModels[0][0]
    maxModel = carModels[0][1]
    #车型最多品牌
    carBrand = {}
    for i in cars:
        if carBrand.get(i.brand,-1) == -1:
            carBrand[str(i.brand)] = 1
        else:
            carBrand[str(i.brand)] += 1
    carBrand = sorted(carBrand.items(), key=lambda x: x[1], reverse=True)
    mostBrand = carBrand[0][0]
    maxBrand = carBrand[0][1]
    #车辆平均价格
    averagePrice = {}
    sumPrice = 0
    for i in cars:
        x = json.loads(i.price)[0] + json.loads(i.price)[1]
        sumPrice += x
    averagePrice = round(sumPrice / (sumCar*2),2)
    return sumCar,highVolume,topCar,mostModel,mostBrand,averagePrice

def getRollData():
    cars = list(getAllCars())
    carBrands = {}
    for i in cars:
        if i.brand not in carBrands:
            carBrands[str(i.brand)] = 1
        else:
            carBrands[str(i.brand)] += 1
    carBrands = sorted(carBrands.items(), key=lambda x: x[1], reverse=True)[:10]
    brandslist = [{"name":name,"value":value} for name,value in carBrands]
    return brandslist

def getTypeRate():
    cars = list(getAllCars())
    carTypes = {}
    for i in cars:
        if i.energyType not in carTypes:
            carTypes[i.energyType] = 1
        else:
            carTypes[i.energyType] += 1
    oilRate = round(carTypes["汽油"]/len(cars)*100,2)
    electricRate = round(carTypes["纯电动"]/len(cars)*100,2)
    otherRate = round((len(cars)-carTypes["汽油"]-carTypes["纯电动"])/len(cars)*100,2)
    return oilRate,electricRate,otherRate