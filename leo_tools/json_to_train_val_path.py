import os
import random
import shutil
import json
import numpy as np

# w = 1320
# h = 816

def json2txt(path_json,path_txt):
    with open(path_json,'r') as path_json:
        jsonx=json.load(path_json)
        w = jsonx['imageWidth']
        h = jsonx['imageHeight']
        # print(w,h)
        with open(path_txt,'w+') as ftxt:
            for shape in jsonx['shapes']:           
                xy=np.array(shape['points'])
                label=str(shape['label'])
                strxy = label
                for m,n in xy:
                    # strxy+= ' ' + str(m)+' '+str(n)
                    strxy+= ' ' + str(round(m/w,6))+' '+str(round(n/h,6))
                strxy+=label                                            
                ftxt.writelines(strxy+"\n")  


dir_images = 'lw_6_20_images/'                 #原始图片目录
dir_json = 'lw_6_20_labels/'                   #原始标签目录 json形式
dir_txt = 'lw_6_20_labels_new/'                #处理过的标签目录 txt形式
dir_images_train = 'lw_6_20_images_train/'     #原始图片训练集目录
dir_images_val = 'lw_6_20_images_val/'         #原始图片验证集目录
dir_labels_train = 'lw_6_20_labels_new_train/' #处理过的标签训练集目录 txt形式
dir_labels_val = 'lw_6_20_labels_new_val/'     #处理过的标签验证集目录 txt形式



#################################将json标注转换为坐标形式的txt################################
if not os.path.exists(dir_txt):
    os.makedirs(dir_txt)
list_json = os.listdir(dir_json)
for cnt,json_name in enumerate(list_json):
    print('cnt=%d,name=%s'%(cnt,json_name))
    path_json = dir_json + json_name
    path_txt = dir_txt + json_name.replace('.json','.txt')
    #print(path_json,path_txt)    
    json2txt(path_json,path_txt)


##################################训练集验证集分配############################################
if not os.path.exists(dir_images_train):
    os.makedirs(dir_images_train)
if not os.path.exists(dir_images_val):
    os.makedirs(dir_images_val)
if not os.path.exists(dir_labels_train):
    os.makedirs(dir_labels_train)
if not os.path.exists(dir_labels_val):
    os.makedirs(dir_labels_val)


# 输出到txt文件，txt文件的路径
path_train_txt = "train.txt"
path_val_txt = "val.txt"

# 打开txt文件
file_handle_train=open(path_train_txt, mode='w')
# 打开txt文件
file_handle_val=open(path_val_txt, mode='w')
# 打开目标路径
datanames = os.listdir(dir_json)
val_num = 30
train_num = len(datanames) - val_num
random.shuffle(datanames)
datanames_train = datanames[:train_num]
datanames_val = datanames[train_num:]

#训练集相关
for filename in datanames_train:
    # filename = os.path.splitext(i)[0]
    print(filename)
    # 第一个 '-' 删除/替换成''
    fn = '../UCAS50/images/train/' + filename.replace('.json','.jpg')+ '\n'
#       指定位置删除/替换
#        filename = filename[:3] + '' + filename[4:] + '\n'
#        print(filename)
    file_handle_train.write(fn)

    shutil.copy(dir_images + filename.replace('.json','.jpg'),dir_images_train + filename.replace('.json','.jpg'))
    shutil.copy(dir_txt + filename.replace('.json','.txt'),dir_labels_train + filename.replace('.json','.txt'))
file_handle_train.close()

#测试集相关
for filename in datanames_val:
    # filename = os.path.splitext(i)[0]
    print(filename)
    # 第一个 '-' 删除/替换成''
    fn = '../UCAS50/images/val/' + filename.replace('.json','.jpg')+ '\n'
    file_handle_val.write(fn)

    shutil.copy(dir_images + filename.replace('.json','.jpg'),dir_images_val + filename.replace('.json','.jpg'))
    shutil.copy(dir_txt + filename.replace('.json','.txt'),dir_labels_val + filename.replace('.json','.txt'))
file_handle_val.close()