# 为了让计算机能计算成千上万次的重复运算，我们就需要循环语句。

# Python的循环有两种，一种是 for...in 循环，依次把 list 或 tuple 中的每个元素迭代出来
name = ['Michael', 'Bob', 'Tracy']
for n in name:
    print(n)

sum = 0
for x in [1, 2, 3, 4, 5]:
    sum = sum + x
print(sum)

list(range(5)) # [0, 1, 2, 3, 4]

sum = 0
for n in range(101): # 0-100
    sum = sum + n
print(sum)

# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum) # 100以内的奇数和

L = [
'Bart'
,
'Lisa'
,
'Adam'
]
for i in L:
    print('hello,', i)

# 在循环中，break 语句可以提前退出循环
n = 0
while n < 100:
    print(n)
    if n > 10:
        break
    n = n + 1
print('END')

# 在循环过程中，也可以通过 continue 语句，跳过当前的这次循环，直接开始下一次循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n) # 只输出奇数