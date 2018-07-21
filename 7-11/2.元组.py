#重点内容：
# 1.查询数据：【索引值、切片、遍历、枚举】
# 2.二级元素修改：【通过索引值进行赋值】
# 3.常用函数：【count（）、index（）】

# 元组：和列表一样，是一个容器类型的数据，元组只能在创建的时候添加数据，创建完成之后只能查询数据，但是元组的一级元素不能够被修改和删除，二级元素可以修改，一般在创建元组的时间，在最后一个元素的后面要加上逗号.

# 创建一个元组
tuple1=(20,9.88,'亚洲捆绑',True,)
# ......................查询数据..............
a=tuple1[0]
print(a)
b=tuple1[1]
print(b)
# 切片查询，返回的是一个元组
# 列表切片查询，返回时一个列表
c=tuple1[0:3]
print(c)
# 通过索引进行遍历
for x in  range(0,len(tuple1)):
    print(tuple1[x])
# 直接遍历里面的数据
for y in tuple1:
    print(y)
#  通过枚举
for index,value in enumerate(tuple1):
    print(index,value)

# ...............修改数据(仅能修改二级元素)..............
# [(40,50)]二级元素 二级元素可以修改
tuple2=(20,30,'meikou',[(40,50)],'hahaha')
res=tuple2[3][0]
print(res)
tuple2[3][0]=(60,70)
print(tuple2)

 # ......................常用函数...............
# count():用于统计元素出现次数
tuple3=(20,30,30,True,'hahaha')
res=tuple3.count(20)
print(res)
# index():用于返回元素的索引值
res=tuple3.index('hahaha')
print(res)
