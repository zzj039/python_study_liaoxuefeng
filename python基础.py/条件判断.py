age = 6
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# if语句执行有个特点，它是从上往下判断，如果在某个判断上是 True，把该判断对应的语句执行后，就忽略掉剩下的 elif 和 else

# 只要 x 是非零数值、非空字符串、非空 list 等，就判断为 True，否则为 False
x = 1
if x:
    print('True')

# 再议 input
s = input('brith:') # input()返回的是字符串,需要用int()把字符串转换为整数
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

# 但如果输入的不是数字，int()函数就会报错，程序就退出了

high = 1.75
weight = 80.5
bmi = weight / (high * high)
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
else:
    print('肥胖')

