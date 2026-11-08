# filter()接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# 删除偶数，只留奇数
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1,2,3,4,5,6,7,8,9,10])))
