class People(object):
    # 类属性
    count = 0
    size = 0
    def __init__(self,name='',age=''):
        # 对象属性
        self.name = name
        self.age = age
    # 对象方法
    def say(self):
        print('hai')

    # class 类 method 方法
    @classmethod
        # cls  class
    def classFun(cls):
        print('Hello ,我是类方法')

    # static 静态 method方法
    @staticmethod
        # 不需要指定self或者cls来调用
    def method():
        print('我是静态方法')

People.classFun()
People.method()
p1  = People()
p1.classFun()
p1.method()
p1.say()
People.say(p1)
# 总结:任何一种类型的方法 都可以用类或者对象来调用
# 什么时候使用对象方法? 什么使用使用类方法和静态方法?
# 1.在绝大部分情况下我们的方法都会声明成 对象方法
# 2.如果我们希望用类来处理这个方法，或者不希望某一个属性值不因为对象
#   而改变的时候 就可以用类方法
# 3.静态方法的使用绝大部分都可以用实例方法或者类方法来替代

# 统计：某一个类的对象 一共被创建了多少个  想要知道有多少个对象
class FoodTemplate(object):
    # 一旦对象被创建会自动调用这个方法
    # 类属性
    count = 0
    def __init__(self):
        print('创建了一次')
        FoodTemplate.count += 1
    pass
    @classmethod
    def myCount(cls):
        print('一共被创建了{}个'.format(FoodTemplate.count))
yueBing = FoodTemplate()
manTou = FoodTemplate()

FoodTemplate.myCount()