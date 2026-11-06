# 写列表生成式时，把要生成的元素(如：x * x）放到前面，后面跟for循环，就可以把list创建出来

L = [x*x for x in range(1,11)]
print(L)
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
L2 = [x*x for x in range(1, 11) if x % 2 == 0]
print(L2)

# 还可以使用两层循环，可以生成全排列
L3 = [m + n for m in 'ABC' for n in 'XYZ']