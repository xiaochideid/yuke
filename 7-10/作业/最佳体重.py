# 最佳体重计算
# 已知一个人的身高是180，体重是80公斤，计算一个人的最佳体重
# 最佳体重计算公式：
# 最佳体重 = 身高 - 105
# 通过体重和最佳体重的对比，利用print输出此人是体重正常还是偏胖还是偏瘦。

# 2.最佳体重
while True:
    height=int(input('请输入您的身高：'))
    weight=int(input('请输入您的体重：'))
    best_weight=height-105
    if weight>best_weight:
        print('您偏胖')
    if weight<best_weight:
        print('您偏瘦')
    if weight==best_weight:
        print('您的体重正常')

# height = float(input('请输入身高:'))
# weight = float(input('请输入体重:'))
# optimalWeight=height-105
# if optimalWeight<weight:
#     print('此人体重偏胖')
#     if optimalWeight>weight:
#         print('此人体重偏瘦')
# else:
#     print('完美身材')