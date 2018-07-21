# 重点内容：
# 1.if.....if....
# 2.if......else.....
# 3.if......elif......

# "==":比较运算符，用与比较左右两边的值是否相等，结果返回True和False
# python中对于代码的缩进要求十分严格，因为python是通过缩进来判断代码之间的包含关系。如果某行代码的缩进比前面代码的缩进多，说明该行是被包含关系。如果代码之间缩进一致，说明是同等级关系
name='张三'
if name=="李四":
    print('姓名是李四')
if name == "张三":
    print('姓名是张三')
if name=="王二":
    print('姓名是王二')

age=20
if age==20:
    print('年龄是20')
else:
    print('年龄不是20')

age=21
if age==20:
    print('年龄是20')
else:
    print('年龄不是20')

animal="小狗"
if animal=="小猫":
    print('这个动物是小猫')
elif animal=="小熊":
    print('这个动物是小熊')
elif animal=="小鹿":
    print('这个动物是小鹿')
elif animal=="小狗":
    print('这个动物是小狗')
