#原始收入，获取用户输入，转换为int
income = int(input("请输入你的薪资： "))

#税后收入
salary = 0

#应纳税所得额
shouldPay = 0

#纳税金额
tax = 0

def calculator(num):
    """计算税后薪资的函数，参数为原始收入"""

    #应纳税所得额为收入减去起征点5000元
    shouldPay = num - 5000

    #根据扣税表不同薪资的档次作条件判断
    if shouldPay <= 0:
        tax = 0
    elif 0 < shouldPay <= 3000:
        tax = shouldPay * 0.03
    elif 3000 < shouldPay <= 12000:
        tax = shouldPay * 0.1 - 210
    elif 12000 < shouldPay <= 25000:
        tax = shouldPay * 0.2 - 1410
    elif 25000 < shouldPay <= 35000:
        tax = shouldPay * 0.25 - 2660
    elif 35000 < shouldPay <= 55000:
        tax = shouldPay * 0.3 - 4410
    elif 55000 < shouldPay <= 80000:
        tax = shouldPay * 0.35 - 7160
    else:
        tax = shouldPay * 0.45 - 15160

    #最终收入为税前收入减去税款，并保留两位小数
    salary = num - tax

    return "{:.2f}".format(salary)

print('你的税后收入是： {}'.format(calculator(income)))

