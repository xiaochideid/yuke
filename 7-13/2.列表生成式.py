
# 列表生成式：快速生成列表的一种方式
# 列表生成式的特点：会将所有的结果全部打印出来放在列表中，这样就会占用很大的内存，如果列表中的数据比较大，程序运行会比较卡顿甚至死机。
my_list=[]
for x in range(1,11):
    res=x*x
    my_list.append(res)
print(my_list)

fast_list=[x*x for x in range (1,11)]
print(fast_list)

# if 判断
fast_list_1=[x*x for x in range(1,11) if x!=2]
print(fast_list_1)
# 遍历（1,11）的数字让数字是奇数项的结果进行相乘运算x*x
fast_list_2=[x*x for x in range(1,11) if x%2==1]
print(fast_list_2)
# 列表生成式还支持双重for循环
my_list1=[]
for x in range(1,4):
    for y in range(1,4):
        res1=x*y
        my_list1.append(res1)
print(my_list1)


res2=[x*y for x in range(1,4) for y in range(1,4)]
print(res2)