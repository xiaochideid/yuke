# 重点内容：
# 1.去重功能（元素不可重复）
# 2.交集：intersection（&） 差集：difference（-） 并集：Union(|) 子集：issubset()  父集：issuperset()  交集：isdisjoint()
# 3.常用函数：add()、remove()、discard()、pop()、updata()、clear()

# 集合是一个无序的，元素不可重复的数据组合 它的标识符号{}
# 它有两个作用：
# 1.去重：把一个容器变成集合,可以实现去重的功能。
# 2.关系测试:测试两组数据之间的交集 差集 并集等等。
# .....................去重.................
list1=[1,2,3,4,5,2,2,1,1]
set_1=set(list1)
print(type(set_1))
print(set_1)

tupli1=(5,6,7,8,9,9,8)
set_2=set(tupli1)
print(type(set_2))
print(set_2)

string='你好，美女'
set_3=set(string)
print(type(set_3))
print(set_3)

# .....................常用函数....................
#定义一个空的set集合的时候，一定要注意不要和声明空字典搞混了
list1=[]
tuple1=()
my_dict={}
myset=set()
print(myset)
# 声明一个非空的set集合
my_set={1,2,3}
# 1.add():往集合里面添加数据，括号中直接填写要添加的数据，如果添加重复的数据也会自动去重。
myset.add('1')
print(myset)
myset.add(2)
print(myset)
myset.add(1)
print(myset)
myset.add(4)
myset.add(5)
myset.add(6)
# 2.remove():删除集合中的元素，括号中直接要删除的元素的值，如果要删除的元素不存在会报错。
myset.remove(1)
print(myset)
# myset.remove(1)
# print(myset)
#3.discard():删除集合的元素，括号中直接要删除的元素的值，如果要删除的元素不存在也不会报错。
myset.discard(2)
print(myset)
myset.discard(2)
print(myset)
# 4.pop():随机删除集合中的元素。当集合为空时，会报错。
myset.pop()
print(myset)
# 5.update():如果添加的数据是一个数列，它会将传入数列中的每一个元素分别传入到集合当中变成集合的元素，区别于add().会将整个序列当作一个整体，添加到集合当中.
myset.update('qafaf')
print(myset)
myset.add('不好意思')
print(myset)
# 6.clear():清空集合；
myset.clear()
print(myset)



# ...................关系测试运算................
list2=[1,2,3,4,5,6]
set1=set(list2)
print(set1)
list3=[4,5,6,7,8,9]
set2=set(list3)
print(set2)

# 1.intersection():求两个集合之间的交集
res=set1.intersection(set2)
print(res)
# 2.union:求两个集合之间的并集
res2=set1.union(set2)
print(res2)
# 3.difference:第一个集合与第二个集合的差集
res3=set1.difference(set2)
print(res3)
# 4. issubset():用于判断xx集合是不是xx集合的子集,返回结果是True or Flase
res4=set1.issubset(set2)
print(res4)
# 5.issuperset():判断xx集合是不是xx集合的父集,返回结果是True or Flase
res5=set1.issuperset(set2)
print(res5)
# 6. isdisjoint():判断xx集合与xx集合是否没有交集，返回是True or Flase
res6=set1.isdisjoint(set2)
print(res6)
# ........................通过运算符的形式进行关系测试............
# &: 交集
res8=set1&set2
print(res8)

# |；并集
res9=set1| set2
print(res9)

# -：差集
res10=set1-set2
print(res10)
