from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .utils import getPublicData
from .utils import getCenterData
from .utils import getCenterLeftData
from .utils import getBottomLeftData
from .utils import getCenterRightData
from .utils import getCenterMostRightData
from .utils import getBottomRightData
# Create your views here.
def center(request):
    if request.method == 'GET':
        sumCar,highVolume,topCar,mostModel,mostBrand,averagePrice=getCenterData.getBaseData()
        brandslist = getCenterData.getRollData()
        oilRate,electricRate,otherRate = getCenterData.getTypeRate()
        return JsonResponse(
                {
                    'sumCar':sumCar,
                    'highVolume':highVolume,
                    'topCar':topCar,
                    'mostModel':mostModel,
                    'mostBrand':mostBrand,
                    'averagePrice':averagePrice,
                    'brandslist':brandslist,
                    'oilRate':oilRate,
                    'electricRate':electricRate,
                    'otherRate':otherRate
                }
            )
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def centerleft(request):
    if request.method == 'GET':
        carVolumes = getCenterLeftData.getPieVolumeData()
        return JsonResponse(
            {
                "carVolumes":carVolumes
            }
        )
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def bottomleft(request):
    if request.method == 'GET':
        brandlist,volumelist,pricelist=getBottomLeftData.getSquareData()
        return JsonResponse(
            {
                "brandlist":brandlist,
                "volumelist":volumelist,
                "pricelist":pricelist
            }
        )
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def centerright(request):
    if request.method == 'GET':
        price_list = getCenterRightData.getCarVolume_PrinceData()
        return JsonResponse(
            {
                "pricelist":price_list
            }
        )
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def centermostright(request,energyType):
    if request.method == 'GET':
        oilData, electricData = getCenterMostRightData.getEnergyType_VolumeData()
        realData = []
        if energyType == 1:
            realData = oilData
        else:
            realData = electricData
        return JsonResponse(
            {
                "realData":realData
            }
        )
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def bottomright(request):
    if request.method == 'GET':
        carData = getBottomRightData.getRankData()
        return JsonResponse(
            {
                "carData":carData
            }
        )
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

