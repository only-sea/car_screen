import time
import json
from .getPublicData import *

def getPieVolumeData():
    cars = getAllCars()
    carVolumes= {}
    for i in cars:
        if i.brand not in carVolumes:
            carVolumes[i.brand] = int(i.saleVolume)
        else:
            carVolumes[i.brand] += int(i.saleVolume)
    carVolumes = sorted(carVolumes.items(), key=lambda x: x[1], reverse=True)
    carVolumes = [{"name":name,"value":value} for name,value in carVolumes][:10]
    return carVolumes
