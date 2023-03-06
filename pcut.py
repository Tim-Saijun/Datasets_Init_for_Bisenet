# -*- coding:utf-8 -*-
#批量剪裁图片，保留位宽
from PIL import Image
import os
file_dir = r'J:\EV\ImageSegmentation\unet-nested-multiple-classification-master\data\test\unsed'
fileList = os.listdir(file_dir)
i = 1
for file_num in fileList:
	if file_num.endswith('json') or file_num.endswith('txt') :
		continue
	file_name = file_dir + '/' + file_num
	img = Image.open(file_name)
	print(img.size)
	big=r'J:\EV\ImageSegmentation\unet-nested-multiple-classification-master\data\test\input'
	small=r'J:\Desktop\SMALL'
	#过滤不同尺寸
	if img.size[1]!=1024:
		img.save(small+'/'+file_num)
		continue
	# croppedl = img.crop((0, 0, 960, 1024))  # (left, upper, right, lower),目标在左
	# save_dir = big + '/b'+file_num
	# croppedl.save(save_dir)

	# croppedr = img.crop((960, 0, 1920, 1024))  # (left, upper, right, lower),目标在右
	# save_dir = big +'/b'+file_num
	# croppedr.save(save_dir)

	croppedr = img.crop((485, 0, 1445, 1024))  # (left, upper, right, lower),目标在中间
	save_dir = big + '/b'+file_num
	croppedr.save(save_dir)
	#
	# croppeds = img.crop((0, 56, 1920, 1080))  # (left, upper, right, lower),一张图单个镜头
	# save_dir =big + '/'+file_num
	# croppeds.save(save_dir)
	#
	# croppedll = img.crop((0, 0, 960, 1024))  # (left, upper, right, lower),目标在左
	# croppedrr = img.crop((960, 0, 1920, 1024))  # (left, upper, right, lower),目标在右
	# save_dirl = big + '/'+ 'bl'+file_num
	# croppedll.save(save_dirl)
	# save_dirr = big + '/'+ 'br'+file_num
	# croppedrr.save(save_dirr)

	i += 1
