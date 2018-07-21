# 重点内容：
# 1.添加数据【append()、insert()】
# 2.删除数据【pop()、del、remove()、循环删除（for循环遍历长度）】
# 3.查询数据【索引值、切片、倒叙、遍历、枚举】
# 4.修改数据【索引值赋值】
# 5.常用函数：【count、index、reverse、sort、extend、clear】


# 列表定义：（关键字list）,是一种容器类型的数据，里面可以保存整数、小数、True/False、字符串、列表、元组、字典、对象等等类型的数据。列表是可变的，可以删除，增加，修改查询等。
# ...............创建列表...............
# 创建一个空列表
list1=[]
# 创建一个非空列表
list2=[20,9.88,True,'张三']
# ...............添加数据..............
# 1.append():括号里面直接填入的数据，默认会添加列表的末尾位置。
list1.append('李四')
print(list1)
# 索引：他是从0开始，一次向后加1个整数，用于标记元素在容器中的存放位置，解释器会默认给每一个元素设置一个索引值，可以更具索引值对元素增删改查的操作。索引值是唯一的不能重复。
# 2.insert():可以根据元素的索引值插入指定的数据，第一个参数：要插入的索引位置；第二个参数：要插入的元素值。
list1.insert(0,'小明')
print(list1)
list1.insert(1,'小红')
print(list1)

# ........删除数据....
list3=['张三','李四',20,False,'哈哈哈']

# 1.pop()函数：根据索引值，删除列表中的某一个元素。括号中填写的是索引值。如果列表中不填写索引值，默认删除最后一个
list3.pop(4)
print(list3)
list3.pop()
print(list3)

# 2.remove():括号中直接填写要删除的元素.如果要删除的元素在列表中存在多个，则默认删除第一个符合条件的元素。
list3.remove('李四')
print(list3)
list4=['张三','李四','王二','麻子','麻子']
list4.remove('麻子')
print(list4)

# 3.del():也是根据索引值删除元素
del list4[3]
print(list4)

# 4.使用循环删除列表中的所有元素。
# len():获取容器的长度
while len(list4):
    del list4[0]
    print(list4)

# ..............查询数据.............
# 1.根据索引值查询
list5=['uzi','7酱','让帝','司马老贼','mlxg','狗妃']
changzhang=list5[1]
print(changzhang)

# 2.切片取值，取头不取尾。从索引值为0的元素，取到索引值为2的元素
# 切片：【头下标：尾下表】
name=list5[0:3]
print(name)
# 从索引值为0的元素，取到索引值为5的元素，每次跳两个索引
name1=list5[0:6:2]
print(name1)

# 如果切片不设置头下标，则默认从0开始。
name2=list5[:6]
print(name2)
# 如果切片不设置下尾标，则默认取到末尾。
name3=list5[0:]
print(name3)
name4=list5[::2]
print(name4)
# 如果切片既不设置头下标也不设置尾下表，从头到尾
name5=list5[:]
print(name5)

# 倒序取值
list6=['edg','永不团灭','rng','永不言弃']
last=list6[-1]
print(last)
last1=list6[-2]
print(last1)
# 通过for循环查询所有元素
# 直接遍历所有元素
for x in list6:
    print(x)
# 根据索引值遍历所有的元素
for y in range(0,len(list6)):
    print(list6[y])
# 通过枚举函数查询：可以把索引值和所对应的元素都查询出来
for index,value in enumerate(list6):
    print('索引值：%s，元素：%s'%(index,value))

# ......修改.......
list6[-1]='永不言败'
print(list6)
list6[0]='we'
print(list6)

# .............常用的函数...............
list7=['亚索','盲僧','劫','瑞文','维嫩','亚索']
# count():用于统计某一个元素在容器中的出现次数
num=list7.count('亚索')
print(num)

# 2.index():用于显示元素的索引，如果列表中存在多个元素，则默认返回第一个符合第一个符合条件的元素的索引值。
num1=list7.index('盲僧')
print(num1)

# 3.reverse():将列表进行反转
list7.reverse()
print(list7)

# 4.sort():对列表中的元素进行排序，默认是按照ASCLL码排序。
list7.sort()
print(list7)

# 考点
#  5.extend():对列表进行合并
list8=[1,2.3]
list9=[4,5,6]
list8.extend(list9)
print(list8)

for x in list8:
    list9.append(x)
    print(list9)

# 6.clear():清空列表
list8.clear()
print(list8)

