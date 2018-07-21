# 重点内容：
# 将类型一转化成类型二：命名=类型2（类型1）特殊：转化为字符串string1=''.join(list or  tuple  or  set)
# 列表：list []
# 元组：tuple   ()
# 字符串：string  {}
# 集合：set   {}
# ..................列表转化成元组 字符串 集合...............
# 列表转换成元组
list1=['a','b','c','d']
tup=tuple(list1)
print(type(tup))
print(tup)
# 列表转化成字符串
string=''.join(list1)
print(type(string))
print(string)
# 列表转化成集合
set1=set(list1)
print(type(set1),set1,sep='')
print(set1)

# ,,,,,,,,,,,,,,,,,,元组转化成列表 字符串 集合...............
# 元组转化成列表
tuple1=('q','w','e')
list2=list(tuple1)
print(type(list2))
print(list2)

# 元组转化成字符串
string1=''.join(tuple1)
print(type(string1))
print(string1)

#  元组转化成集合
set2=set(tuple1)
print(type(set2))
print(set2)


# ...............字符串转化成列表 元组 集合...............
# 字符串转化成列表
string2='qdqf'
list3=list(string2)
print(type(list3))
print(list3)

# 字符串转化成元组
tuple2=tuple(string2)
print(type(tuple2))
print(tuple2)

# 字符串转化成集合
set3=set(string2)
print(type(set3))
print(set3)

# ................集合转化成列表 元组 字符串................
# 由于集合是无序的，所以转化出来的列表元组字符串的结果也是无序的
# 声明一个非空集合
my_set={'a','d','d','e'}
# 声明一个空集合
my_set1=set()

# 集合转化为字符串
string3=''.join(my_set)
print(type(string3))
print(string3)

# 集合转化为列表
list4=list(my_set)
print(type(list4))
print(list4)

# 集合转化为元组
tuple3=tuple(my_set)
print(type(tuple3))
print(tuple3)




