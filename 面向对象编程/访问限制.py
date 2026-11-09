# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        # 改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量.__name和实例变量.__score，注意，访问也不行！！
        # 要想获取信息，可以添加get函数
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

    def print_info(self):
        print('%s, %s' % (self.__name, self.__score))

    # 如果又要允许外部代码修改score怎么办？可以再给Student类增加set_score方法
    def set_score(self, score):
        self.__score = score

bart = Student('Endeavour', 100)
print(bart.get_name())
bart.print_info()

# 在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
# 特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名

# 一个常见的错误
# 在类的外部给__name重新赋值，看似赋值成功，
# 但实际上是给该实例创建了一个新的属性“__name”，因为在类中，__name实际上是_Student__name，但是不要在类外这样访问属性！！！