from dataclasses import dataclass, field
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

def load_quiz_data(file_path: str) -> QuizData:
    with open(file_path, 'r') as f:
        data = json.load(f)
    quizzes = [Quiz(**quiz) for quiz in data['quizzes']]
    best_score = data['best_score']
    return QuizData(quizzes=quizzes, best_score=best_score)

class QuizGame:
    quiz_data: QuizData = field(default_factory=lambda: load_quiz_data('quiz_data.json'))

    def play_quiz(self):
        print(f"퀴즈를 시작합니다! (총 {len(self.quiz_data.quizzes)}문제)")

        for i in range(len(self.quiz_data.quizzes)):
            print('-'*30)
            quiz = self.quiz_data.quizzes[i]
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

    def add_quiz(self):
        return True

    def list_quiz(self): 
        print(f"등록된 퀴즈 목록 ({len(self.quiz_data.quizzes)}개)")
        print('-'*30)   
        for i in range(len(self.quiz_data.quizzes)):
            quiz = self.quiz_data.quizzes[i]
            print(f"[{i+1}] {quiz.question}")
        print('-'*30)

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
