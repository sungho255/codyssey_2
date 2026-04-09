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

    # 퀴즈 풀기
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

    # 퀴즈 추가
    def add_quiz(self):
        print("➕새로운 퀴즈를 추가합니다.")
        new_question = input("문제를 입력하세요: ")
        new_choices = []
        for i in range(len(self.quiz_data.quizzes[0].choices)):
            new_choice = input(f"선택지 {i+1}: ")
            new_choices.append(new_choice)
        new_answer = int(input("정답 번호(1~4): "))

        new_quiz = Quiz(question=new_question, choices=new_choices, answer=new_answer)
        self.quiz_data.quizzes.append(new_quiz)
        print("퀴즈가 추가되었습니다!")
        return True

    # 퀴즈 목록
    def list_quiz(self): 
        print(f"등록된 퀴즈 목록 ({len(self.quiz_data.quizzes)}개)")
        print('-'*30)   
        for i in range(len(self.quiz_data.quizzes)):
            quiz = self.quiz_data.quizzes[i]
            print(f"[{i+1}] {quiz.question}")
        print('-'*30)

    # 점수 확인
    def check_score(self):
        return True

    # 종료
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
