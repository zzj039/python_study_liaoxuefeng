# 如果我们想要限制实例的属性，比如，只允许对Student实例添加name和age属性，则要使用__slots__
class Student(object):
    __slots__ = ('name', 'age') #用tuple定义允许绑定的属性

s = Student()
s.name = 'mike'
s.age = 23
s.score = 60 # 失败

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__