from http.client import responses
from wsgiref import headers
import requests
import csv
from lxml import etree
import os
import time
import json
import pandas as pd
import re
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','车辆大屏可视化.settings')
django.setup()
from myApp.models import carInfo

class spider():
    def __init__(self):
        self.url = "https://www.dongchedi.com/motor/pc/car/rank_data?aid=1839&app_name=auto_web_pc&city_name=%E9%95%BF%E6%B2%99&count=10&month=&new_energy_type=&rank_data_type=11&brand_id=&price=&manufacturer=&series_type=&nation=0&a_bogus=DJ4RDzyLxNAnKpCGmKmRC3clp%2FjMNsWyIqTdRytpS3c6aHUToEPLRca9bxuMNzRclRB92qIHAnslbfncYVU0129pqmhkSTijUs%2F59X8LMqqIalhkLHRuShsFqwMS0RwilAc6i1URAsMjId25IHIYAQVae5FLQO62SHM5p%2FT9jDCU3sgTno%2FttrvA%2Fqf%3D"
        self.headers = {"user-agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0",
                   "cookie":
"ttwid=1%7CbDMbfYAElSpvOQtaAUkgqiCHQlMMrzefM-xUis4NMRM%7C1776100069%7Cafec7fbc8d8aef6aafbba17ebe51a43fe113f06bda7c9593461ac20665d4cc03; tt_web_version=new; is_dev=false; is_boe=false; gfkadpd=1839,45203; x-web-secsdk-uid=a991f97a-8cf7-4e2a-9592-2cc092d9a54b; s_v_web_id=verify_mnxg4iqz_n7EV0VVm_HYZN_4pdt_99S9_iWJeIeXVr8wP; city_name=%E9%95%BF%E6%B2%99; tt_webid=7628291585725515289",
                   "referer":
"https://www.dongchedi.com/"}

    def init(self):
        if not os.path.exists("./temp.csv"):
            with open("./temp.csv","a",encoding="utf-8",newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["brand","carName","carImg","saleVolume","price","manufacturer","rank",
                                 "carModel","energyType","marketTime","insure"])

    def get_page(self):
        with open("./page.txt","r") as rf:
           return rf.readlines()[-1].strip()

    def set_page(self,Newpage):
        with open("./page.txt","a") as af:
            af.write("\n" + str(Newpage))

    def main(self):
        count = self.get_page()
        params = {"offset": int(count)}
        print("从第{}数据开始".format(int(count) + 1))
        print("-" * 30)
        pagejson = requests.get(self.url, headers=self.headers, params=params).json()
        pagejson = pagejson["data"]["list"]
        for index, car in enumerate(pagejson):
            try:
                print(f"正在爬取数据{index + 1}")
                carData = []
                carData.append(car["brand_name"])
                carData.append(car["series_name"])
                carData.append(car["image"])
                carData.append(car["count"])
                price = []
                min_price = car["min_price"]
                price.append(min_price)
                max_price = car["max_price"]
                price.append(max_price)
                carData.append(price)
                carData.append(car["sub_brand_name"])
                carData.append(car["rank"])

                id = car["series_id"]
                kid_url = f"https://www.dongchedi.com/auto/params-carIds-x-{id}"
                html = requests.get(kid_url, headers=self.headers).text
                html = etree.HTML(html)
                carModel = html.xpath("//div[@data-row-anchor='jb']/div[2]/div[1]/text()")[0]
                carData.append(carModel)
                energyType = html.xpath("//div[@data-row-anchor='fuel_form']/div[2]/div[1]/text()")[0]
                carData.append(energyType)
                marketTime = html.xpath("//div[@data-row-anchor='market_time']/div[2]/div[1]/text()")[0]
                carData.append(marketTime)
                insure = html.xpath("//div[@data-row-anchor='period']/div[2]/div[1]/text()")[0]
                carData.append(insure)
                print(carData)
                self.save_to_csv(carData)
            except:
                continue
        self.set_page(int(count) + 10)
        self.main()

    def save_to_csv(self,data):
        with open("./temp.csv","a",encoding="utf-8",newline="") as f:
            writer = csv.writer(f)
            writer.writerows(data)

    def clear_csv(self):
        df = pd.read_csv("./temp.csv")
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)
        print("清洗后数据总数为%d"%df.shape[0])
        df.to_csv("./temp.csv", index=False, encoding="utf-8")
        return df.values

    def save_to_sql(self):
        data = self.clear_csv()
        for car in data:
            carInfo.objects.create(
                brand=car[0],
                carName=car[1],
                carImg=car[2],
                saleVolume=car[3],
                price=car[4],
                manufacturer=car[5],
                rank=car[6],
                carModel=car[7],
                energyType=car[8],
                marketTime=car[9],
                insure=car[10],
            )
if __name__ == "__main__":
    obj = spider()
    obj.init()
    obj.main()
    # obj.clear_csv()
    obj.save_to_sql()