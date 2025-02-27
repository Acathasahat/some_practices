#输入一次性投资某产品的总金额，计划持有的年限及每年收益率
money = float(input('一次性投多少人民币？ '))
years = int(input('持有多少年？ '))
pr = float(input('预计年度收益率？ '))
sum_money_profit = money * (1 + pr/100)
for i in range(years-1):
    sum_money_profit = sum_money_profit * (1 + pr/100)
    print(i+2,'年本金收益合：',sum_money_profit,'\n')
    
rate_tt = (sum_money_profit - money) / money*100
print('收益率',rate_tt,'\n')
    
