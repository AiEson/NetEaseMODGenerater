import json
import uuid
import tkinter as tk
import os
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


def is_alphabet(uchar):
    """判断一个unicode是否是英文字母"""
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return False
    else:
        return True


def createFile(name, msg):
    full_path = name  # 也可以创建一个.doc的word文档
    file = open(full_path, 'w')
    file.write(msg)  # msg也就是下面的Hello world!
    file.close()


def mkdir(path):

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


shortName = input("请输入名称(只能使用英文)：")
while (is_alphabet(shortName)):
    shortName = input("不符合MOD创建条件，请重新输入：")
folderName = shortName + "Mod"
smallName = shortName.lower()
description = input("请输入manifest.json中的描述：")
Fpath = filedialog.askdirectory()
# Fpath = "C:\\Users\\23684\\PycharmProjects\\untitled1\\"
print(Fpath)
modBehaviorPack = Fpath + "\\" + folderName + "\\" + smallName + "BehaviorPack\\"
modResourcePack = Fpath + "\\" + folderName + "\\" + smallName + "ResourcePack\\"
mkdir(modBehaviorPack + smallName + "Scripts")
mkdir(modResourcePack + "textures")
mkdir(modResourcePack + "effects")
behaviorUuid1 = str(uuid.uuid4())
behaviorUuid2 = str(uuid.uuid4())
resourceUuid1 = str(uuid.uuid4())
resourceUuid2 = str(uuid.uuid4())
moduleBehavior = {"format_version": 1,
                  "header": {"description": description, "name": shortName, "uuid": behaviorUuid1, "version": [0, 0, 1]},
                  "modules": [
                      {"description": description, "type": "data", "uuid": behaviorUuid2, "version": [0, 0, 1]}]}
moduleResource = {
    "format_version": 1,
    "header": {
        "description": description,
        "name": shortName,
        "uuid": resourceUuid1,
        "version": [0, 0, 1]
    },
    "modules": [
        {
            "description": description,
            "type": "resources",
            "uuid": resourceUuid2,
            "version": [0, 0, 1]
        }
    ]
}
createFile(modBehaviorPack + "manifest.json", json.dumps(moduleBehavior, indent=4))
createFile(modResourcePack + "manifest.json", json.dumps(moduleResource, indent=4))
os.system("pause")
