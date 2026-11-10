# @property 装饰器就是负责把一个方法变成属性调用的
class Student(object):
    
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be a integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

# 属性方法名和实例变量重名，会造成递归调用，导致栈溢出报错
