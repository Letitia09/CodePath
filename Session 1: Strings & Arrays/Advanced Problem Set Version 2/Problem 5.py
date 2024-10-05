def wealthiest_customer(accounts):
    wealthiest = []
    for vals in accounts:
        wealthiest.append(sum(vals))
    print([wealthiest.index(max(wealthiest)),max(wealthiest)])
	
accounts = [
	[1, 2, 3],
	[3, 2, 1]
]
wealthiest_customer(accounts)

accounts = [
	[1, 5],
	[7, 3],
	[3, 5]
]
wealthiest_customer(accounts)

accounts = [
	[2, 8, 7],
	[7, 1, 3],
	[1, 9, 5]
]
wealthiest_customer(accounts)
