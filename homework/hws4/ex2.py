prices={
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock={
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15

}
name=["apple", "pear"]
thislist=[prices, stock ]
total_money = 0
for x in name:
    print(x)
    a = prices[x]
    b = stock[x]
    print("price",  a)
    print("stock", b)        
    total = a * b
    print("total:", total)
    total_money += total
    print("total money: ", total_money)
