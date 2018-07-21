# 成绩计算
# 输入一个成绩，然后进行判断。
# 要求显示的结果：
# 如果成绩在[0 60]之间   不及格
# 如果成绩在[60 70)之间   等级是D
# 如果成绩在[70 80)之间         C
# 如果成绩在[80 90)之间         B
# 如果成绩在[90 100]之间        A
# 可以使用if...else...组合(不使用elif)
# 也可以使用if...elif...组合
# 1.成绩计算
# while True:
#     # input()接受的是一个字符串，想要与整数作比较，需要int转换
#     score=input('请输入您的成绩：')
#     score=int(score)
#     if score>=0and score<60:
#         print('您的成绩不及格，请及时补考')
#     elif score>= 60 and score<70:
#         print('您的成绩是D！')
#     elif score>=70 and score<80:
#         print('您的成绩是C！')
#     elif score>=80 and score<90:
#         print('您的成绩是B！')
#     elif score>=90 and score<=100:
#         print('您的成绩是A！')

score=80
if score>=0 and score<60:
    print('成绩不及格')
elif score>=60 and score<70:
    print('成绩等级是D')
elif score>=70 and score<80:
    print('成绩等级是C')
elif score>=80 and score<90:
    print('成绩等级是B')
elif score >= 90 and score <= 100:
    print('成绩等级是A')

score=50
if score>=0 and score<60:
    print('成绩不及格')
    if score>=60 and score<70:
      print('成绩等级是D')
    if score>=70 and score<80:
      print('成绩等级是C')
    if score>=80 and score<90:
      print('成绩等级是B')
else :
    print('成绩等级是A')