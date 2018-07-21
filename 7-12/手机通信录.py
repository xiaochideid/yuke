"""
座右铭:将来的你一定会感激现在拼命的自己
@project:预科
@author:Mr.chi
@file:手机通信录.PY
@ide:PyCharm
@time:2018-07-20 10:45:51
"""
## 练习一：模拟手机通讯录的搜索过程(列表和字典)
list_student=['郝超杰','李威','吕朝朝','张广师','李宇恒','池永伟','黄保安','陈鹏','余江帆','曹森','郑慧诏','郭克松','高翔','杨建宇','孟新珂','司金辉','张梦冉','王坤峰','蔡飞','樊俊','张稼瑞','吴亚涛','葛成云','王鹏基','樊俊峰','张崇雷','陈泽坤','王震宇','曾一飞','凌晨洋','郑雪鹏','李鑫一','晋吉祥','王晓茹','陶林','范雪婷','岳银龙','王继涛','张力方','牛铭瑞','马深凌','楚少杰','刘家豪','潜伏期']
# # name_dict={}
# for  name in list_student:
#     fist_char = name[0]
#     if fist_char in name_dict.keys():
#         list1 = name_dict[fist_char]
#         list1.append(name)
#
#     else:
#         name_dict[fist_char] = [name]
# while True:
#     s = input('请输入要查找的联系人姓氏：')
#     if s in name_dict.keys():
#         list1 = name_dict[s]
#         for index, name in enumerate(list1):
#             print('序号：%s，姓名：%s' % (index+1, name))
#     else:
#         print('没有找到联系人')

# # 2.
# # 声明一个空字典
student_dict={}
# 遍历所有联系人,取去姓氏
for student in list_student:
    # 从每个人的名字当中，取出名字的姓氏，联系人的分类就是以姓氏为键
    first_char=student[0]
    # 判断字典中是否已经存在first_char这个键
    if first_char in student_dict:
    # 如果有这个件，通过键取出联系人列表
        result_list=student_dict[first_char]
        result_list.append(student)
    else:
        # 如果没有这个键
        # 创建这个键，并且给这个键配置一个联系人列表
        result_list=[student]
        student_dict[first_char]=result_list
while True:
    print('''
    1-查询
    2-退出
    ''')
    select_number=int(input('请选择操作序号：'))
    while select_number!=1 and select_number!=2:
        select_number=int(input('请重新选择操作序号：'))
    if select_number==1:
        select_char=input('请输入要查询的联系人的姓氏：')
        if select_char in student_dict:
            # 如果在，则已输入姓氏为建取出对应的联系人列表，然后遍历联系人列表
            stu_list=student_dict[select_char]
            for index,result in enumerate(stu_list):
                print(index+1,'_',result)
        #         如果不在，则提示没有联系人信息
        print('没有对应的联系人信息！')

    else:
        break