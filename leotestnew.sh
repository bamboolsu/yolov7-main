

conda activate py39-torch1.12.1

# yolo 官方测试命令
#python test.py --data data/leo_cust.yaml --img 640 --batch 32 --conf 0.001 --iou 0.65 --device 0,1  --weights yolov7.pt --name yolov7_640_val_test &


# leo 的测试命令  --task test 其中的test 必须在leo_cust.yaml 里面存在才能是， 没有test的话，可以添加一个，或者使用val这个参数；
python test.py --device 0 --batch-size 2 --data data/leo_cust.yaml --img-size 640 --weights './runs/train/yolov7-epoch100-batch3-worker6/weights/best.pt' --conf-thres 0.1 --iou-thres 0.7 --task test
