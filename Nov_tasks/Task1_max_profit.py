stock_prices = [100, 180, 260, 310, 40, 535, 695]
profit = 0
sell_day = 0
buy_day = 0
buy_stock = 0
sell_stock = 0
for i in range(len(stock_prices)):
    for j in range(i,len(stock_prices)):
        if stock_prices[j]-stock_prices[i] > profit:
            profit = stock_prices[j]-stock_prices[i]
            buy_day = i+1
            sell_day = j+1
            buy_stock = stock_prices[i]
            sell_stock = stock_prices[j]
print(f"Buy Day {buy_day} stock price {buy_stock} sell day {sell_day} sell_stock {sell_stock} Max Profit {[profit]}")
    