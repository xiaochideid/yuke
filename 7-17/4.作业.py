class People(object):
    def __init__(self,name='',age='',sex='',yaowei='',height=''):
        self.name = name
        self.age = age
        self.sex = sex
        self.yaowei = yaowei
        self.height = height
        # 4
    def sexIsFit(self , other):
        if self.sex == True and self.sex == other.sex :
            print('我是男的，但是你也是一个男的')
            # 在此 用False代表相亲失败
            return False
        if self.sex == False and self.sex == other.sex :
            print('我是女的，但是你也是女的')
            return  False
        # 6
    def ageIsFit(self ,other):
        if self.sex == False and self.age > other.age :
            print('小弟弟，你太小')
            return False
        if self.sex == True and self.age < other.age:
            print('大姐姐，你太大')
            return False

class Man(People):
    def __init__(self , salary='',house_area='',house_value=''):
        super(Man,self).__init__(name='',sex='',age='',height='',yaowei='')
        self.salary = salary
        self.house_area = house_area
        self.house_value = house_value

        # 2
    def makeFriendWithGirl(self ,other):
        # 3
        result =  super(Man,self).sexIsFit(other)
        if result == False :
            return

        # 5
        result = super(Man,self).ageIsFit(other)
        if result == False :
            return
        # 7
        if other.height < 165 :
            print('我喜欢个子高的，你很好，但是我们不合适')
            return
        # 8
        if other.yaowei > self.yaowei :
            print('我喜欢稍微瘦一点的')
            return
        # 9
        if other.readCount < 100 :
            print('好看的皮囊和有趣的灵魂我都喜欢')
            return
        # 10
        print('你是我的女神')


class Woman(People):
    def __init__(self , readCount =''):
        super(Woman,self).__init__(name='',sex='',age='',height='',yaowei='')
        self.readCount = readCount

jack = Man()
jack.sex = True
jack.age = 21
jack.height = 176
jack.yaowei = 45
jack.salary = 20000000
jack.house_area = 130
jack.house_value = 2000000

rose = Woman()
rose.sex = False
rose.age = 20
rose.height = 170
rose.readCount = 919
rose.yaowei = 250


# 1
jack.makeFriendWithGirl(rose)