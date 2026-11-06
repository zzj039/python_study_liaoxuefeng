# 取一个list或tuple的部分元素是非常常见的操作
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 切片
l1 = L[0:3] #前三个
# 如果第一个是0，还可以省略
l2 = L[:3]
l3 = L[-2:] # 最后两个

n = 1
M = []
while n<100:
    M.append(n)
    n = n+1

l4 = M[:10:2] # 前十个数，每两个取一个
l5 = M[::5] # 所有的数，每5个取一个
l6 = M[:] # 复制原list

# tuple和字符串也可以切片
l7 = (1,2,3,4,5)[:2]
l8 = 'i love china'[::2]

# trim函数，可以删除字符串首尾的空格
# def trim(s):
#     n = 0
#     while n<len(s):
#         w = s[n]
#         if ord(w) == 32:
#             s = s[(n+1):]
#         n = n+1
#     return s

def trim(s):
    while s[0] == ' ':
        s = s[1:]
    while s[-1] == ' ':
        s = s[:-2]
    return s
if trim('  hello  ') == 'hello':
    print(trim('  hello  '))
    print('成功！')
