cd ../../
CUDA_VISIBLE_DEVICES=0,1 python train.py --img 640 --batch 64 --epochs 100 --data sucity-vehicle_count-5.yaml --weights /workspace/models/yolov5/tensorrtx/yolov5s.pt --sync-bn  --device 0,1
