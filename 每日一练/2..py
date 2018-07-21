# 将字符串"k:1|k1:2|k2:3|k3:4"处理成Python字典{k:1,k1:2,k2:3,k3:4}
string1 = "k:1|k1:2|k2:3|k3:4"
# 1.
list1 = string1.split('|')
dict1 = {}
for x in list1:
    list2 = x.split(":")
    dict1[list2[0]] = int(list2[1])
print(dict1)

# 2.
#  str2 = string1.split("|")
# print(str2)
# dict1 = {}
# for i in str2:
#     x = i.split(':')
#     dict2= dict1.setdefault(x[0],x[1])
# print(dict1)

# 3.
string1 = "k:1|k1:2|k2:3|k3:4"
list1 = string1.split("|")
string2= str(list1)

string3 = string2.spilt(':')
print(string3)

