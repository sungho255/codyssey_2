from dataclasses import dataclass
import json


@dataclass
class Quiz:
    question: str
    choices: list[str]
    answer: int

@dataclass
class QuizData:
    quizzes: list[Quiz]
    best_score: int

@dataclass
class QuizGame:
    quiz_data: QuizData
    select_num: int = 0

    def play_quiz(self):
        
        return True

    def add_quiz(self):
        return True

    def list_quiz(self):
        return True

    def check_score(self):
        return True

    def exit_game(self):
        return True

if __name__ == "__main__":
    menu_dict = {"퀴즈 풀기": None, "퀴즈 추가": None, "퀴즈 목록": None, "점수 확인": None, "종료": None}

    print('='*30)
    print('🎲나만의 퀴즈 게임🎲')
    print('='*30)

    for i, menu in enumerate(menu_dict.keys()):
        print(f"{i+1}. {menu}")
    print('='*30)

    input_num = int(input("메뉴를 선택하세요: "))
    
    print(list(menu_dict.keys())[input_num-1])
