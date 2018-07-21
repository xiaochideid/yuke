# 输入两个人的信息，对比两个人是否符合对方要求
# 1.输入男生年龄、身高、体重、收入
# 2.输入女生年龄、身高、体重、收入
# 3.设定男生要求和女生要求
  # 例如：男生要求:
  # 年龄大于20
  # 小于28
  # 身高大于160
  # 小于175
  # 体重大于40
  # 小于60
  # 收入大于2000
  # 小于5000
# 4.对比女生是否符合男生要求
# 5.对比男生是否否和女生要求
# 6.如果男女双方均符合对方要求，则配对成功！

# 3.男女配对练习
man_age=int(input('请输入男生的年龄：'))
mam_height=int(input('请输入男生的身高：'))
man_weight=int(input('请输入男生的体重(KG)：'))
man_incom=int(input('请输入男生的收入：'))

woman_age=int(input('请输入女生的年龄：'))
womam_height=int(input('请输入女生的身高：'))
woman_weight=int(input('请输入女生的体重(KG)：'))
woman_income=int(input('请输入女生的收入：'))

if (20<woman_age<30) and (160<womam_height<170) and (50<woman_weight<65) and (2000<woman_income<=3000):
# 在女生符合男生要求的前提下，判断男生是否符合女生的要求
   if(20<=man_age<=25)and (170<=mam_height<=180) and (70<=man_weight<=80) and (man_incom>=10000):
    print('男女配对成功！')
   else:
       print('男生不符合女生的要求！')
else:
    print('女生不符合男生的要求！')






# name='小曹'
# age=10
# height=174
# weight=59
# income=4000
#
# name1='小池'
# age1=23
# height1=176
# weight1=80
# income1=9000
# print('男生要求：')
# if age<20 or age >28:
#     print('女生年龄不符合要求')
#     exit()
# if height <160 or height>175:
#     print('女生身高不符合要求')
#     exit()
# if weight <40 or weight>60 :
#     print('女生体重不符合要求')
#     exit()
# if income <2000 or income>5000:
#     print('女生收入不符合要求')
#     exit()
# print('女生符合要求')
# print('女生要求：')
# if age<20 or age >28:
#     print('男生年龄不符合要求')
#     exit()
# if height <160 or height>175:
#     print('男生身高不符合要求')
#     exit()
# if weight <40 or weight>60 :
#     print('男生体重不符合要求')
#     exit()
# if income <2000 or income>5000:
#     print('男生收入不符合要求')
#     exit()
# print('男生符合要求')
# print('男女双方可以见面')