# 首先以读的方式打开ThatGirl.txt这个文件
f=open('ThatGirl.txt','r',encoding='utf-8')
#以 'w'模式打开文件，如果当前目录不存在该文件，则自动创建
f_new=open('ThatGirl.bak','w',encoding='utf-8')
for line in f:
    if '一切都是我的错'in line:
        line=line.replace('一切都是我的错','沉默不是代表我的')
        f_new.write(line)
    else:
        f_new.write(line)
f.close()
f_new.close()