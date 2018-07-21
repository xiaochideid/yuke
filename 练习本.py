import random
random_number=random.randint(0,10)
error_count=0
while True:
    input_number=int(input('请输入要猜的数（0-10）：'))
    while input_number<0 or input_number>10:
        input_number=int(input('您输入的数字不在范围内，请重新输入：'))
    if input_number>random_number:
        print('数字大了！')
        error_count += 1
    if input_number< random_number:
        print('数字小了！')
        error_count += 1
    if input_number==random_number:
        print('''猜对了！
        1-继续猜 
        2-退出''')
        error_count=0
        select_number=int(input('请选择你的数字：'))
        while select_number < 1 or select_number > 2:
            select_number = int(input('您选择的操作序号错误，请重新选择：'))
        if select_number == 1:
            random_number = random.randint(0, 10)
        else:
            break
    if error_count >= 3:
            print('错误次数以达到三次，不给你机会了！')
            break
