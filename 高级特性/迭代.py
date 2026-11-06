# 只要是可迭代对象，无论有无下标，都可以迭代

# 所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，
# 而我们不太关心该对象究竟是list还是其他数据类型。

# 通过collections.abc模块的Iterable类型可以判断一个对象是否是可迭代对象
from collections.abc import Iterable
print(isinstance('abc', Iterable)) # str是否可迭代