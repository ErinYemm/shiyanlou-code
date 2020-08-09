import random

#初始化指令号
num = 0

#初始化角色卡
role = ('宫本武藏', '李白', '诸葛亮', '武则天', '嬴政')

#背包里的卡片名
bag_card = []

while num != 4:
    num = int(input('''
  	充值能让你变得更强！
  	请选择指令：
  	1.抽卡
  	2.查看背包
 	3.整理背包
 	4.离开
  '''))
    if num == 1:
        card_num = int(input('请输入抽卡次数：'))
        for i in range(card_num):
            role_card = random.choice(role)
            print('你抽到了：{}'.format(role_card))
            bag_card.append(role_card)
        print('卡已存入了背包')
        print('-----------------')
    if num == 2:
        if len(bag_card) > 0:
            for i in range(len(bag_card)):
                print(bag_card[i])
        else:
            print("你的背包空空如也")
        print('------------------')
    if num == 3:
        bag_card.sort()
        for i in range(len(bag_card)):
            print(bag_card[i])
        print('------------------')

