#将下列字符串中的所有网址提取出来进行输出。

# coding='utf-8'
# f=open('字符串方法练习.txt','r')
# f_new=open('字符串方法练习.bak','w')
# f=open('字符串方法练习.txt','r',encoding='utf-8')
# f_new=open('字符串方法练习.bak','w+',encoding='utf-8')
# string=str(f.readlines())
#
# find_str='http'
# res1=string.find(find_str)
# find_str1='" title'
# res2=string.find(find_str1)
# print(string[res1:res2])
#
#
# string1=string[:res1-4]+string[res2+8:]
# res3=string1.find(find_str)
# res4=string1.find(find_str1)
# print(string1[res3:res4])


#
# f=open('字符串方法练习.txt','r',encoding='utf-8')
# f_new=open('字符串方法练习.bak','w',encoding='utf-8')
# lis=[]
# for lise in f:
#   res1=lise.split('"')
# for x in res1:
#   if x[0]=='h':
#     lis.append(x)
# print(lis)
# string=''.join(lis)
# f_new.write(string)
# f.close()

# f.close()
# f_new.close()

# 2.网址提取
# coding:utf-8
# string='<div class="item-list ni-list"><ul><li  class="first"><a href="http://www.tepintehui.com/detail/57185?ce" title="明星同款| 钟基欧巴穿的小脏鞋5折辣!" ><span>明星同款| 钟基欧巴穿的小脏鞋5折辣!</span></a></li><li><a href="http://www.tepintehui.com/detail/56847?ce" title="装逼| 你们见过凌晨四点钟的洛杉矶吗?" ><span>装逼| 你们见过凌晨四点钟的洛杉矶吗?</span></a></li><li  ><a href="http://www.tepintehui.com/detail/57127?ce" title="反人类| 世界上最干净的纸竟然是黄色的!" ><span>反人类| 世界上最干净的纸竟然是黄色的</span></a></li><li><a href="http://www.tepintehui.com/detail/57120?ce" title="科普| 吃了避孕药之后怀的孩子能要吗?" ><span>科普| 吃了避孕药之后怀的孩子能要吗?</span></a></li><li><a href="http://www.tepintehui.com/detail/57125?ce" title="真假| 9年义务升为12年制,是要取消高考吗" ><span>真假| 9年义务升为12年制,是要取消高考吗</span></a></li><li><a href="http://www.tepintehui.com/detail/57124?ce" title="土豪| 揭秘迪士尼见不得光的33号俱乐部" ><span>土豪| 揭秘迪士尼见不得光的33号俱乐部</span></a></li><li  ><a href="http://www.tepintehui.com/detail/41008?ce" title="吐槽| 男人单身太久会没感觉?" ><span>吐槽| 男人单身太久会没感觉?</span></a></li><li  ><a href="http://www.tepintehui.com/detail/23488?ce" title="冷知识| 为什么镜子是左右颠倒不是上下呢" ><span>冷知识| 为什么镜子是左右颠倒不是上下呢</span></a></li><li  ><a href="http://www.tepintehui.com/detail/37213?ce" title="新玩法| 这年头情侣之间种草莓已经out了!" ><span>新玩法| 这年头情侣之间种草莓已经out了!</span></a></li><li  ><a href="http://www.tepintehui.com/detail/11411?ce" title="四壁| 老美说凤姐把范冰冰秒成渣,你怎么看" ><span>四壁| 老美说凤姐把范冰冰秒成渣,你怎么看</span></a></li><li  ><a href="http://www.tepintehui.com/detail/37456?ce" title="凭什么| 个人挖墓是盗墓,国家挖是考古?" ><span>凭什么| 个人挖墓是盗墓,国家挖是考古?</span></a></li><li  ><a href="http://www.tepintehui.com/detail/40706?ce" title="福利| 要知道加这个群这么爽！我早进了" ><span>福利| 要知道加这个群这么爽！我早进了</span></a></li></ul></div>'

# start_mark='href="'
# end_mark="?ce"
# # 声明用于每次记录查找的变量，初始值就是索引值为0的字符
# record_position=0
#
# while record_position<len(string):
#     # 先确认下herf="这段字符所在起始索引值
#     start_index=string.find(start_mark,record_position)
#     if start_index==-1:
#          print('没有找到')
#          break
#     # 因为使用find找到的是start_mark的’h'这个字母的索引值，还有end_mark的？这个索引值
#     end_index=string.find(end_mark,start_index)
#     print(end_index)
#     ur1=string[start_index+len(start_mark):end_index+len(end_mark)]
#     record_position=end_index
#     print(ur1)
