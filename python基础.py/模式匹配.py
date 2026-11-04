# 用if elif写判断时代码很长，可读性差

# 如果要针对某个变量匹配若干种情况，可以使用 match 语句。
score = 90
match score:
    case 90:
        print('A')
    case 80:
        print('B')
    case 70:
        print('C')
    case 60:
        print('D')
    case _: # 表示其他任何情况
        print('E')

# 复杂匹配
# match 语句除了可以匹配简单的单个值外，还可以匹配多个值、匹配一定范围，并且把匹配后的值绑定到变量
age = 20
match age:
    case x if x < 3: # 变量 x 已被赋值
        print('婴儿')
    case 3 | 4 | 5: # 可以匹配多个值
        print('幼儿')
    case 6 | 7 | 8:
        print('儿童')
    case _:
        print('其他年龄段')

# 匹配列表
args = ['gcc', 'hello.c', 'world.c']
match args:
    case ['gcc']:
        print('编译 hello.c')
    case ['gcc', *files]: # *files 表示匹配剩余所有元素，并把它们放到一个列表里
        print('编译', files)
    case _:
        print('invalid command')
