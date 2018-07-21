# 重点内容：
# 1.取值：切片、倒序  count()、find()、index()、upper()、lower()、upper()、strip（）、split()、replace()、startwith()、endswith()、
# 2.字符串的添加（将字符串变换成列表进行，再讲列表转化成字符串） 修改：replace()

# 字符串也可以理解为一个容器，它也是有序的，也存在索引值。
# .........................字符串常用方法...........................
string='德玛西亚'
# 1.len()：长度
res1=len(string)
print(res1)

# 2.字符串取值
res2=string[0]
print(res2)
# 切片查询
res3=string[0:3]
print(res3)
# 倒序查询
res4=string[-1]
print(res4)
# 3.count:统计某个字符出现的次数。
res5=string.count('德')
print(res5)
# 4.find():用于查询某串字符，在匹配到合适的字符串之后，会直接返回该字符串所在位置的起始索引值。如果查询不到，会返回-1
find_str='西'
res6=string.find(find_str)
print(res6)
# 参数一：要找的字符串：参数二：从哪个位置开始找：参数三：找到那个位置（取头不取尾），如果不设置范围，则从整个字符串中找。
res7=string.find(find_str,0,1)
print(res7)
# 5.index():在匹配到合适的字符串之后，会直接返回该字符串所在位置的起始索引值。若果没有查询到合适的字符串会报错。
res8=string.index(find_str)
print(res8)
# res9=string.index(find_str,0,1)
# print(res9)
# 6.upper():将小写的英文字母全部转化为大写。
string1='abcd'
res10=string1.upper()
print(res10)
# 7.lower():将大写英文字母全部装化为小写。
string2='WQDQ'
res11=string2.lower()
print(res11)
# 8.strip(): 去除字符串首尾两端的指定字符
string3=';adda;'
res12=string3.strip(';')
print(res12)
# 9.split():根据指定字符对一个字符串进行分割，返回值是一个list列表
string4='a;d;d;f'
res13=string4.split(';')
print(res13)
# 10.replace()：以新换旧（使用新的字符替换旧的字符，第一个参数：旧的字符：第二个参数：新的字符）
string5='a;b'
res14=string5.replace(';','-')
print(res14)
# 11.startwith():判断一个字符串是否是以某一个字符串开头，返回结果：True 或 False
string6='asdd'
res15=string6.startswith('a')
print(res15)

# 12.endswith():判断一个字符串是否是以某一个字符串结尾，返回对错
res16=string6.endswith('b')
print(res16)

# ...............字符串的添加和修改...............
# 修改
string7='你好'
new_string=string7.replace('你','她')
print(new_string)

# 添加
#1. 添加字符串转化成列表
new_list=list(string7)
print(type(new_list))
print(new_list)
# 2.向列表中添加字符
new_list.insert(2,'他')
new_list.insert(3,'也')
new_list.insert(4,'好')
print(new_list)
# 3.再将列表转化成字符串
new_string1=''.join(new_list)
print(new_string1)

