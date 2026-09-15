def running_balance(transactions):
    balance = 0
    result = []
    for t in transactions:
        balance += t
        result.append(balance)
    return result

print(running_balance([100, -30, 50, -20]))
print(running_balance([]))
print(running_balance([500, 200, -700]))