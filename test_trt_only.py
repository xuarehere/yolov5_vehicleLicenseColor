'''
Author: xujianrong xujianrong@sutpc.com
Date: 2023-09-19 10:29:09
LastEditTime: 2023-09-19 10:46:17
LastEditors: xujianrong xujianrong@sutpc.com
Description: 
FilePath: /yolov5_vehicleLicenseColor/test_trt_only.py

'''
import numpy as np

class calculate_result:
    def __init__(self) -> None:
        self.val_trt_output_dir = "/workspace/py/yolov5_tensorrtx_vehicleLicenseColor/build/results"
        self.val_server_dir = '/workspace/dataset/vehicleLicenseColor/val/images/'
        self.val_trt_output_files=[]
        
    def read_txt(self, file_path):
        """
        输入坐标  # id, x, y, width, height, conf ，其中xy指的是图像的左上角的位置
        
        输出坐标格式x1y1x2y2, conf, cls
        x1y1---------
        |            |  
        |            |  
        -------------x2y2
        """
        with open(file_path, 'r') as f:
            
            l = np.array([x.split() for x in f.read().strip().splitlines()], dtype=np.float32)  # labels
            # 读入坐标格式
            # id, x, y, width, height, conf ，其中xy指的是图像的左上角的位置
            # 坐标转化
            # x1, y1 = l[1], l[2]
            # x2, y2 = l[1] + l[3], l[2] + l[4], # 右下角坐标
            data = np.zeros(l.shape)
            # x1y1
            data[:, 0] = l[:, 1]
            data[:, 1] = l[:, 2]
            
            # x2y2
            data[:, 2] = np.sum(l[:, [1, 3]], axis=1)
            data[:, 3] = np.sum(l[:, [2, 4]], axis=1)
            # conf
            data[:, 4] = l[:, 5]
            # id
            data[:, 5] = l[:, 0]
        return data        
    
    pass