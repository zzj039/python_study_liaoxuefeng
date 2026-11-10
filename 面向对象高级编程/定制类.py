class Student(object):
    def __init__(self, name):
        self.name = name

    # 此时print(Student('Michael'))的结果不好看，可以定制：

    def __str__(self):
        return('Student object (name: %s)' % self.name)

    # 但是此时实例的打印没变，还是不好看
    # 方法是定义__repr__，但由于和上面写法一样，所以通常jianxie
    __repr__ = __str__

print(Student('Mike'))
s = Student('John')
print(s)


# __iter__

# __getitem__

# __getattr__

# __call__