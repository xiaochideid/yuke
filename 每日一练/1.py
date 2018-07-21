# list1=['a','a','a',1,3,5,7,9]

#第一种
# list1=['a','b','d','a','a','e','b','b','a','b']
# while list1.count('a')>0:
#     list1.remove('a')
# print(list1)
# while list1.count('b')>0:
#     list1.remove('b')
#     print(list1)

# #第二种
# list1 = [1, 2, 3, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9]
# list2=[]
# for x in range(0,len(list1)):
#      num1=list1.count(x)
#      if num1==1:
#          list2.append(x)
# print(list2)
# #
# #第三种
# lst = ['1', '2', '4', '5', '5', '5', '4', '7']
# print([x for x in lst if lst.count(x)==1])
# #第四种：
# list1=[1,2,1,2,3,4,5,6,5]
# list2=[]
# for x in list1:
#     if list1.count(x)==1:
#         list2.append(x)
#         # print(list2)
# print(list2)
# #第五种
# list1 = [1,2,3,1,1,1,1,2]
# num = list1.count(1)
# print(num)
# #指定的相同的元素全部删除
# # for i in range(0,num):
# #     list1.remove(1)
# # print(list1)
# # #保留一个不全删除
# for i in range(0,num-1):
#     list1.remove(1)
# print(list1)

 # 1.使用4,9,2,7四个数字，可以使用+ - * /，每个数字使用一次，使表达式的结果为24。请问表达式是什么    2*4+(9+7) 、（7+9-4）*2
# 2.尽可能多的写出列表去重方案，另写出去重的同时保持顺序不变的方案。


# list1=['a','b','d','a','a','e','b','b','a','b']
# while list1.count('a')>0:
#     list1.remove('a')
# print(list1)
# while list1.count('b')>0:
#     list1.remove('b')
#     print(list1)


# list1 = [1, 2, 3, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9]
# list2=[]
# for x in range(0,len(list1)):
#      num1=list1.count(x)
#      if num1==1:
#          list2.append(x)
# print(list2)


list1 = [1, 2, 5, 23, 23, 24, 4, 5, 6, 6, 6, 7, 8, 9]
# 1.
# list2=set(list1)
# list3=list(list2)
# list3.sort()
# print(list2)

# 2.
# for x in  list1:
#   while list1.count(x)>1:
#         list1.remove(x)
#   print(list1)




