a = int('abc') # 默认转换为十进制，也可以用base指定
b = int('abc', base = 16) # 指定转换为十六进制

# 简单说，functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
import functools
int2 = functools.partial(int, base = 2) # 固定了partial参数为二进制

# 注意到上面的新的int2函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值：
c = int2('abc', base = 8)

# 其余例子，如max：
# 效果是实际比较大小时会自动加上10来比较
max2 = functools.partial(max,10)
