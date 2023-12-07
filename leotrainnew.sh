

conda activate py39-torch1.12.1

python train.py --workers 6 --device 0,1  --batch-size 32 --data data/leo_cust.yaml --img 640 640 --cfg cfg/training/leo_yolov7.yaml --weights '' --name yolov7-epoch5-batch32-worker6 --hyp data/hyp.scratch.p5.yaml  --epochs 50 &
