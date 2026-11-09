# 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，
# 新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）

# 父类
class Animal(object):
    def run(self):
        print('Animal is running...')

# 子类
class Dog(Animal):
    pass

class Cat(Animal):
    pass

# 继承最大的好处是子类获得了父类的全部功能。
# 由于Animal实现了run()方法，因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()方法
dog = Dog()
dog.run()

# 也可以对子类添加一些方法

# 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，
# 在代码运行的时候，总是会调用子类的run()。
# 这样，我们就获得了继承的另一个好处：多态
class Tiger(Animal):
    def run(self):
        print('Tiger is eating...')

# 理解多态
# 上面的animal, dog和list一样都是一种数据类型，可以用isinstance来检测

a = []
print(isinstance(a, list))
print(isinstance(dog, Dog))
# 但是对于dog来说，它也是Animal类型
# 如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行
print(isinstance(dog, Animal))