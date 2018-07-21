phone_info = [{'name':'vivox9', 'price':'1200', 'count':'30'},{'name':'iphone6', 'price':'2000', 'count':'55'},{'name':'iphone6s', 'price':'2200', 'count':'120'},{'name':'iphone7', 'price':'4000', 'count':'80'},{'name':'iphone7s','price':'4200', 'count':'90'},{'name':'iphone8', 'price':'5200', 'count':'70'}]
# while True:
#     print('''欢迎使用手机销售管理系统
#     1-查看所有手机品牌
#     2-更该产品库信息
#     3-移除产品库存信息
#     4-退出程序''')
#     for x in range(0, len(phone_info)):
#         phone = phone_info[x]
#         name = phone['name']
#     select_number=int(input('请选择您要操作的序号:'))
#     while select_number not in range(1,5):
#        select_number = int(input('序号输入错误，请重新输入:'))
#     if select_number == 1:
#             print("""分支选项：
#             1-选择产品序号查看详情
#             2-返回
#             """)
def query_phone(type):
    for x in range(0,len(phone_info)):
        phone = phone_info[x]
        name = phone['name']
        if type==1:
            price=phone['price']
            count=phone['count']
            print('序号：%s  产品名称：%s  产品价格：%s  产品库存：%s'%(name,price,count))
        else:
            print('序号：%s , 产品名称：%s'%(x+1,name))
def buy_phone():
    if len(phone_info)<=0:
        print('当前无产品信息！')
        return
    print('1.选择序号查看手机详情：')
    print('2.返回')
    num = int(input('请选择您的操作：'))
    while num not in  range(1,3):
        num= int(input('选项有误，请重选：'))
    if num==1:
        index=int(input('请输入查看的产品序号：'))
        while index not in range(0,len(phone_info)):
            index = int(input('序号有误，请重选：'))
            # 根据index的值，取出小字典
        phone = phone_info[index]
        # 输出产品序号、名称、价格、库存
        print('序号：%s  产品名称：%s  产品价格：%s  产品库存：%s' % (index, phone['name'], phone['price'], phone['count']))
        # 是否购买
        print('1.购买')
        print('2.返回')
        num = int(input('请选择：'))
        while num not in range(1, 3):
            num = int(input('选择错误，请重选：'))
        if num == 1:
            count = phone['count']
            count = count - 1
            if count == 0:
                # 手机卖完了
                print('%s 已售罄，请及时补货！' % phone['name'])
                phone_info.remove(phone)

            else:
                # 更改库存量
                phone['count'] = count
                return
    else:
        return

    # 更改产品信息
def update_phone():
    print('1.添加新产品')
    print('2.修改原有产品')
    print('3.返回')
    num = int(input('请选择您的操作：'))
    while num not in range(1, 4):
        num = int(input('选项错误，请重选'))
    if num == 1:
            # 包括产品名称、价格、库存
        name = input('请输入添加的产品名称：')
        price = input('请输入添加的产品价格：')
            # 转换为数字
        count = int(input('请输入添加的产品库存量：'))
        while count <= 0:
            count = int(input('库存量不能小于1，请重新输入：'))
            # 将产品信息组装为一个小字典
        phone = {'name': name, 'price': price, 'count': count}
            # 将小字典添加到大列表中
        phone_info.append(phone)
    elif num == 2:
        if len(phone_info) <= 0:
            print('当前无商品信息！')
            return
            # 查询手机详细信息
        query_phone(1)
        index = int(input('请输入要修改的产品序号：'))
        while index not in range(0, len(phone_info)):
            index = int(input('序号有误，请重选：'))
        # 根据index取出手机信息字典
        phone = phone_info[index]
        # 取出原来的名称
        old_name = phone['name']
        phone['name'] = input('请输入修改后的名称(%s)：' % old_name)
        phone['price'] = input('请输入修改后的价格(%s)：' % phone['price'])
        count = int(input('请输入修改后的库存量(%s)：' % phone['count']))
        # 库存量不能为0
        while count <= 0:
            count = int(input('库存不能小于1，请重新输入：'))
        phone['count'] = count
        print('修改成功!')
    else:
        # 结束函数执行
        return


while True:
    print('''欢迎使用手机销售管理系统
         1-查看所有手机品牌
         2-更该产品库信息
         3-移除产品库存信息
         4-退出程序''')
    num=int(input('选择您的操作：'))
    while num not in range(1,5):
        num = int(input('选择错误，请重新选择：'))
    if num==1:
        query_phone(2)
        buy_phone()
    elif num == 2:
        update_phone()
    elif num == 3:
        print('移除产品信息')
    else:
        break