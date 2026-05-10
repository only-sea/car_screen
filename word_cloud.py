import numpy as np
from PIL import Image
import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud
import pymysql
import json

def get_wordcloud_img(field,targetImgSrc,resImgSrc):
    con = pymysql.connect(host='localhost', port=3306, user='root', passwd='20050811lh', charset='utf8mb4',database='cardata')
    cur = con.cursor()
    sql = f"select {field} from carinfo"
    cur.execute(sql)
    data = cur.fetchall()

    text = ''
    for i in data:
        if i[0] != None:
            tagArr = i
            for j in tagArr:
                text += j
    cur.close()
    con.close()
    data_cut = jieba.cut(text,cut_all=False)
    string = " ".join(data_cut)
    #图片
    img = Image.open(targetImgSrc)
    img_arr = np.array(img)
    wc = WordCloud(
        font_path='STHUPO.TTF',
        mask=img_arr,
        background_color='#04122c',
    )
    wc.generate_from_text(string)
    #绘制图片
    fig = plt.figure(1)
    plt.imshow(wc)
    plt.axis('off')

    plt.savefig(resImgSrc,dpi=800, bbox_inches='tight',pad_inches=0 )

get_wordcloud_img("manufacturer",'./big-screen-vue-datav-master/public/car.jpg','./big-screen-vue-datav-master/public/car_cloud.png')