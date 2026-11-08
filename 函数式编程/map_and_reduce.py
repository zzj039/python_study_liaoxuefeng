# 函数本身也可以赋值给变量，即：变量可以指向函数。
# 如果一个变量指向了一个函数，那么，可否通过该变量来调用这个函数？用代码验证一下，是可以的
f = abs
print(f)
print(f(-10))

# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x, y, f):
    return f(x) + f(y)

print(add(5, -10, abs))

# 编写高阶函数，就是让函数的参数能够接收别的函数。

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
    return x*x
r = map(f, [1,2,3,4,5])
print(list(r)) # r是一个惰性序列

# map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x*x，还可以计算任意复杂的函数
r2 = map(str, [1,2,3,4,5])
print(list(r2))

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce
def add_2(x, y):
    return x+y
r3 = reduce(add_2, [1,2,3,4,5])
