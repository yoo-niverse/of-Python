def calculate_change(payment, cost):
    change = payment - cost
    a = (change // 50000)
    change -= a * 50000
    print(f'50000원 지폐: {a}장')
    b = (change // 10000)
    change -= b * 10000
    print(f'10000원 지폐: {b}장')
    c = (change // 5000)
    change -= c * 5000
    print(f'5000원 지폐: {c}장')
    d = (change // 1000)
    change -= d * 1000
    print(f'1000원 지폐: {d}장')

calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)

#1차시도
