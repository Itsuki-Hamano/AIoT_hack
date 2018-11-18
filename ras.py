# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 17:44:19 2018

@author: IstukiHamano
"""

from PIL import Image
import numpy as np
import requests
import json
import collections as cl


def img_set(url, imgpath):
    files = {'upload_file': open("fav_girl.jpg", "rb")}
    res = requests.post(url, files=files)
    return res

if __name__=='__main__':
    res=img_set('https://078ae6fb.ngrok.io/imgAnalysis','car.jpg')
    #res=img_set('http://localhost:5000/imgAnalysis','fav_girl.jpg')
    print(res.text)
