# 判断对象类型，使用type()函数
# 基本类型都可以用type()判断
print(type(123))

print(type(123)==int)

# 如果要判断一个对象是否是函数，可以使用types模块中定义的常量
import types
def f(n):
    pass
print(type(f) == types.FunctionType)

# 还可以使用isinstance函数
print(isinstance('123', str))

# 还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple
print(isinstance([1,2,3], (list, tuple)))

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print(dir('abc'))