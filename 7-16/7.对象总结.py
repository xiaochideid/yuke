class People(object):
    # 类属性
    name =  '道德经'
    age = ''
    def __init__(self, fond=''):
        # 对象属性
        self.fond = fond
    # 对象方法 self指的是调用的对象本身
    def say(self):
        print('Hello')

p1 = People()
p1.fond = '学习'
print(People.name)
print(p1.name)
print(p1.fond)
# 对象属性不能通过类名+属性的方式来调用 只能通过对象来调用
# 类属性可以通过类名+属性的方式来调用 也可以通过对象来调用
# print(People.fond)
p1.say()
# 对象方法可以通过对象 + 方法名 这种形式类调用
# 也可以通过类名 + 方法名，然后将对象当成参数传入方法中这种形式来调用
People.say(p1)