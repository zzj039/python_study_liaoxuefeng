# 函数对象有一个__name__属性（注意：是前后各两个下划线），可以拿到函数的名字
def now():
    print('hello')

f = now
print(now.__name__)
print(f.__name__)

# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下
def log(func):
    def wrapper(*args, **kw):
        print('call %s():'% func.__name__)
        return func(*args, **kw)
    return wrapper

# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
# 我们要借助Python的 @ 语法，把decorator置于函数的定义处
@log
def now():
    print('hello')

# 后续还有些内容没写，些许复杂，直接看pdf对应内容