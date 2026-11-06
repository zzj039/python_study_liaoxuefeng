# 默认参数
# 必选参数在前，默认参数在后，否则Python的解释器会报错
# 要注意，默认参数必须指向不变对象！！

def power(x, n=2): # 由于我们经常计算x的平方，所以，可以把第二个参数n的默认值设定为2
    return x**n

print(power(5,3))

# 可变参数：传入的参数个数是可变的
def calc(*numbers): # 参数numbers接收到的是一个tuple，因此，函数代码完全不变。
                    # 但是，调用该函数时，可以传入任意个参数，包括0个参数
    sum = 0
    for i in numbers:
        sum = sum + i*i
    return sum

# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
nums = [1, 2, 3]
calc(*nums)

# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

# 关键字参数有什么用？它可以扩展函数的功能。
# 比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到
def person(name, age, **kw):
    if 'city' in kw:
        pass # 检查是否有city
    print("name:", name, 'age:', age, 'other:', kw)
print(person('mike', 30))
print(person('john', 20, city='beijing', job='engineer'))

# 只接收city和job作为关键字参数，用 * 隔开
def person(name, age, *, city, job):
    print(name, age, city, job)