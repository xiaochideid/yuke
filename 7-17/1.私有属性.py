# list = list()
# dic = dict()

# 对象属性中，凡是带下划线的_，都是不希望外部使用(道德上)
# 但是并不是说我们完全不能使用
# 如果加的单下划线_ ,可以通过 p1._name = 'xiaozhang'这种方式使用
# 如果加的是双下划线，可以通过p1._People__name这种当时使用
class People(object):
    def __init__(self , name='' ,sex='' ,age='16' ,fond='学习'):
        self.name = name
        self._sex = sex
        self.__age = age
        self.__fond = fond
    # get set方法
    @property
    def fond(self):
        print('fond被get了')
        return self.__fond
    fond.setter
    def fond(self , fond):
        print('fond被set了')
        self.__fond = fond
p = People()
p.name = '张三'
print(p.name)
p._sex = '男'
# __age
print(p._People__age)

# set
str = '123123123123'
# get
str1 = str

# p.fond = '开车'

print(p.fond('开车'))

# 如果有这个属性 则修改属性值
# 如果没有这个属性 则添加
p.girlFriend = '小美'
print(p.girlFriend)
# p.__age = '17'
# print(p.__age)

# dic = {}
# dic['name'] = 'zhangsan'
