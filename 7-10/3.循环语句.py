   # 重点内容：
    # 1.for循环（遍历）
    # 2.while循环(一般不知道循环次数)

   # 循环打印1-10的数字
   # range():python的内置函数，用于设置范围。range()函数：取头不取尾。range(1,10)取值是1-9
for x in range(1,11):
    print(x)

string='恭喜LPL获得洲际赛冠军！'
for s in string:
    print(s)
    # 一般来说，能使用for循环遍历的，都可以称之为可迭代对象。
    # 循环中的两个关键字：
    # continue:用于中断for/while循环中的某一次循环，剩下的循环还会执行完毕。
    # break:用于中断整个for/while循环
for y in range (1,6):
    if y==2:
        break
    else:
        print('===',y)
for y in range(1,6):
    if y==2:
        continue
    else:
        print(y)


# .........while循环....
# while循环，执行的依据是判断while后面跟的条件是否成立，一般用于不知道循环的次数的情况下，使用while循环
# 当while后面跟的条件为真时，就会成为死循环。
# while True:
#     print('只是一个死循环！')
# while True:
#    print('我爱你！')
num =1
while num<=520:
    print('我爱你')
    num+=1