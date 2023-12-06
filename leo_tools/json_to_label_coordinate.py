import os
import json
import numpy as np

# w = 1320
# h = 816


# 指定目录 leo_training 里面的json 转换到 txt 格式； 



def json2txt(path_json,path_txt):
    with open(path_json,'r',encoding='gb18030',errors = 'ignore') as path_json:  #windows add  ,encoding='gb18030'，errors = 'ignore'
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


# dir_json = 'lw_labels/'
# dir_txt = 'lw_labels_new/'

currentpath = os.getcwd()
#dir_json = 'leo_training/'  #linux format
#dir_txt = 'leo_training/'  #linux format

dir_json = currentpath + '\\jsonpath\\'  #windows format
dir_txt = currentpath + '\\jsonpath\\'   #windows format
if not os.path.exists(dir_txt):
    os.makedirs(dir_txt)
list_json = os.listdir(dir_json)
for cnt,json_name in enumerate(list_json):
    print('cnt=%d,name=%s'%(cnt,json_name))
    path_json = dir_json + json_name
    path_txt = dir_txt + json_name.replace('.json','.txt')
    #print(path_json,path_txt)    
    json2txt(path_json,path_txt)
