# 在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，这样，就可以知道是否有错，以及出错的原因。
# 在操作系统提供的调用中，返回错误码非常常见。
# 用错误码来表示是否出错十分不便，因为函数本身应该返回的正常结果和错误码混在一起，造成调用者必须用大量的代码来判断是否出错

# 所以高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外

# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，
# 即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
try:
    print('try...')
    r = 10 / 0
    # 当错误发生时，后续语句不会被执行，except由于捕获到ZeroDivisionError，因此被执行
    # 如果把0改成2，则么有错误，except不发生，继续按顺序执行
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
# 错误应该有很多种类，如果发生了不同类型的错误，应该由不同的except语句块处理
except ValueError as e:
    print('ValueError:', e)
# 如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句
else:
    print('no error')

finally:
    print('finally...')
print('end')

# 记录错误
import logging
def foos(s):
    return 10 / int(s)

def bar(s):
    return foos(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
        
# 同样是出错，但程序打印完错误信息后会继续执行，并正常退出
main()
print('end')

