import yaml
import os
import numpy as np
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


def convert(size, box):
    """convert coordinate to yolo label style

    Args:
        size (tuple or list): image shape (width, height)
        box (tuple or list): the coordinate of the rectange's corner

    Returns:
        tuple: yolo style bounding
    """
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(image_id):
    in_file = open(r'%s%s.xml' % (label_directory, image_id))
    out_file = open(r'%s%s.txt' % (txt_directory, image_id), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), 
             float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

if __name__ == '__main__':
    cfg = 'prep_config.yaml'
    with open(cfg, 'r') as f:
        params = yaml.safe_load(f)

    txt_directory = params['txt_directory']
    img_directory = params['img_directory']
    label_directory = params['label_directory']
    classes = params['classes']
    train_test_ratio = params['train_test_ratio']

    image_ids = []
    for f in os.listdir(label_directory):
        img_id, ends = f.split('.')
        if ends in ['xml', 'txt']:
            image_ids.append(img_id)
    image_ids = sorted(image_ids)

    with open('img_path.txt', 'w') as list_file:
        for image_id in image_ids:
            try:
                if not os.path.isfile(txt_directory + image_id + '.txt'):
                    convert_annotation(image_id)
                list_file.write('%s%s.jpg\n'%(img_directory, image_id))
            except FileNotFoundError as e:
                print(e)

    with open('img_path.txt', 'r') as f:
        img_path = f.readlines()
    train = img_path
    validate = train[::train_test_ratio]
    del train[::train_test_ratio]
    with open('train.txt', 'w') as f:
        f.writelines(train)
    with open('validate.txt', 'w') as f:
        f.writelines(validate)