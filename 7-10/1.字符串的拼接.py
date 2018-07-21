# 重点内容：
# 1.占位符（%d、%f、%s）
# 2,连接符（+）：只能用于连接字符串时使用
# 3.拼接：（format）:拼接顺序注意，前后一致

# 1.字符串拼接：就是将不完整的字符串或者变量拼接成完整的字符串内容
# 第一种：使用占位符拼接字符串
# %d:整数类型的占位符
age=20
score=100
result='小明的年级是%d，成绩是%d' %(age,score)
print(result)

people1=100
people2=200
result='%d,%d'%(people1,people2)
print(result)


# 拼接字符串的时候：如果只拼接一个变量，那么%后面不需要(),如果只拼接2个或2个以上变量则需要（）
height=180
result='小刚的身高是%d'%height
print(result)

# %f:小数类型的占位符，用于拼接小数类型的变量,默认情况会取去小数点后6位, .*是取小数点后几位
weight=135.5
result2='小红的体重是%f'%(weight)
result3='小红的体重是%.1f'%weight
result4='小红的体重是%.2f'%weight
print(result2)
print(result3)
print(result4)

# %s:通用占位符，可以拼接任意类型的数据(当要求值精确到小数点后几位是，要用到%f占位符)
name='张三'
age=18
height=178.5
sex='male'
result5='他的名字是%s，年龄是%s,身高是%s，性别是%s'%(name,age,height,sex)
print(result5)

#第二种;使用加号拼接,只能拼接字符串类型
result6='今'+'晚'+'吃'+'鸡'+'吗'
print(result6)

result11=1+2+3
print(result11)

# 第三种方式：使用.format()拼接.
# 使用.format()函数对字符串进行拼接的时候，小括号中填写的是要拼接的变量，{}中设置的是拼接变量的顺序，顺序的编号默认从0开始
name='小白'
age=20
sex='famle'
weight=130.5
result7='她的姓名是{0}，年龄是{1}，性别是{2}，体重是{3}'.format(name,age,sex,weight)
print(result7)

