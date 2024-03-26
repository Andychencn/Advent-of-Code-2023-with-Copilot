
# 检查当前工作文件夹，解决了文件读取的路径问题
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

#1.读取文件的总行数
with open('Day1\Day1.txt', 'r') as file:
    lines = file.readlines()
total_lines = len(lines)
print("总行数为：", total_lines)

