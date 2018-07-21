# 重点内容：
# 1.文件的的打开模式：r、w、a、r+、w+、a+
# 2.open():打一个参数：文件名 第二个参数：文件的打开方式； 第三个参数：文件的编码格式
# 3.writable()、readable(）、tell()、name()、encoding()、seek（）、close（）

# 大象装进冰箱三个步骤：1.打开冰箱2.把大象装进去3.关闭冰箱
# 文件的读写：1.打开文件 2.读/写 3.关闭文件

# 文件打开的几种模式：
# 1.r:只读模式,如果打开的文件不存在，则会报错；如果存在。则会打开。
# 2.w:只写模式，如果要打开的文件不存在，则会自动创建。如果存在，则会自动打开，光标的文件的开头位置。会对文件进行覆盖写入。光标在文件的开头位置。
# 3.a:追加写入模式 如果打开的文件不存在，则会自动创建，如果存在，则会打开。光标在文件的开头位置。如果文件不为空，光标在文件末尾位置，不论光标位置在哪里，都会在文件的末尾位置追加字符 能写也能读
# 4.w+:写读模式  如果要打开的文件不存在，则会自动创建。如果存在，则会自动打开.使用open函数打开，会自动将文件里面的内容清空，光标在文件的开头位置，能写也能读 也是覆盖写入，但是位置会根据光标移动
# 5.r+:读写模式  如果打开的文件不存在，则会报错；如果存在。则会打开。区别于写读模式，打开文件时不会清空内容，如果光标不在末尾位置会覆盖写入，但会保留没有被覆盖的内容。不能够移动光标写入，否则会乱码，默认也是覆盖写入
# 6.a+:追加读写  如果文件不存在，则会自动创建，如果存在，则会自动打开。如果文件不为空，光标在文件末尾位置，不论光标位置在哪里，都会在文件的末尾位置追加字符,能写也能读,写入读数据会追加到原数据的最后
# 7.rb:二进制读，但是不能设置编码，因为默认就是二进制模式
# 8.rw:二进制写入，但是需要更改写入文件得编码模式
# 9.ab:二进制追加模式

# 1.创建文件操作的的句柄
# open():打一个参数：文件名 第二个参数：文件的打开方式； 第三个参数：文件的编码格式。  这几个参数之间的位置不能调换

# --------------w只写模式-----------------
f=open('ThatGirl.txt','w',encoding='utf-8')
# 1.writable():判断文件是否可写，返回的结果是True或者False
print(f.writable())
# 2.readtable():判断文件是否可读，返回的结果是True或者False
print(f.readtable())
# 3.tell():返回当前的光标的位置
# print(f.tell())
f.write('123')
print(f.tell())
# 4.name():返回当前文件名称
print(f.name)
# 5.encoding:返回当前文件的编码格式
print(f.encoding)
# 6.seek:返回到指定的光标位置
f.seek(0)
print(f.seek)
f.write('456')
# 7.close():关闭文件。因为文件写入，首先是写入计算机缓存当中，然后再写入硬盘当中。假如不对文件关闭，不对文件进行关闭，万一电脑出现问题或者重启，则会导致文件丢失或者损坏
# f.close()

# #---------------r只读模式-----------------
# f.open('test1'.txt,'r',ending='utf-8')
# print(f.tell())
# print(f.readable())
# print(f.writeable())
# # read():读文件，括号立刻填写读取字符的个数,如果不填参数默认读取整个文件。
# print(f.read())
# print(f.tell())
# f.seek(0)
# print(f.read(3))
# readline():一次只会读取一行数据
# print(f.readline())
# readlines():会读取所有行的数据，但是会将每一行的数据当成一个元素存放在列表中
# print(f.readlines())
# f.close()

# ---------------w+写读模式--------------
# f=open('test2.txt','w+',encoding='utf-8')
# print(f.seek())
# print(f.readable())
# print(f.writeable())
# f.write('123')
# print(f.tell())
# print(f.read(1))
# f.close()

# # ---------------r+读写模式----------------
# f=open('test3.txt','r+',encoding='utf-8')
# print(f.seek())
# print(f.readable())
# print(f.writeable())
# print(f.read(3))
# print(f.tell())
# f.write('aaaa')
# print(f.tell())
# f.seek(5)
# f.write('123')
# print(f.tell())
# f.close()

# ---------------a;读写模式----------------
f=open('test4.txt','a',encoding='utf-8')
print(f.seek())
print(f.readable())
print(f.writeable())
f.write('bbbb')
print(f.tell())
f.seek(5)
f.write('ccc')
f.close()

# --------------------追加读写模式----------------
f=open('test,txt','a+',encoding='utf-8')
print(f.tell())
print(f.writable())
print(f.readable())
f.seek(0)
print(f.read(5))
print(f.tell())
f.write('78877')
print(f.tell())
f.close()

# --------------------------trucate--------------------
f=open('test,txt','a+',encoding='utf-8')
print(f.tell())
f.seek(2)
# trucate:指定长度的话，就从文件的开头开始截取指定长度，其余内容删除，不指定长度的话，就从文件的开头开始截取到当前位置，其余内容删除。
f.truncate(3)
f.close()

# -------------------flush-------------------------
# 假如写入数据时文件中没有写入的数据，需要用到flush刷新一下缓冲区，直接将文件写入到本地文件中
f=open('test,txt','a+',encoding='utf-8')
f.write('123455')
f.flush()
f.close()
# 一些总结：一般文件流操作都包含缓冲机制，write方法并直接将数据写入文件，而是先写入到内存当中指定的缓冲区，Flush方法是用来刷新缓冲区的，即将缓冲区的数据立即写入到文件中，正常情况下缓冲区满是，操作系统会将缓冲数据写到文件中，至于close方法，试讲flush 方法开刷新缓冲区，在执行关闭操作。
# f.seek(0):回到原来
# f.seek(0)
#
#

# 文件在读取的模式下，是不能写入数据的,文件在写入的模式下，是不能读取数据的
# f.write('haha')
# print(f.read())

# print(f.read())
# print(f.tell())
#  f.encoding 文件的编码格式
# print(f.encoding)
# f.name:文件的名称
# print(f.name)

# f=open('ThatGirl.txt','w',encoding='utf-8')
# # print(f.read(5))
# # 'w':写入模式，写进去的数据会覆盖原有数据，把’w'改为’a'
# f.write('hello')

# f=open('ThatGirl.txt','r',encoding='utf-8')
# readline():一次只读取一行数据
# print(f.readline())
# print(f.readline())
# print(f.readline())
# readlines():会读取所有行的数据，但是会将每一行的数据当成一个元素存放在列表中
# print(f.readlines())
# f.truncate(3)
# print(f.truncate(3))

# f=open('ThatGirl.txt','w+',encoding='utf-8')
# f.write('Hello')
# print(f.read())

# f=open('ThatGirl.txt','r+',encoding='utf-8')
# print(f.read(3))
# f.write('哈哈')
#
# f=open('ThatGirl.txt','w+',encoding='utf-8')
# # f.write('world')
# # print(f.read(5))
# f.seek(4)
# f.write('hehe')

