

import torch 
import torchvision
import numpy as np
"""

对类别之间进行nms计算，并且对特定的类别进行映射处理
"""
output = torch.load("output.pth")[0].cpu()
print(output)

def compute_IOU(rec1, rec2, denominator_type=None):
    """
    计算两个矩形框的交并比。
    :param rec1: (x0,y0,x1,y1)      (x0,y0)代表矩形左上的顶点，（x1,y1）代表矩形右下的顶点。下同。
    :param rec2: (x0,y0,x1,y1)
    :param denominator_type: IOU 分母，默认是 None，默认的IOU 求法。 denominator_type="rec1" 则使用 rec1 作为分母
    :return: 交并比IOU.
    """
    ret = 0.0
    left_column_max = max(rec1[0], rec2[0])
    right_column_min = min(rec1[2], rec2[2])
    up_row_max = max(rec1[1], rec2[1])
    down_row_min = min(rec1[3], rec2[3])
    # 两矩形无相交区域的情况
    if left_column_max >= right_column_min or down_row_min <= up_row_max:
        return 0
    # 两矩形有相交区域的情况
    else:
        S1 = (rec1[2] - rec1[0]) * (rec1[3] - rec1[1])
        S2 = (rec2[2] - rec2[0]) * (rec2[3] - rec2[1])
        S_cross = (down_row_min - up_row_max) * (right_column_min - left_column_max)
        # return S_cross / (S1 + S2 - S_cross)
    if denominator_type == "rec1":
        return S_cross / S1 
    elif denominator_type == "rec2":
        return S_cross / S2 
    else:
        # 标准的 IOU 求法
        return S_cross / (S1 + S2 - S_cross)

def class_nms(output):
    names= ["Bus",
            "Car" ,
            "Cycle" , 
            "Pedestrian" , 
            "Truck",
            "BigTruck",
            "Tanker",
            "GarbageTruck",
            "MuckTruck",
            "CoachesCar",]
        
    l = len(output)
    ious_label_thres = 0.9
    output_new = []
    # 进行类别之间的nms时候，选择置信度，用于矫正id
    # 一个目标同时出现两个类别，进行映射处理
    # id_map = {
    #     names.index("Bus"):names.index("Bus"),
    #     names.index("Car"):names.index("Truck"),
    #     names.index("Cycle"):names.index("Cycle"),
    #     names.index("Pedestrian"):names.index("Pedestrian"),
    #     names.index("Truck"):names.index("Truck"),
    #     names.index("BigTruck"):names.index("BigTruck"),
    #     names.index("Tanker"):names.index("Tanker"),
    #     names.index("GarbageTruck"):names.index("GarbageTruck"),
    #     names.index("MuckTruck"):names.index("MuckTruck"),
    #     names.index("CoachesCar"):names.index("CoachesCar"),
    # }

    is_label_change = True      # 进行 id 矫正
    for i in range(l-1):
        rec1 = output[i]
        rec_save = output[i]
        for j in range(i+1, l):
            # if i ==10:
            #     print("==>")        
            rec2 = output[j]
            iou = compute_IOU(rec1, rec2)   # x0,y0,x1,y1, conf, id
            # 需要进行类别 nms
            if iou >ious_label_thres:
                # 取置信度高的框
                if rec1[4]>rec2[4]:
                    rec_save = rec1
                else:
                    rec_save = rec2
        
                if is_label_change:
                    # 一个目标同时出现两个类别，进行映射处理
                    if int(rec1[5]) ==  names.index("Truck") or int(rec2[5]) ==  names.index("Truck"):
                        # 两个类别，出现了Truck，将其划分为 Truck
                        rec_save[5] = names.index("Truck")
            else:
                continue
            print("i:{}, j:{}, iou:{}", i,j,iou)
        rec_save = torch.reshape(rec_save, (1,-1))
        if i ==0:
            output_new.append(rec_save)
        else:
            output_new[0] = torch.cat((output_new[0], rec_save), 0)
    print(output_new)
    
    
def main():
    class_nms()

if __name__ =="__main__":
    main()
    pass