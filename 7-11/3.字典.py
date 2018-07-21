# 重点内容：
# 1.添加数据：dict1[键]=值
# 2.删除数据：del dict1[键] 通过删除键，删除值
# 3.查询数据：name=dict1[键]通过找键，查询数据
# 4.修改数据：dict1[键]=修改的数据
# 3.常用函数：get()、items()、keys()、values()、pop()、setdefault()、popitem()、fromkeys()、clear()、update（）、del（）

# 字典：也是python中内置的一种容器类型，字典是可变的，可以对子典进行增删改查的操作。
# 字典有以下几个特点：
# 1.字典是以"键-值"结构来储存数据的，字典中没有索引这个概念，‘键’：相对于列表中的索引，可以通过键对一个数据进行增删改查
# 2.列表中的索引值是唯一的,键也是唯一的,都不许重复。
# 3.字典是无序的,'键-值'对的储存没有先后顺序,只需一个键对应一个值

# 声明一个空字典
dict1={}
# 声明一个非空字典
dict2={'ADC':'UZI','辅助':'Ming','打野':'MLXG','中单':'xiaohu','上单':'LetMe'}
# 字典的另一种声明方式
dict55=dict(name='张三',age=20)
print(dict55)

# 计算机中，True=1  与 Flase=0  True与1、Flase与0不能同时作为键存在，如果同时存在，键会产生冲突。列表和字典不能当做键，元组可以当做键：通常情况下，键是不可以变的。但是列表是可变的。所以列表不能当做键，但是元组不可变所以元组可以当做键。
dict3={1:'1',True:'true',(1,2,3):'(1,2,3)'}
print(dict3)

# .......................添加数据...............
# 添加数据的时候，要制定一个键，并且要给该键附一个值。
dict2['替补']='karse'
print(dict2)

# .......................查询数据,......................
name=dict2['ADC']
print(name)
name1=dict2['辅助']
print(name1)

# .......................常用的函数................
dict4={'name':"张三",'age':20,'sex':'男'}

# 1.get():根据键获取对应的值，如果字典中不存在这个键，则默认采用后面的默认值。如果存在该键，则直接采取字典中的值。如果不存在，结果返回为none。
# get()函数：第一个函数：键， 第二个函数：默认值
res=dict4.get('name','李四')
print('.....',res)
res1=dict4.get('height','170')
print(res1)

#2.items:将字典中的每一个键值对都设置成元组的形式，并且储存在列表中
res3=dict4.items()
print(res3)

# 第一种便利字典的方式
# for key,value in dict4.items():
#     print(key,value)

# for tuple_test in dict4.items():
#     print(tuple_test[0],tuple[1])

# for key,value in enumerate(dict4):
#     print(key,value)
#
# for test in enumerate(dict4):
#     print(test)

# 3. keys():取出字典中所有的键，并存放在列表中
res3=dict4.keys()
print(res3)

# 4. values:取出字典中所有的值并存放在列表中。
res4=dict4.values()
print(res4)

# 5. pop():根据键删除字典中的值，返回的结果是删除的这个键对应的值
res5=dict4.pop('sex')
print(res5)

# 可能会考 6.setdefault():根据键获取对应的值，如果字典中不存在这个键，则采用后面默认得值，并且将该建制地加入到原始字典中。如果存在该键，则直接获取字典中的值。
dict5={'name':'麻子','age':21,'sex':'女'}
res6=dict5.setdefault('name','王二')
print(res6)
res7=dict5.setdefault('height',180)
print(res7)
print(dict5)

# 7. popitem:随即返回并删除字典中的一对键值对（一般默认删词末尾的键值对），返回值是一个被删除的键值对组成的元组。
res8=dict5.popitem()
print(res8)
print(dict5)

# 8. fromkeys():生成一个字典，第一个参数是键，第二个参数是值，如果第一个参数填写的是可迭代对象，则会将该对象中的每一个元素当键，并且对应的值都是第二个参数。
dict6=dict.fromkeys('12',[1 ,2])
print('00',dict6)
dict7=dict.fromkeys('1','hahaha')
print(dict7)

# 9. update():用于将一个字典添加到另一个字典中。
dict8={'射手':'iboy','辅助':'meiko'}
dict9={'打野':'7酱','中单':'scount','上单':'Ray'}
dict8.update(dict9)
print(dict8)

# 10.判断一个键是否在字典中
if '射手' in dict8:
    print('存在射手这个键')

# 11.clear():清空所有键值对
# dict8.clear()
# print(dict8)

# 12. del():根据键删除字典中的值
dict10={'name':'张三'}
del dict10['name']
print(dict10)

