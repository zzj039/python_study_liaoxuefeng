# 多重继承，比如要给动物分类，既要按照哺乳，鸟类分，也要按照会飞，会跑分
class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 可以额外再定义类
class Runnable(object):
    def run(self):
        print('I can run')

class Flyable(object):
    def fly(self):
        print('I can fly')

# 创建子类时，可以多重继承
class Dog(Mammal, Runnable):
    pass

# 通过多重继承，一个子类就可以同时获得多个父类的所有功能

# 在设计类的继承关系时，通常，主线都是单一继承下来的。
# 但是，如果需要“混入”额外的功能，通过多重继承就可以实现，。这种设计通常称之为MixIn。

# 所以，上述的Runnable类通常命名为RunnableMixIn

# MixIn的目的就是给一个类增加多个功能，
# 这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系