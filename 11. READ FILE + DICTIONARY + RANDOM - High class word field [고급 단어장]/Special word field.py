''' vocabulary.txt에 저장된 단어를 random 모듈을 활용하여 랜덤 출제하는 코드 '''

import random as rnd
with open('vocabulary.txt', 'r') as voca:
    quest = {} # txt 파일에서 read한 후 가공된 단어들이 저장될 dictionary
    word = "" # txt 파일에서 read하여 가공한 단어들이 저장될 리스트

    for i in voca:
        word = i.strip().split(":")
            # 화이트 스페이스를 제거하고 :를 기준으로 단어와 뜻을 분리한 내용을 word에 저장
        quest[word[1]] = word[0]
            # txt 파일에서 읽어온 단어들이 quest라는 딕셔너리에 저장됨.
            
        # 이 for문이 while문 내부로 들어가면 랜덤이 적용되어도 처음엔 순서대로 문제가 출제된다. 처음에 딕셔너리에 저장된 단어가 한정적이기 때문.
        # 또한 txt 파일에서 더 이상 불러올 내용이 없으면 반복문이 종료되어 버리므로, 단어의 개수 이상 테스트 할 수 없게 된다.

    while True:
            test = list(quest.keys())
                # list 메소드를 이용하여 딕셔너리를 리스트로 변환할 수 있었다.
            answer_list = list(quest.values())
                # answer_list에는 단어들이 저장됨

            random_order = rnd.randint(0, (len(test)-1))
                # 리스트 길이에 맞추어 랜덤 정수 생성
            user_answer = input(test[random_order] + ": ")
                # 랜덤으로 문제를 출제하고

            if user_answer == 'q':
                break
            elif user_answer == answer_list[random_order]:
                    # 정답과 사용자의 입력이 일치하는지 확인
                print("맞았습니다!\n")

            else :
                print(f"틀렸습니다. 정답은 {answer_list[random_order]}입니다.\n")

''' ------ 동작 설명 ------
1. txt 파일에 저장되어 있는 단어와 뜻을 read하여 가공(strip, split)한다.
2. 가공한 데이터를 dictionary에 각각 key(뜻)와 value(단어)로 저장한다.
3. dictionary에서 key 부분을 list로 변환하여 순서를 갖게 한다.
4. random 모듈을 활용하여 임의의 정수를 발생시키고, 그를 index로 하여 문제를 출제한다.

 ------ 어려웠던 점 ------

 수도 코드로 구상하는데에는 큰 어려움이 없었지만, 문제의 조건으로 주어진 random 모듈과 dictionary를 어떻게 활용할지
 고민하는데 많은 시간을 소요했다. list와 달리 dictionary는 순서가 없으며, index가 없어서 정수로 호출할 수도 없었다.

 dictionary를 list로 변환하여 랜덤정수를 활용하면 되겠다는 생각은 일찍 할 수 있었지만 그것을 구현하는데 시간이 많이 걸렸다.
 나는 최초시도에서 비어있는 리스트 "quest_list = []"에 quest.keys()를 for문을 이용하여 차례로 저장하려고 했다.
 하지만 비어있는 list에는 이와 같은 방법으로 데이터를 저장할 수 없었다는 걸 알게 되었다.

 어떻게 해야할지 많은 시도를 거듭한 끝에 list 메소드라는 아주 간단한 방법을 알아냈고,
 dictionary의 key와 value를 각각 list 형으로 변환한 뒤 randint를 활용해 문제 출제 및 정답 확인을 할 수 있었다. '''
