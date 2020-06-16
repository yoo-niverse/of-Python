from generate_numbers import *
from get_score import *
from take_guess import *
    # main 코드에서 사용하기 위해 이전에 작성했던 함수들을 모두 import

ANSWER = generate_numbers()
    # ANSWER 상수에 임의로 추첨한 랜덤 정수 3개를 저장
tries = 1
    # 도전 횟수는 최초 1부터 기록되도록 설정

while True:
    # 조건이 True인 동안 반복 수행. 즉, break하여 반복문 밖으로 나가기 전까지 수행
    user = take_guess()
        # 플레이어에게 3개의 정수를 입력받는다.
    st, ba = get_score(user, ANSWER)
        # get_score 함수를 통해서 strike와 ball의 개수를 return 받는다.
    if st == 3:
        break
            # 만약 strike == 3을 만족하는 경우, 게임의 목적을 달성한 것이므로 즉시 반복문 밖으로 나간다.
    else:
        print(f'{st}S {ba}B')
        tries += 1
            # 그렇지 않은 경우에는 strike와 ball의 개수를 출력해주고, 도전 횟수를 +1 증가시킨다.

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))

''' ------ 동작 설명 ------
1. 각 module에서 작성한 함수들을 import 한다.
2. ANSWER 상수에 컴퓨터가 임의 추출한 3개의 랜덤 정수를 저장한다.
3. 반복문을 통해 플레이어에게 3개의 정수를 입력받고, strike와 ball을 계산하여 출력해준다.
4. 3strike가 된 경우 몇 번만에 맞추었는지를 출력하고, 그렇지 않은 경우에는 힌트를 주며 반복한다.

 ------ 시간이 걸린 이유 ------
 이미 작성한 함수들을 import 하여 다같이 동작되도록 설정만 하면 됐기에, 코드 작성에는 어려움이 없었다.
 최초 작성 후 실행시켜보니 정상적으로 수행은 되었으나, 문제는 3S가 아닌 경우 출력되는 *S *B이 무한 출력되며 다음 동작을 수행하지 않았다.
 처음에는 반복문에 어떤 문제가 있는 것이라 생각했는데, 알고보니 코드를 작성하는 과정에서 사용자의 입력을 받고 score를 계산하는 부분을
 반복문에 포함하지 않아 이런 문제가 발생했던 것이었다. '''
