# 面向对象最重要的概念就是类（Class）和实例（Instance），
# 必须牢记类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。

# 在Python中，定义类是通过class关键字
class Student(object): # object表示该类是从哪个类继承下来的
    pass

# 创建实例
bart = Student()
# 可以给一个实例绑定属性
bart.name = 'Mike'

# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
class Student_2(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，
# 因为self就指向创建的实例本身。

# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，
# 但self不需要传，Python解释器自己会把实例变量传进去
bart_2 = Student_2('John', 95)
print(bart_2.name, bart_2.score)

# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，
# 并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别

# 数据封装

# Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，
# 可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。
class Student_3(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_info(self):
        print('%s, %s' % (self.name, self.score))

bart_3 = Student_3('Lisa', 88)
bart_3.print_info() #切记，带上括号才是调用
