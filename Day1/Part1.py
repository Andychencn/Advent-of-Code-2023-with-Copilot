import os
import re

# 检查当前工作文件夹，解决了文件读取的路径问题
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

#在这个例子中，我们使用了Python的re模块，这是一个用于处理正则表达式的模块。re.findall函数会返回一个包含所有匹配的列表，我们的正则表达式\b\d+\b会匹配所有的整数。然后我们使用join函数将列表中的所有元素连接起来，形成一个新的字符串。最后，我们使用int函数将这个字符串转换为整数。
def concatenate_integers_in_string(s):
    if len(re.findall(r'\d+', s)) >=1:
        numbers = re.findall(r'\d+', s)
        concatenated_number = int(''.join(numbers))
    else:
        concatenated_number = 0
    return concatenated_number

#在这个例子中，我们首先使用str函数将整数转换为字符串。然后我们使用字符串的索引来获取首位和末位。字符串的索引是从0开始的，所以s[0]就是字符串的首位，s[-1]就是字符串的末位。最后我们使用int函数将这两个字符串转换回整数。
def get_first_and_last_digit(n):
    s = str(n)
    first_digit = int(s[0])
    last_digit = int(s[-1])
    return first_digit, last_digit

def replace(s):
    number_words = {
        r"\bzero\b": "0",
        r"\bone\b": "1",
        r"\btwo\b": "2",
        r"\bthree\b": "3",
        r"\bfour\b": "4",
        r"\bfive\b": "5",
        r"\bsix\b": "6",
        r"\bseven\b": "7",
        r"\beight\b": "8",
        r"\bnine\b": "9",
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9"
    }
    for word, number in number_words.items():
        if re.search(word, s):
            s = re.sub(word, number, s, count=1)
            break

    s = s[::-1]
    reversed_number_words = {word[::-1]: number for word, number in number_words.items()}
    for word, number in reversed_number_words.items():
        if re.search(word, s):
            s = re.sub(word, number, s, count=1)
            break
    s = s[::-1]

    return s


#1.读取文件的总行数
with open('Day1\Day1.txt', 'r') as file:
    lines = file.readlines()
total_lines = len(lines)

#2.创建一个循环，循环数为总行数。使用两个变量分别储存当前总校准值和当前行校准值
current_total = 0
current_line = 0
print(replace("eightwothree"))
for i in range(total_lines):

    #3.每个循环内先生成当前行校准值，再将该值与当前总校准值相加，生成新的总校准值
    true_line = replace(lines[i])
    current_line_count = concatenate_integers_in_string(true_line)
    #print(current_line_count)
    if 1 <= current_line_count <= 9:
        current_line = current_line_count * 10 + current_line_count
    if current_line_count >= 10:
        first_digit, last_digit = get_first_and_last_digit(current_line_count)
        current_line = first_digit * 10 + last_digit       
    current_total += current_line

#4.循环结束后输出总校准值
print("总校准值为：", current_total)



