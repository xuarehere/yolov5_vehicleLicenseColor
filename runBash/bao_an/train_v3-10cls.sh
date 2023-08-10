# 22.12.30 所有的类别信息
###
 # @Author: xujianrong
 # @Date: 2022-12-30 14:52:42
 # @LastEditTime: 2022-12-30 16:54:24
 # @LastEditors: xujianrong
 # @Description: 
 # @FilePath: /app/runBash/bao_an/train_v3-10cls.sh
 # 
### 
# cd ../../
CUDA_VISIBLE_DEVICES=0,1 python train.py --img 640 --batch 128 --epochs 100 --data sucity-10-v2-baoan.yaml --weights /workspace/models/yolov5/tensorrtx/yolov5s.pt --sync-bn  --device 0,1
