import json
import time
from .getPublicData import *

def getEnergyType_VolumeData():
    cars = list(getAllCars())
    oilData = []
    electricData = []
    for i in cars:
        if i.energyType == '汽油':
            oilData.append([i.carName,i.saleVolume,i.energyType])
        if i.energyType == '纯电动':
            electricData.append([i.carName,i.saleVolume,i.energyType])
    return oilData[:10], electricData[:10]