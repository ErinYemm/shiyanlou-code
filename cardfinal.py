# -*- coding: UTF-8 -*-
import random
import time

#初始化角色卡
role = ('宫本武藏', '李白', '诸葛亮', '武则天', '嬴政')
weight_list = (5, 10, 20, 50, 100)
weight_compare = (5, 15, 35, 85, 185)

#背包里的卡片名及对应数量
bag_card = {}

while 1:
    choose = int(input('''
  	充值能让你变得更强！
  	请选择指令：
  	1.抽卡
  	2.查看背包
 	3.离开
  '''))
    if choose == 1:
        num = int(input('请输入抽卡次数：'))
        for i in range(num):
            #生成1到总权重之间的随机数
            rand_num = random.randint(1, weight_compare[-1])
            n = 0
            #将随机数依次向后比较，确定所在区间
            while rand_num > weight_compare[n]:
                n += 1
            if role[n] not in bag_card.keys():
                bag_card[role[n]] = 1
            else:
                bag_card[role[n]] += 1
            print('你抽到了：{}'.format(role[n]))
        print('卡已存入了背包')
        print('-----------------')
        time.sleep(0.3)
    if choose == 2:
        if len(bag_card) > 0:
            for key, value in bag_card.items():
                print('{} - 数量：{}'.format(key, value))
        else:
            print("你的背包空空如也，快来抽取些英雄吧！")
        print('------------------')
    if choose == 3:
        break
