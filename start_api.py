# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 17:28:16 2018

@author: IstukiHamano
"""

#必要なモジュールの読み込み
from flask import Flask,jsonify,abort,make_response,request
from keras.models import model_from_json
from keras.optimizers import SGD
from keras.preprocessing import image
from keras.applications.vgg16 import VGG16,preprocess_input,decode_predictions
import numpy as np
from numpy.random import *
import tensorflow as tf
from keras import backend as K
from PIL import Image

#Flaskクラスのインスタンス化
#__name__は現在のだいるのモジュール名
api=Flask(__name__)
load=True
#graph = tf.get_default_graph()


#POSTの口空ける
@api.route('/imgAnalysis',methods=['GET'])
def imgAn():#受け取り確認した
    value=request.files['upload_file']#jsonのkey名指定
    img = Image.open(value)
    img.show()
    #print(request.files)
    return make_response(jsonify({'answer':'aaaa'}))

#POSTの口空ける
@api.route('/imgAnalysis',methods=['POST'])
def imgAn2():
    model_file_name="car_model_from_VGG16.json"#作成したモデル（層の作り）を出力するファイル名
    weight_file_name="car_Transfer_Learning_Weight.h5"#学習済みモデルの重みを出力するファイル名
    model=model_from_json(open(model_file_name).read()) #作成したモデルの読み込み
    model.load_weights(weight_file_name)#学習済み重みの読み込み
    imgVec=np.random.normal(255,0.5,(1,224,224,3))
    
    value=request.files['upload_file']#jsonのkey名指定
    img = Image.open(value)
    #print(request.files)
    img=img.resize((224, 224))
    #img.show()
    x=image.img_to_array(img)#画像ベクトルに変換
    x=np.expand_dims(x,axis=0)#画像ベクトルをnumpy配列に変換
    preds=model.predict(preprocess_input(x))
    K.clear_session()
    preds=np.array(preds[0])
    labels=np.array(["Danger_Road","Safe_Road"])
    results=np.vstack((labels,preds))#結果のラベルづけ
    return str(results[0][0])+str(results[0][1])+str(results[1][0])+str(results[1][1])
  
     

@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'ermsg':'not found'}))

#ポート番号設定
if __name__=='__main__':
    api.run(port=7777)
    

    
