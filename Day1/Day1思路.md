1.读取文件的总行数
2.创建一个循环，循环数为总行数。使用两个变量分别储存当前总校准值和当前行校准值
3.每个循环内先生成当前行校准值，再将该值与当前总校准值相加，生成新的总校准值
    3.1先判断当前行包含多少数字，然后生成当前行校准值
        3.1.1如果当前行数字数为0，则当前行校准值为0
        3.1.2如果当前行数字数为1，则读取该数字，将该数字x10以后再和自身相加，结果为当前行校准值
        3.1.3如果当前行数字数>=2，则读取当前行的第一个和最后数字。使用一个变量储存第一个读取到的数字，另一个变量储存最后一个读取到的数字。将第一个数字X10后等到的结果与最后一个读取到的数字相加，得到的结果为当前行校准值
    3.2将当前总校准值与当前行校准值相加，得到新的总校准值
4.循环完成后输出总校准值。