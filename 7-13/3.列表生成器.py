# zhang
# 通过列表生成式：一次将所有的值计算出来存放到内存当中，这样就会占用很大的内存，导致程序卡顿，另外但是由于内存有限。列表的容器也是有限的，如果一个列表数据十分庞大，但是我们只需要访问前面几个元素，那么就会导致后面接大多数元素占用内存被白白浪费了；
# 列表生成器：并不会一次性将所有的计算结果存放在内存中，而是将使用某一些值的时候，才会去动态计算并返回，而没有使用得值不会计算。

# 在使用next（）方法从列表生成器中取值时，如果元素被取完之后还接着去会报错StopIteratiion
fast_list=(x*x for x in range(0,2))
print(fast_list)
print(next(fast_list))
print(next(fast_list))
# print(next(fast_list))

# 警告:不要运行
# fast_list=[x*x for x in range(0,100000000)]
# print(fast_list)
# fast_list=(x*x for x in range(0,100000000))
# print(fast_list)
