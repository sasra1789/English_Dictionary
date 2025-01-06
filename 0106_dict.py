

import json
import random # 필요한 라이브러리들을 불러옵니다
import os

# 영어 단어장을 저장할 딕셔너리
dictionary = {} # 빈 딕셔너리를 생성하여 단어장으로 사용할 준비를 합니다

def load_dictionary():
    """단어장 파일을 불러오는 함수"""
    json_path = "home/rapa/my_python/json/english_dictionary.json" # 단어장 파일의 저장 위치를 지정합니다
    
    # 파일이 없으면 빈 딕셔너리 반환
    if not os.path.exists(json_path): # 파일이 존재하는지 확인하고, 없으면 빈 딕셔너리를 반환합니다
        return {}
    
    # 파일이 있으면 불러오기
    with open(json_path, "r", encoding='utf-8') as file: # 파일을 읽기 모드로 열고, UTF-8 인코딩을 사용하여 한글도 처리할 수 있게 합니다
        return json.load(file) # 
 
def save_dictionary(dictionary):
    """단어장을 파일로 저장하는 함수"""
    json_path = "home/rapa/my_python/json/english_dictionary.json" 
    with open(json_path, "w", encoding='utf-8') as file: #파일을 쓰기 모드로 열어 저장할 준비를 합니다
        json.dump(dictionary, file, ensure_ascii=False, indent=4) # 딕셔너리를 JSON 형식으로 저장하며, 한글 지원(ensure_ascii=False)과 들여쓰기(indent=4)를 설정합니다

def add_word():
    """단어 추가 함수"""
    word = input("추가할 영단어를 입력하세요: ") # 사용자로부터 영단어를 입력받습니다
    meaning = input("단어의 뜻을 입력하세요: ") # 입력받은 단어의 뜻을 저장합니다
    dictionary[word] = meaning #단어와 뜻을 딕셔너리에 추가합니다
    print(f"'{word}' 단어가 추가되었습니다!") 

def edit_word():
    """단어 수정 함수"""
    word = input("수정할 단어를 입력하세요: ")
    if word in dictionary:  # 수정하려는 단어가 딕셔너리에 있는지 확인합니다
        meaning = input("새로운 뜻을 입력하세요: ")
        dictionary[word] = meaning # 있다면 새로운 뜻으로 업데이트합니다
        print(f"'{word}'의 뜻이 수정되었습니다!")
    else:
        print("존재하지 않는 단어입니다.")

def delete_word():
    """단어 삭제 함수"""
    # 이 함수가 실행되면 1개의 인풋을 받아서 영어 딕셔너리에 키가 있는지 확인하고 
    #있으면 키를 지운다.
    word = input("삭제할 단어를 입력하세요: ")
    if word in dictionary:
        del dictionary[word]  #딕셔너리에서 해당 단어를 삭제합니다
        print(f"'{word}'가 삭제되었습니다!")
    else:
        print("존재하지 않는 단어입니다.")

def play_game():
    """단어 게임 함수"""
    if len(dictionary) < 3: #게임을 시작하기 전 최소 3개의 단어가 있는지 확인합니다
        print("게임을 하려면 최소 3개의 단어가 필요합니다!")
        return


# 단어사전에 있는 딕셔너리 키 중 랜덤으로 3개를 가지고 오면 쉽게 풀 수 있을 듯
    correct = 0
    words = random.sample(list(dictionary.keys()), 3) # 딕셔너리에서 무작위로 3개의 단어를 선택합니다
    
    for word in words: # 선택된 단어들로 퀴즈를 진행합니다
        print(f"\n'{word}'의 뜻은 무엇일까요?")
        answer = input("답: ")
        if answer == dictionary[word]: # 사용자의 답이 정확한지 확인합니다
            print("정답입니다!")
            correct += 1
        else:
            print(f"틀렸습니다. 정답은 '{dictionary[word]}' 입니다.")
    
    # 점수 계산 및 결과 출력
    if correct == 3:
        print("\n대단해요! 100점입니다!")
    elif correct == 2:
        print("\n70점입니다. 조금만 더 노력하세요!")
    elif correct == 1:
        print("\n30점입니다. 더 열심히 공부해주세요.")
    else:
        print("\n0점. 마 유치원다시다녀라")
    
dictionary = load_dictionary()
    
while True: # 프로그램을 계속 실행하는 무한 루프를 시작합니다
    command = input("\n무엇을 하시겠습니까? (add/edit/delete/game/exit): ") # 사용자로부터 명령어를 입력받습니다
        
    if command == "add": # if/elif 구문들: 입력받은 명령어에 따라 적절한 함수를 실행합니다
        add_word()
    elif command == "edit":
        edit_word()
    elif command == "delete":
        delete_word()
    elif command == "game":
        play_game()
    elif command == "exit":
         save_dictionary(dictionary)
         print("프로그램을 종료합니다. 단어장이 저장되었습니다!")
         break
    else:
        print("잘못된 명령어입니다.")

