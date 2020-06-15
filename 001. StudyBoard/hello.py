import random as rnd

with open('vocabulary.txt', 'r') as voca:
    quest = {}
    word = ""

    for i in voca:
        word = i.strip().split(":") # 화이트 스페이스를 제거하고 :를 기준으로 단어와 뜻을 분리한 내용을 word에 저장
        quest[word[1]] = word[0] # txt 파일에서 읽어온 단어들이 quest라는 딕셔너리에 저장됨.
    # 이 for문이 while문 내부로 들어가면 랜덤이 적용되어도 처음엔 순서대로 문제가 출제된다. 처음에 딕셔너리에 저장된 단어가 한정적이기 때문.
    # 또한 txt 파일에서 더 이상 불러올 내용이 없으면 반복문이 종료되어 버리므로, 단어의 개수 이상 테스트 할 수 없게 된다.

    while True:
            test = list(quest.keys()) # list 메소드를 이용하여 딕셔너리를 리스트로 변환할 수 있었다.
            answer_list = list(quest.values()) # answer_list에는 단어들이 저장됨

            random_order = rnd.randint(0, (len(test)-1)) # 리스트 길이에 맞추어 랜덤 정수 생성
            user_answer = input(test[random_order] + ": ") # 랜덤으로 문제를 출제하고

            if user_answer == 'q':
                break
            elif user_answer == answer_list[random_order]: # 정답과 사용자의 입력이 일치하는지 확인
                print("맞았습니다!\n")

            else :
                print(f"틀렸습니다. 정답은 {answer_list[random_order]}입니다.\n")

