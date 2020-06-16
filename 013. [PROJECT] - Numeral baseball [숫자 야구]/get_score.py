def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    i = 0
    for i in range(0, len(guess)):
        if guess[i] == solution[i]:
            strike_count += 1
                # 동일한 인덱스로 2개 list의 요소를 비교하여, 일치하는 경우 strike를 +1 증가

        elif guess[i] in solution and guess[i] != solution[i]:
            ball_count += 1
                # 또는 guess[i]요소가 solution 리스트에 존재하는 경우에는 ball을 +1 증가
                # 단, 같은 자리에 있는 요소도 ball로 취급할 수 있기에, 동일 index에 존재하는 경우는 제외

        i += 1

    return strike_count, ball_count


''' ------ 동작 설명 ------
1. 사용자가 입력한 3개의 정수(guess)와 컴퓨터가 임의로 추출한 랜덤 정수 3개(solution)을 파라미터로 받는다.
2. 2개의 list를 사용하여 각 요소에 대해 동일 index에 일치하는 요소가 있는지, 또는 포함된 요소가 있는지를 검사한다.
3. 최종적으로 strike_count와 ball_count를 동시 반환한다.

 ------ 오래걸린 이유 ------
 
 구상은 어렵지 않았으나, 처음에는 반복문으로 [while i < len(guess)] 대신에 [for i in range(0, 2)]를 사용했다.
 막상 실행시켜보니 끝까지 정상 수행되지 않아서 strike나 ball이 하나씩 부족하게 결과가 출력됐다.
 내가 착각했던 것이, range(0, 2)이면 0~1까지만 반복수행하는 것이므로 0, 3까지로 했어야했는데 그 부분을 생각치 못했었다.
 
 ------ 새로 알게된 내용 ------
 
 함수 실행의 결과로 2개 이상의 결과를 return 할 수 있음을 알게 됐다.
 return 뒤에 반환할 data를 모두 쉼표로 구분하여 작성하고, 결과를 받는 위치에서도 대응하여 변수를 작성하면 된다.
 ex_ return a, b, c : A, B, C = function()
 '''
