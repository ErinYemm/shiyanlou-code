import random
import time

#初始化角色卡
role = ('宫本武藏', '李白', '诸葛亮', '武则天', '嬴政')

#背包里的卡片名及对应数量
bag_card = {}

while 1:
    num = int(input('''
  	充值能让你变得更强！
  	请选择指令：
  	1.抽卡
  	2.查看背包
 	3.离开
  '''))
    if num == 1:
        card_num = int(input('请输入抽卡次数：'))
        for i in range(card_num):
            role_card = random.choice(role)
            print('你抽到了：{}'.format(role_card))
            if role_card not in bag_card.keys():
                bag_card[role_card] = 0
            bag_card[role_card] += 1
        print('卡已存入了背包')
        print('-----------------')
        time.sleep(float(0.3))
    if num == 2:
        if len(bag_card) > 0:
            for key in bag_card.keys():
                print('{} - 数量：{}'.format(key, bag_card[key]))
        else:
            print("你的背包空空如也，快来抽取些英雄吧！")
        print('------------------')
    if num == 3:
        break
