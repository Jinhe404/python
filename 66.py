# -*- codeing = utf-8 -*-
# @Time : 2023/3/21 20:12
# @File : 66.py
import os
import pymesh

def check_zero_faces(mesh):
    """检查一个网格是否有零面并将其删除"""
    zero_faces = mesh.faces_with_area(0.0)
    if len(zero_faces) > 0:
        mesh.delete_faces(zero_faces)
        print("删除了{}个零面".format(len(zero_faces)))

def convert_off_to_obj(off_file_path):
    """将一个OFF文件转换为OBJ文件"""
    # 读取OFF文件
    mesh = pymesh.read_mesh(off_file_path)

    # 检查是否有零面并删除它们
    check_zero_faces(mesh)

    # 构建输出OBJ文件路径
    obj_file_path = os.path.splitext(off_file_path)[0] + ".obj"

    # 保存为OBJ文件
    pymesh.save_mesh(obj_file_path, mesh)

    print("转换完成：{} -> {}".format(off_file_path, obj_file_path))

def batch_convert_off_to_obj(folder_path):
    """批量将文件夹中的所有OFF文件转换为OBJ文件"""
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".off"):
            off_file_path = os.path.join(folder_path, file_name)
            convert_off_to_obj(off_file_path)

if __name__ == '__main__':
    folder_path = "G:/zhongji/Mesh/ModeNet6/airplane/train"
    batch_convert_off_to_obj(folder_path)





# G:/zhongji/Mesh/ModeNet6/airplane/train