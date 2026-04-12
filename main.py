from dataclasses import dataclass, field
import json
import sys

# 퀴즈 데이터 구조 정의
@dataclass  
class Quiz:
    question: str
    choices: list[str]
    answer: int

# 퀴즈 데이터와 최고 점수 관리
@dataclass
class QuizData:
    quizzes: list[Quiz]
    best_score: int

def load_quiz_data(file_path: str) -> QuizData:
    with open(file_path, 'r') as f:
        data = json.load(f)
    quizzes = [Quiz(**quiz) for quiz in data['quizzes']]
    best_score = data['best_score']
    return QuizData(quizzes=quizzes, best_score=best_score)

class QuizGame:
    def __init__(self):
        self.__quiz_data = load_quiz_data('state.json')

    # 퀴즈 풀기
    def play_quiz(self):
        print(f"퀴즈를 시작합니다! (총 {len(self.__quiz_data.quizzes)}문제)")

        for i in range(len(self.__quiz_data.quizzes)):
            print('-'*30)
            quiz = self.__quiz_data.quizzes[i]
            print(f"[문제 {i+1}]")
            print(quiz.question)

            for j, choice in enumerate(quiz.choices):
                print(f"{j+1}. {choice}")

            user_answer = int(input("정답 입력: "))
            if user_answer == quiz.answer:
                print("정답입니다!")
            else:
                print(f"틀렸습니다! 정답은 {quiz.answer}번입니다.")
            print('-'*30)

    # 퀴즈 추가
    def add_quiz(self):
        print("➕새로운 퀴즈를 추가합니다.")
        new_question = input("문제를 입력하세요: ")
        new_choices = []
        for i in range(len(self.__quiz_data.quizzes[0].choices)):
            new_choice = input(f"선택지 {i+1}: ")
            new_choices.append(new_choice)
        new_answer = int(input("정답 번호(1~4): "))

        new_quiz = Quiz(question=new_question, choices=new_choices, answer=new_answer)
        self.__quiz_data.quizzes.append(new_quiz)
        print("퀴즈가 추가되었습니다!")

    # 퀴즈 목록
    def list_quiz(self): 
        print(f"등록된 퀴즈 목록 ({len(self.__quiz_data.quizzes)}개)")
        print('-'*30)   
        for i in range(len(self.__quiz_data.quizzes)):
            quiz = self.__quiz_data.quizzes[i]
            print(f"[{i+1}] {quiz.question}")
        print('-'*30)

    # 점수 확인
    def check_score(self):
        best_score = self.__quiz_data.best_score
        total_quizzes = len(self.__quiz_data.quizzes)
        print(f"🏆최고 점수: {best_score}점 ({total_quizzes}문제 중 {best_score}문제 정답)")
        
    # 종료
    def exit_game(self):
        sys.exit(0)

if __name__ == "__main__":
    game = QuizGame()
    menu_dict = {"퀴즈 풀기": game.play_quiz, "퀴즈 추가": game.add_quiz, "퀴즈 목록": game.list_quiz, "점수 확인": game.check_score, "종료": game.exit_game}
    
    while True:
        print('='*30)
        print('🎲나만의 퀴즈 게임🎲')
        print('='*30)

        for i, menu in enumerate(menu_dict.keys()):
            print(f"{i+1}. {menu}")
        print('='*30)
        try:
            input_num = int(input("메뉴를 선택하세요: ")) - 1

            print(list(menu_dict.keys())[input_num])
            menu_dict[list(menu_dict.keys())[input_num]]()
        # ValueError: int() 변환 실패 - 공백 , IndexError: 메뉴 번호 범위 초과
        except (ValueError, IndexError):
            print("잘못된 입력입니다. 다시 시도하세요.")
