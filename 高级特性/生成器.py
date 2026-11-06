# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator

# 生成式的写法一
# 把列表生成式的中括号换成小括号
L = (x*x for x in range(10))

# 可以通过next()把一个generator的元素一个一个打印出来
for n in L:
    print(n)

# 所以，我们创建了一个generator后，基本上永远不会调用next()，
# 而是通过for循环来迭代它，并且不需要关心StopIteration的错误

# 方法二
# 一个函数中包含yield关键字，则这个函数是一个generator函数
# 调用一个generator函数将返回一个generator

# 变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
# 再次执行时从上次返回的yield语句处继续执行
def odd():
    print('第一步')
    yield 1
    print('第二步')
    yield 3
    print('第三步')
    yield 5

# 要创建一个对象接收generator函数的结果
o = odd()
next(o)
