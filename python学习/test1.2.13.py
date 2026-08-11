name = "传智播客"
stock_code = "003032"
stock_price = 19.99
stock_price_daily_growthly_factor = 1.2
growth_days = 7
print(f"公司名称为{name},股票代码为:{stock_code},当前股价：{stock_price}")
print("每日增长系数为:%.1f ,经过%d天的增长后, 股价到达了：%.2f" %(stock_price_daily_growthly_factor,growth_days,(stock_price*1.2**growth_days)))