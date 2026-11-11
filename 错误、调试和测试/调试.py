# 程序能一次写完并正常运行的概率很小，基本不超过1%。
# 总会有各种各样的bug需要修正。
# 有的bug很简单，看看错误信息就知道，有的bug很复杂，我们需要知道出错时，哪些变量的值是正确的，哪些变量的值是错误的，
# 因此，需要一整套调试程序的手段来修复bug。

# 第一种方法简单直接粗暴有效，就是用print()把可能有问题的变量打印出来看看
# 用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息。

# 第二种方法是用断言（assert）来替代print
def foo(s):
    r = int(s)
    assert r != 0, 'r is zero'
    return 10 / r
# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
# 如果断言失败，assert语句本身就会抛出AssertionError：AssertionError: r is zero

# 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert

# logging等方法