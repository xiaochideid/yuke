import math
user =input('输入主角名称')
kills =input('输入技能名称')
msg ='攻击次数{0}'
skill_valua ='0'
ade_kills = '0'
kills_die_num = '0'
if user == '赵云':
    skill_num = math.floor(500/50)
    if kills == '物理攻击':
        kills_die_num = math.ceil(10000/80)
    elif kills =='技能攻击':
        kills_die_num =math.ceil(10000/120)
    else:
        kills_die_num =skill_num+math.ceil((10000-skill_num*120)/80)
        ade_kills =kills_die_num-skill_num
        skill_valua =500%50
        msg =('需要总攻击次数 {0},物理攻击次数{1},技能攻击次数{2}剩余能量值{3}')
elif user == '李白':
    skill_num = math.floor(350/80)
    if kills == '物理攻击':
        kills_die_num =math.ceil(10000/30)
    elif kills =='技能攻击':
        kills_die_num =math.ceil(10000/100)
    else:
        kills_die_num =skill_num+math.ceil((10000-skill_num*100)/30)
        ade_kills =kills_die_num-skill_num
        skill_valua =350%80
        msg =('需要总攻击次数 {0},物理攻击次数{1},技能攻击次数{2}剩余能量值{3}')
elif user == '刘备':
    skill_num = math.floor(400/100)
    if kills == '物理攻击':
        kills_die_num =math.ceil(10000/50)
    elif kills =='技能攻击':
        kills_die_num =math.ceil(10000/200)
    else:
        kills_die_num =skill_num+math.ceil((10000-skill_num*200)/50)
        ade_kills =kills_die_num-skill_num
        skill_valua =400%100
        msg =('需要总攻击次数{0},物理攻击次数{1},技能攻击次数{2}剩余能量值{3}')
print (msg.format(kills_die_num,ade_kills,skill_num,skill_valua))