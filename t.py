#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :t.py
# @Time      :2023/3/5 21:28
# @Author    :Tim-Saijun
# @Site      : http://zairun.eu.org


import os
from PIL import Image
import numpy as np

#将一张图片大小转换为1080*960，然后保存在output文件夹中
def resize_img(img_path):
    img = Image.open(img_path)
    img = img.resize((960,1024),Image.ANTIALIAS)
    img.save(img_path)

#将before文件夹中的图片使用resize_img函数转换为1080*960，然后保存在output文件夹中
def resize_img_folder():
    img_path = os.path.join(os.getcwd(),'before')
    img_list = os.listdir(img_path)
    for img in img_list:
        img_path = os.path.join(os.getcwd(),'output',img)
        resize_img(img_path)

resize_img_folder()

