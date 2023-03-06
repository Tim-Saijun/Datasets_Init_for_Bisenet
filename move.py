#该文件用于整理数据集，作用是将与path0文件夹下同名的、处在path1的所有文件移动到path2
import shutil
import glob
import os
path0=r"J:\EV\ImageSegmentation\unet-nested-multiple-classification-master\data\images\右" #对照的文件夹路径
path1=r"J:\EV\ImageSegmentation\unet-nested-multiple-classification-master\data\masks"#文件来源路径
path2=r"J:\EV\ImageSegmentation\unet-nested-multiple-classification-master\data\masks\右"     #剪切到的文件夹路径
move_list=os.listdir(path0)
file_list=glob.glob(path1+"/*.bmp")
# print(file_list)
for i in range(len(file_list)):
    for j in range(len(move_list)):
        if file_list[i].endswith(move_list[j]):
            shutil.move(file_list[i],path2)

