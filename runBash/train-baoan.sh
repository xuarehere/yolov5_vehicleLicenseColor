cd ../
CUDA_VISIBLE_DEVICES=0,1 python train.py --img 640 --batch 128 --epochs 100 --data sucity-19-baoan.yaml --weights /workspace/models/yolov5/tensorrtx/yolov5s.pt --sync-bn  --device 0,1
