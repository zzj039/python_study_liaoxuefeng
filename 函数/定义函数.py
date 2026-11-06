# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回。
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))

# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return。

# 如果想定义一个什么事也不做的空函数，可以用 pass 语句
def nop():
    pass
# 实际上 pass 可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

# 当传入了不恰当的参数时，内置函数 abs 会检查出参数错误，而我们定义的my_abs没有参数检查，会导致if语句出错，出错信息和abs不一样。
# 所以，这个函数定义不够完善。

# 对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现
def my_abs_2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs_2(-99))

# 返回多个值

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

# 但其实这只是一种假象，Python函数返回的仍然是单一值
# 如果用一个变量接收上述move的返回值，也是可以的
# 事实上，函数返回的是一个tuple，只不过语法上，返回一个tuple可以省略中括号
# 而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    return x1, x2