#输入总的投资年限，每年定投金额，每年收益率
money = float(input('每年定投多少人民币？ '))
years = int(input('定投多少年？ '))
pr = float(input('预计年度收益率？ '))

sum_invested = 0
tot_profit = 0
sum_money = 0

for i in range(years):
    sum_invested = sum_invested + money
    profit = sum_invested * pr/100
    sum_invested = sum_invested + profit
    tot_profit = tot_profit + profit
    sum_money = sum_money + money
    print('时间进入第',i+1,'年:')
    print(i+1,'年，共投入工资',sum_money)
    print('第',i+1,'年末收益：', profit)
    print(i+1,'年累计获得收益共：',tot_profit)
    print(i+1,'年本金收益合：',sum_invested,'\n')
    
rate_tt = tot_profit / sum_money*100
print('收益率',rate_tt,'\n')
    
