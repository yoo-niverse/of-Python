def calculate_change(payment, cost):
    change = payment - cost
    
    thousand_50 = change // 50000
    print(f'50000원 지폐: {thousand_50}장')
    thousand_10 = (change % 50000) // 10000
    print(f'10000원 지폐: {thousand_10}장')
    thousand_5 = (change - (thousand_50 * 50000 + thousand_10 * 10000)) // 5000
    print(f'5000원 지폐: {thousand_5}장')
    thousand_1 = (change - (thousand_50 * 50000 + thousand_10 * 10000 + thousand_5 * 5000)) // 1000
    print(f'1000원 지폐: {thousand_1}장')

calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)

#2차 시도 - '//(버림 나눗셈)' 및 '%(나머지)' 연산자 활용
