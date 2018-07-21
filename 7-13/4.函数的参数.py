# zhang
# 1.必备参数:要用形参和实参数量上保持一致
def sum (a,b):
    c=a+b
    print(c)
sum(1,2)

# 2.命名关键字参数：通过定义关键字来获取实参的值，与形参的顺序无关
def show(name,age):
    print('姓名是：%s_年龄是：%s'%(name,age))
show(age=20,name='张三')

# 3.默认参数
# 一般可用于用户账号密码登录的函数，或者是数据库连接的函数。
def show1(name='MLXG',password='123456'):
    print('账号是：%s'%name)
    print('密码是：%s'%password)
# 使用默认参数的时候，如果给形参传递了实参，则行参会接受实参的值，如果没有给这个形参传递实参，则形参会采用默认值.
show1()
show1('UZI','67810')

# 4.位置参数。形参的数量会根据实参的变化而变化。
# *args:接受N个位置参数，只能通过位置传值。并且会把未知参数转化为元组的方式。
def show2(*args):
    print(type(args))
    print(args)
show2(1)
show2(1,2)
show2(1,2,3)

def say_hello(*args):
    print('hello{0}'.format(args))
# 通过位置传值
say_hello('jack','tom')

# 5. **kwarges:关键字参数
# **kwarges:把N个关键字参数，转化为字典的方式
def show3(**kwargs):
    print(type(kwargs))
    print(kwargs)
show3(name='zhang',age=8,sex='male')

def fun_b(**kwargs):
    print(kwargs)
# 通过关键字传值
fun_b(a=1,b=2)

# 写一个函数把以上所有参数全部添加
def show4(name,*args,age=20,**kwargs):
    print(name)
    print(args)
    print(age)
    print(kwargs)
show4(10,20,'zhang',age=34,sex='male',father='马云')

# name：必备参数   *args:位置参数  age:默认参数  **kwargs:关键字参数

# def show5(name,age=20,*args,**kwargs):
#     print('...',name)
#     print('...',args)
#     print('---',age)
#     print('---',kwargs)
# show5(10,20,'zhang',34,sex='male',father='马云')