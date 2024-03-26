#1.读取文件的总行数
with open('Day1.txt', 'r') as file:
    lines = file.readlines()
total_lines = len(lines)
print("总行数为：", total_lines)

