

conda activate py39-torch1.12.1

#official detect
#python detect.py --weights yolov7.pt --conf 0.25 --img-size 640 --source inference/images/20231207103708.jpg 

#leo detect --conf 0.45 --iou 0.10
python  detect.py --weights ./runs/train/yolov7-epoch150-batch4-worker6/weights/best.pt --source  ./test/ 

