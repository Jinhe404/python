# -*- codeing = utf-8 -*-
# @Time : 2023/3/21 10:16
# @File : 6.py
import os
import trimesh


def convert_off_to_obj(input_folder, output_folder):
    """
    将输入文件夹中的.off文件批量转换为.obj文件，并导出到输出文件夹中。

    Args:
        input_folder (str): 输入文件夹路径。
        output_folder (str): 输出文件夹路径。
    """
    # 如果输出文件夹不存在，则创建它
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有.off文件
    for file in os.listdir(input_folder):
        if file.endswith('.off'):
            # 读取.off文件
            input_path = os.path.join(input_folder, file)
            mesh = trimesh.load(input_path)

            # 将网格写入.obj文件
            output_path = os.path.join(output_folder, file[:-4] + '.obj')
            with open(output_path, 'w') as f:
                f.write(trimesh.exchange.obj.export_obj(mesh))

            print('Converted', file, 'to', output_path)


# 调用函数进行转换
input_folder = 'G:/zhongji/Mesh/ModeNet/ModelNet40/xbox/train'
output_folder = 'G:/zhongji/Mesh/ModeNet40/xbox/train'
convert_off_to_obj(input_folder, output_folder)

