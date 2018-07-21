import sqlite3
import  random
con = sqlite3.connect('phoneDB')
cursor = con.cursor()
cursor.execute("create table if not exists phone_info (brand text , price int  ,memory text , function text , count int)")
con.commit()

class Customer(object):
    brand = ''
    memory = ''
    price = ''
    count = ''
    function = ''
class Seller(object):
    @classmethod
    def fullMyshop(cls):
        nameList = ['华为','小米','锤子','oppo','vivo','一加','apple']
        memoryList = ['512M','1G','2G','4G','8G']
        priceList = [599 ,799,999,1299,1499,1799,1999,2199,2599,2999,3599,3999,4599,4999,5999]
        functionList =['美颜手机','双卡双待','超长续航','高清音质','超性价比','娱乐专项','时尚前沿','商务定制']

        # for x in range(20):
        #     cursor.execute('INSERT INTO phone_info (brand, price, memory, function, count) '
        #                    'VALUES ("{}","{}","{}","{}","{}")'
        #                    .format(random.choice(nameList),random.choice(priceList),random.choice(memoryList),random.choice(functionList),random.randint(0,10)))
        #     con.commit()
        for x in range(20):
            cursor.execute('INSERT INTO phone_info (brand, price, memory, function, count) '
                           'VALUES ("{}","{}","{}","{}","{}")'
                           .format(random.choice(nameList), random.choice(priceList), random.choice(memoryList),
                                   random.choice(functionList), random.randint(0, 10)))
            con.commit()
    @classmethod
    def findPhone(cls , other):
        cursor.execute('SELECT * from phone_info WHERE brand = "{}" and price <= "{}" and count > 0'.format(other.brand,other.price))
        con.commit()
        print(cursor.fetchall())

Seller.fullMyshop()
Customer.brand = '华为'
Customer.price = 2500
Seller.findPhone(Customer)