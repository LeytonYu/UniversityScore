import os
import sys


# 批量修改文件名
def renameall():
    fileList = os.listdir(r"华东理工大学")
    print("修改前：" + str(fileList))
    currentpath = os.getcwd()
    os.chdir(r"华东理工大学")
    num = 1  # 名称变量
    for fileName in fileList:
        if fileName.startswith('20'):
            os.rename(fileName, (fileName + '.json'))
            num = num + 1
    print("---------------------------------------------------")
    os.chdir(currentpath)
    sys.stdin.flush()
    print("修改后：" + str(os.listdir(r"华东理工大学")))


if __name__ == '__main__':
    renameall()
