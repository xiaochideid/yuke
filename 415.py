member_list=[]
while True:
    print('''欢迎使用python-13期学员信息管理系统
    1-添加学员姓名
    2-修改学员姓名
    3-查询学员姓名
    4-删除学员姓名
    0-退出''')
    select_number=int(input('请选择您要操作的序号：'))
    while select_number<0 or select_number>4:
        select_number=int(input('序号输入错误，请重新输入:'))
    # 如果用户选择序号1.说明用户要添加学员姓名
    if select_number==1:
        name=input('请输入要添加的学员姓名：')
        member_list.append(name)
        print('学员信息添加成功')
    #如果用户选择序号2，说明用户想要修改学员姓名
    if select_number==2:
        # 判断列表中是否有学员信息
        if len(member_list):
        # 让用户选择学员信息，需要将列表中的学员信息遍历出来
        # 用户选择的序号从1开始，对应的索引要加1
            for x in range (0,len(member_list)):
                print(x+1,member_list[x])
            student_number=int(input('请输入你要修改的学员序号'))
            while select_number<1 or student_number>len(member_list):
                student_number=int(input('序号输入错误，请重新输入你要修改的学员序号：'))
            new_name=input('请输入修改的姓名：')
            # 由于用户选择的序号是从1开始的，所以更改时要-1
            member_list[student_number-1]=new_name
            print('学员信息修改成功！')
        else:
            print('学员信息为空，无法修改！')
    # 序号等于3的时候说明用户想要查询学员信息
    if select_number==3:
        # 首先判断列表中是否有学员信息
        if len(member_list):
            print('''
            1-输入序号查询
            2-查询所有学员''')
            select_number=int(input('请输入你要操作的序号：'))
            while select_number!=1 and select_number !=2 :
                select_number = int(input('序号输入错误，请重新输入:'))
            if select_number==1:
                student_number=int(input('请输入要查询的学员的序号'))
                while student_number<1 or student_number>len(member_list):
                    student_number=int('序号输入错误，请重新输入:')
                name=member_list[student_number-1]
                print('查询到的学员姓名是：%s'%name)
            if select_number ==2:
                for x in range(0, len(member_list)):
                    print(x + 1, member_list[x])
        else:
            print('学员信息为空，无法查询！')
    # 用户选择序号4，说明用户想要删除学员
    if select_number==4:
        print('''
        1-输入序号删除
        2-输入学员姓名删除
        3-删除所有学员
        ''')
        for x in range(0, len(member_list)):
            print(x + 1, member_list[x])
        select_num=int(input('请输入要操作的序号：'))
        while select_num !=1and select_num!=2 and       select_num!=3:
            select_num=int(input('请重新输入序号'))
        if select_num==1:
            select=int(input('请输入要删除的学员的序号：'))
            while select<1 or select>len(member_list):
                select=int(input('编号不存在，请重新输入'))
            member_list.pop(select-1)
            print('删除学员成功！')
        if select_num == 2:
            name=input('请输入要删除的学员的名称：')
            while name not in member_list:
                name=input('请重新输入要删除的学员的名称：')
            member_list.remove(name)
            print('学员信息删除成功！')
        if select_num==3:
            while len(member_list):
                del member_list[0]
            print('学员信息删除成功')
        else:
          print('学员信息为空，无法删除！')
    if select_number==0:
        break