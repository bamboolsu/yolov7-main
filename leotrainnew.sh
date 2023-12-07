

conda activate py39-torch1.12.1

#leo add, --batch-size 一次传给cpu进行识别的个数；  cpu个数的整数倍； 
python train.py --workers 6 --device 0,1  --batch-size 4 --data data/leo_cust.yaml --img 640 640 --cfg cfg/training/leo_yolov7.yaml --weights '' --name yolov7-epoch150-batch4-worker6 --hyp data/hyp.scratch.p5.yaml  --epochs 150 &
