''' 로또 시뮬레이션을 위한 코드 '''

from random import randint

def generate_numbers(n):
    randnum = []
    while len(randnum) <= n-1:
            # n개의 랜덤 정수를 뽑기 위해 정수가 저장되는 randnum 리스트의 길이가 (n-1)이 될때까지 반복
            # 이 때, n이 아닌 n-1인 이유는 : while문은 False가 된 직후에도 한번 더 수행하기 때문.

        tmpnum = randint(1, 45)
                # 뽑힌 정수가 중복 또는 0인지 확인하기 위해 임시로 tmpnum이라는 변수에 저장
        if tmpnum not in randnum :
            randnum.append(tmpnum)
                    # 랜덤 정수가 list에 없는 값일 경우 list를 append 하는 방식으로 추가
    return randnum

def draw_winning_numbers():
    normal_num = sorted(generate_numbers(6))
        # 6개의 일반 추첨번호를 저장
    tmp_special = generate_numbers(1)
        # 보너스 추첨번호 1개의 중복검사를 위하여 임시 변수에 저장
    while tmp_special in normal_num:
        # 임시 보너스 번호가 일반 추첨번호 리스트에 있다면 반복문을 계속 수행
        if tmp_special in normal_num :
            continue
                # 만약 임시 보너스 번호가 일반 추첨번호 리스트에 있을 경우 해당 숫자는 넘어간다.
        else :
            special_num = tmp_special
            result = normal_num.append(special_num)
                # 그렇지 않을 경우 임시 보너스 번호를 special_num 변수에 저장하고, 반환할 결과 리스트에 연결

    return (normal_num)

def count_matching_numbers(list_1, list_2):
    count = 0
    for i in list_1:
        for j in list_2:
            if i == j:
                count += 1
    return count

def check(numbers, winning_numbers):
    prizefor = count_matching_numbers(numbers, winning_numbers[0:6])
     # 사용자가 선택한 6개의 번호와 일반 추첨번호 6개를 우선 비교하여 prize에 겹치는 개수 저장
    bonus = count_matching_numbers(numbers, winning_numbers[6:])
     # 사용자가 선택한 6개의 번호 중 보너스 추첨번호와 일치하는 숫자가 있는지 여부를 bonus에 저장
    if prizefor == 6 :
        return(1000000000)
    elif prizefor == 5 and bonus == 1:
        return(50000000)
    elif prizefor == 5:
        return(1000000)
    elif prizefor == 4:
        return(50000)
    elif prizefor == 3:
        return(5000)

print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))
''' ------ 동작 설명 ------
generate_numbers(n)
1. 추첨할 수의 개수 n을 파라미터로 받아 함수 generate_numbers()를 수행
2. if문을 통해 추첨한 랜덤 정수가 randnum 리스트에 이미 존재하는지를 학인하며 반복 
3. 파라미터로 받은 n개의 랜덤 정수 반환 

draw_winning_numbers()
1. 일반 추첨번호 6개와 보너스 추첨번호 1개를 추출
2. 보너스 추첨번호가 일반 추첨번호와 중복되지 않는지 확인 후 최종 7개의 추첨번호 반환

count_matching_numbers(list_1, list_2)
1. 파라미터로 받은 두개의 리스트에서 중복값 개수 반환

 ------ 시간이 걸렸던 부분 ------
 
 [generate_numbers(n)]
 랜덤 정수 추첨과정에서 리스트에 이미 있는 값이 나올 경우, continue 문을 사용해버려서 파라미터로 받았던 값보다 적은 결과값이 return 되는 상황이 있었다. 이를 해결하기위해 다중 if문을 적용하고자 하였으나, 생각을 달리하여 최초사용했던 for 반복문(for i in range(0, n) 대신 while 문을 사용하였다.
 
 [draw_winning_numbers()]
 일반 추첨번호 6개와 보너스 번호 1개를 return 해야한다. 앞에 작성한 generate_numbers() 함수를 사용하면 간단했지만, 문제는 보너스 번호 1개가 일반 추첨번호와 중복이 되는지를 어떻게 처리할지였다. 고민 끝에 코드가 조금 복잡해지긴 했지만, while문과 if문을 이용하여 중복여부를 검토하고 저장하는 방식으로 결정했다.
 
 * 문제 해결 후 모범답안을 확인해보니 그 코드에서는 그냥 애초에 7개의 랜덤정수를 추출하고, 그 중에서 [:6]을 일반 추첨번호로 하여 sorting, [6:]을 보너스 추첨번호로 처리했다. 이렇게 단순하게 생각하니 코드도 내 코드에 비해 훨씬 짧고 간결했다. 생각하는 연습을 더 해야겠다.
 
 [check(numbers, winning_numbers)]
 상금 조건에 맞추어 if 문으로 판단하는 과정에서 상금번호 리스트의 slicing을 잘못했다. winning_numbers[0:6]을 통해 마지막 보너스 번호를 제외한 6개를 count_matching_numbers() 함수로 보냈어야했는데, [0:5]만 전달하는 바람에 보너스 번호까지 제대로 파악이 되지 않은 것을 모르고 있어서 시간이 오래 걸렸다.

 
 
 '''
