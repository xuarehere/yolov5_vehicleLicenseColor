cd ../../
###
 # @Author: xujianrong xujianrong@sutpc.com
 # @Date: 2023-09-04 16:58:20
 # @LastEditTime: 2023-09-06 11:11:10
 # @LastEditors: xujianrong xujianrong@sutpc.com
 # @Description: 
 # @FilePath: /app/runBash/vehicle_count/vehicle_count_train_v2.1.sh
 # 
### 

 CUDA_VISIBLE_DEVICES=0,1 python train.py --img 640 --batch 128 --epochs 200 --data sucity-vehicle-5-v2.1.yaml --weights /workspace/models/yolov5/tensorrtx/yolov5s.pt --sync-bn  --device 0,1
 