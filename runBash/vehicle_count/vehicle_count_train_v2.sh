cd ../../
###
 # @Author: xujianrong xujianrong@sutpc.com
 # @Date: 2023-09-04 16:58:20
 # @LastEditTime: 2023-09-04 17:01:18
 # @LastEditors: xujianrong xujianrong@sutpc.com
 # @Description: 
 # @FilePath: /app/runBash/vehicle_count/vehicle_count_train_v2.sh
 # 
### 

CUDA_VISIBLE_DEVICES=0,1 python train.py --img 640 --batch 64 --epochs 100 --data sucity-vehicle-5-v2.0.yaml --weights /workspace/models/yolov5/tensorrtx/yolov5s.pt --sync-bn  --device 0,1
```
Plotting labels...                                                                                                                 [7/111]
Writting labels to runs/train/exp63/labels_info.txt...
id      class   numbers
0       Car     169476
1       Bus     5916
2       Cycle   40004
3       Pedestrian      1059924       Truck   12873
label_nums = 334261                                                   

label_file_nums = 6465

Images sizes do not match. This will causes images to be display incorrectly in the UI.
Plotting labels...
Writting labels to runs/train/exp63/val_info/labels_info.txt...
id      class   numbers
0       Car     16039
1       Bus     251
2       Cycle   6173
3       Pedestrian      13969
4       Truck   750
label_nums = 37182

label_file_nums = 548
```