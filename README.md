<!--
 * @Author: xujianrong xujianrong@sutpc.com
 * @Date: 2022-11-18 15:31:49
 * @LastEditTime: 2023-08-10 15:25:06
 * @LastEditors: xujianrong xujianrong@sutpc.com
 * @Description: 
 * @FilePath: /app/README.md
 * 
-->


# 训练
```
CUDA_VISIBLE_DEVICES=0,1 python train.py --img 640 --batch 64 --epochs 100 --data sucity-19-baoan.yaml --weights /workspace/models/yolov5/tensorrtx/yolov5s.pt --sync-bn  --device 0,1
```


# 测试
```
CUDA_VISIBLE_DEVICES=0,1 python test.py  --data sucity-vehicle-5-v1.1.yaml    --weights /workspace/py/ultralytics/yolov5_container/app/runs/train/exp11/weights/best.pt   --batch 128

```

# 推理
```
python detect.py --source data/images --weights yolov5s.pt --conf 0.25
```