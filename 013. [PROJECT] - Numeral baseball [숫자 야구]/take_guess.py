def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    new_guess = []

    while (len(new_guess) < 3):
        tmp = int(input(f"{len(new_guess)+1}번째 숫자를 입력하세요: "))
        if tmp not in new_guess and (0 <= tmp <= 9):
            new_guess.append(tmp)
                # tmp에 저장한 임시 랜덤정수가 중복이 아니고, 범위 내일 경우 list에 추가

        elif tmp in new_guess:
            print("중복된 숫자입니다. 다시 입력하세요")
                # tmp로 추출된 랜덤 정수가 list에 이미 존재할 경우 추가하지 않음

        elif tmp < 0 or tmp > 9:
            print("범위를 벗어난 숫자입니다. 다시 입력하세요.")
                # tmp로 추출된 랜덤 정수가 숫자 제한 범위를 벗어날 경우 추가하지 않음

    return new_guess

''' ------ 동작 설명 ------
1. input 함수를 통해 사용자에게 숫자 3개를 입력받을 동안 반복 수행
2. 입력 받은 후 중복여부와 범위를 검사한 후 적합할 경우 리스트에 추가
3. 요소가 3개가 된 리스트를 반환
'''
