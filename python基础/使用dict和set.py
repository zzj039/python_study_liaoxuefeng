# Python内置了字典：dict 的支持，dict 全称 dictionary，在其他语言中也称为 map，使用键-值（key-value）存储，具有极快的查找速度。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob']) # 75

# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d['Adam'] = 67

# 由于一个 key 只能对应一个 value，所以，多次对一个 key 放入 value，后面的值会把前面的值冲掉

# 要避免 key 不存在的错误，有两种办法，一是通过 in 判断 key 是否存在
'Tom' in d # False

# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
d.get('Tom') # None，默认返回不显示
d.get('Tom', -1) # -1

# 要删除一个 key，用 pop(key) 方法，对应的value也会从dict中删除
d.pop('Tom') # 如果key存在，删除并返回对应的value，否则抛出KeyError

# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的

# 需要牢记的第一条就是dict的key必须是不可变对象
# 作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
s = {1, 2, 3}
# 或者提供一个list作为输入集合
s = set([1, 2, 3])

# 重复元素在set中自动被过滤

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果

# 通过remove(key)方法可以删除元素
s.remove(2) # 删除元素2

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2 # 交集
s1 | s2 # 并集

# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，
# 同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”

# 再议不可变对象
a = 'abc'
a.replace('a', 'A')
print(a) # 依旧是abc
b = a.replace('a', 'A')
print(b) # Abc
# 当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，
# 而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。
# 相反，replace方法创建了一个新字符串'Abc'并返回，
# 如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了

# 所以，对于不变对象来说（比如上面的 str 类型 a），调用对象自身的任意方法，也不会改变该对象自身的内容。
# 相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。