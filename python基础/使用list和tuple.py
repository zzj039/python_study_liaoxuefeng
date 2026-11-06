# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', 'Tracy']
len(classmates)  # 获取list元素个数
print(classmates[0])  # 获取第一个元素
# 如果要取最后一个元素，除了计算索引位置外，还可以用 -1 做索引，直接获取最后一个元素
print(classmates[-1])  # 获取最后一个元素

# list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('Adam')

# 也可以把元素插入到指定的位置，比如索引号为 1 的位置
classmates.insert(1, 'Jack')

# 要删除list末尾的元素，用 pop() 方法
classmates.pop()

# 要删除指定位置的元素，用 pop(i) 方法，其中 i 是索引位置
classmates.pop(1)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Sarah'

# list里面的元素的数据类型也可以不同，也可以是另一个list
s = ['python', 'java', ['asp', 'php'], 'scheme'] # 注意，s只有4个元素，其中第3个元素是一个list
# 获取'php'可以写 s[2][1]，因此s可以看作是一个二维数组

# 如果一个list中一个元素也没有，就是一个空的list，它的长度为0
L = []
len(L)  # 0

# 另一种有序列表叫元组：tuple。tuple 和 list 非常类似，但是 tuple 一旦初始化就不能修改
mates = ('Michael', 'Bob', 'Tracy') # 内容不可修改，其余获取元素的方法和list是一样的，但不能使用append()、insert()这样的方法

# 因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple

# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
t = (1, 2) # 这是一个tuple
t = () # 这是一个空的tuple
t = (1) # 这是一个整数，不是tuple
t = (1,) # 这是一个只有1个元素的tuple, 需要加一个逗号, 否则括号()既可以表示tuple，又可以表示数学公式中的小括号,且python默认当成小括号处理

# ‘可变’的tuple
t = (1, [2, 3]) # tuple的元素含有list, list是可变的，所以tuple的元素“变了”，但tuple的元素指向的list并没有变
t[1][0] = 4 # 修改tuple中list的元素