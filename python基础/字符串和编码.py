# 计算机是由外国人发明的，计算机只认数字和编码，于是最初只有127个字符，对应的字符集是ASCII码表。

# 但是随着计算机的普及，ASCII码表已经无法满足人们的需求了，于是就有了Unicode编码。可以表示中文，日语等其他语言。

# ASCII码表是单字节编码，Unicode编码是多字节编码。

# 但是当文本多是英文时，使用Unicode编码会浪费空间，于是就有了UTF-8编码。

# UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。

# UTF-8编码有一个额外的好处，就是ASCII编码实际上可以被看成是UTF-8编码的一部分，所以，大量只支持ASCII编码的历史遗留软件可以在UTF-8编码下继续工作。

# 对于单个字符的编码，Python提供了 ord() 函数获取字符的整数表示， chr() 函数把编码转换为对应的字符
print(ord('A')) # 输出：65
print(ord('中')) # 输出：20013
print(chr(65)) # 输出：A

# Python对 bytes 类型的数据用带 b 前缀的单引号或双引号表示
b = b'Hello, world!' # 要注意区分 'ABC' 和 b'ABC' ，前者是 str ，后者虽然内容显示得和前者一样，但 bytes的每个字符都只占用一个字节

# 以 Unicode表示的 str 通过 encode() 方法可以编码为指定的 bytes
'ABC'.encode('ascii') # 输出：b'ABC'
'中文'.encode('utf-8') # 输出：b'\xe4\xb8\xad\xe6\x96\x87'

# 含有中文的 str 无法用 ASCII 编码，因为中文编码的范围超过了 ASCII 编码的范围，Python会报错。

# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是 bytes 。要把 bytes变为 str ，就需要用 decode() 方法
b'ABC'.decode('ascii') # 输出：'ABC'
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') # 输出：'中文'

# 要计算 str 包含多少个字符，可以用 len() 函数
len('ABC') # 输出：3
len('中文') # 输出：2
len('中文'.encode('utf-8')) # 输出：6，len()函数计算的是字节数，所以中文的字节数是3个字节

'''
# 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。
# 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
'''

# 格式化 用 % 来实现
'hello, %s' % 'world' # 输出：'hello, world'
'Hi, %s, you have $%d.' % ('Michael', 1000000) # 输出：'Hi, Michael, you have $1000000.'
# 当只有一个%时，括号可以省略
# 当字符串里有 % 时，要写成 %%，这样就不会被当成占位符了

# 一种格式化字符串的方法是使用以 f 开头的字符串，称之为 f-string ，它和普通字符串不同之处在于，字符串如果包含 {xxx} ，就会以对应的变量替换
name = 'Michael'
age = 20
f'Hello, {name}, you are {age:.2f} years old.' # 输出：'Hello, Michael, you are 20.00 years old.'，.2f 表示保留两位小数

s1 = 72
s2 = 85
r = (85 - 72) / 72
print(f'小明成绩由{s1}提升到了{s2}，成绩提升了{r:.1f}%') # 输出：'小明成绩由72提升到了85，成绩提升了18.1%'

