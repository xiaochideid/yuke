list = [1,2,3,4,5,6,7,8]
# IndexError: list index out of range
# print(list[14])
dic = {}
# 如果dic有name属性 则修改这个属性的值
# 如果没有name属性 则添加name属性
dic['name'] = '张三'
# KeyError: 'age'
# print(dic['age'])

# 将有可能引起错误的代码放进try里面
# 如果出现错误
# 代码会根据错误类型  进入到指定的except
# 这样做的：
# 代码不会因为错误而中断执行好处
try :
    print('-----------------------')
    # print(list[14])
    print(dic['age'])
except IndexError as e :
    print('捕获了一个索引错误{}'.format(e))
except KeyError as e :
    print('捕获了一个关键字错误{}'.format(e))
print('hello world')

try :
    print(list[21])
# Exception 和 IndexError , KeyError ...
# 为父与子关系
except Exception as e :
    print('捕获了一个错误{}'.format(e))

# try :
#     pass
# except :
#     pass
# else :
#     pass
# finally:
#     pass


try:
    print('这是一个标准格式')
    print(dic['data'])
except IndexError as e:
    print('上一行代码出现了索引错误{}'.format(e))
except KeyError as e:
    print('上一行代码出现了关键字错误{}'.format(e))
# 如果没有出现任何错误 即执行else代码块
else :
    print('目前代码感觉良好')

finally:
    print('代码结束')



age = input('请输入你的年龄')
age = int(age)
if age <  0 :
    print('年龄不对')
    # raise  升起 ； 在此指抛出错误
    # 手动抛出异常
    raise Exception('FBI warning')
