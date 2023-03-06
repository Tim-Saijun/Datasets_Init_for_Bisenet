import cv2
import os
from PIL import Image
import matplotlib.image as mpimg
import numpy as np
M=6
imga = Image.open(r'J:\Desktop\BIG\masks\{E5CC7ABF-6E76-4451-8570-D79F3D014D6B}.bmp')
imgb = Image.open(r'J:\Desktop\bad\masks\bb{1DE32B8B-2ADB-4B4C-8764-7A393DCDF185}.bmp')
# image.flags.writeable = True  # 将数组改为读写模式`
liss=np.array(imga)
for i in range(959):
        for k in range(1023):
                if liss[k][i]==M:
                    liss[k][i]=255
liss = Image.fromarray(liss.astype('uint8')).convert('RGB')
liss.save('/a' + "%d.png"%M)

liss=np.array(imgb)
for i in range(959):
        for k in range(1023):
                if liss[k][i]==M:
                    liss[k][i]=255
liss = Image.fromarray(liss.astype('uint8')).convert('RGB')
liss.save('/b' + "%d.png"%M)
