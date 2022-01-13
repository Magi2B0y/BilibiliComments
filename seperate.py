


open_diff = open('neg.txt', 'r',encoding='utf-8') # 源文本文件
diff_line = open_diff.readlines()

line_list = []
for line in diff_line:
    line_list.append(line)

count = len(line_list) # 文件行数
print('源文件数据行数：',count)
# 切分diff
diff_match_split = [line_list[i:i+1] for i in range(0,len(line_list),1)]# 每个文件的数据行数

# 将切分的写入多个txt中
for i,j in zip(range(0,49),range(0,49)): # 写入txt，计算需要写入的文件数
    #zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
    with open('./neg/%d.txt'% j,'w+') as temp:
        for line in diff_match_split[i]:
            temp.write(line)
print('拆分后文件的个数：',i+1)
