

conda activate py39-torch1.12.1


python test.py --data data/coco.yaml --img 640 --batch 32 --conf 0.001 --iou 0.65 --device 0,1  --weights yolov7.pt --name yolov7_640_val_test &
