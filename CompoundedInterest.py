# compounded interest calculator
def compounded_interest(amount, rate, time):
    print('Principal amount: ' + str(amount))
    period = 1
    unpc_rate = rate / 100
    while period <= time:
        com_int = amount * (1 + unpc_rate)**period
        print('Year' + str(period) + ': $' + str(com_int))
        period = period + 1
        if period > time:
            break

compounded_interest(100, 5, 8)

# online solution
def invest(amount, rate, time):
    print('Principal amount:{}'.format(amount))
    for t in range(1, time + 1):
        amount = amount * (1 + rate)
        print('Year {}: ${}'.format(t, amount))
invest(100, 0.05, 8)