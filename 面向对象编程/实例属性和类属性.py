# 由于Python是动态语言，根据类创建的实例可以任意绑定属性。
# 给实例绑定属性的方法是通过实例变量，或者通过self变量
class Student(object):
    def __init__(self, name):
        self.name = name
    # 如果Student类本身需要绑定一个属性,可以直接在class中定义属性，
    # 这种属性是类属性，归Student类所有
    gentle = 'fma'

s = Student('John')
s.score = 90 # 可以添加属性

# 类中定义的属性，类本身和对象都可以访问
print(s.gentle)
print(Student.gentle)

# 但如果给对象的这个属性重新赋值，则会覆盖类中定义的初值
s.gentle = '男或女'
print(s.gentle)

# 但这并不影响类本身。而且，如果把实例的该属性删除，则会默认再次使用类中的初始值
print(Student.gentle)

del s.gentle

print(s.gentle)
print(Student.gentle)

'''
从上面的例子可以看出，在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，
因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

'''