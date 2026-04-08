from dataclasses import dataclass
import json

menu_list = ["퀴즈 풀기","퀴즈 추가","퀴즈 목록","점수 확인","종료"]

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
    print('='*30)
    print('🎲나만의 퀴즈 게임🎲')
    print('='*30)
