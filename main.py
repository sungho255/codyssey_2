from json_util import load_quiz_data, save_quiz_data
from contexts import menu_input_handler
from quiz import Quiz

import signal
import json
import sys

def control_z_handler(signum, frame):
    # Ctrl + Z가 들어오면 즉시 예외를 발생시킴
    raise EOFError("Ctrl+Z가 감지되었습니다!")

# macOS/Linux에서 Ctrl+Z(SIGTSTP) 시그널에 핸들러 등록
if hasattr(signal, 'SIGTSTP'):
    signal.signal(signal.SIGTSTP, control_z_handler)

class QuizGame:
    def __init__(self):
        self.__quiz_data = load_quiz_data('state.json')

    # 퀴즈 풀기
    def play_quiz(self):
        print(f"퀴즈를 시작합니다! (총 {len(self.__quiz_data.quizzes)}문제)")
        current_score = 0

        for i in range(len(self.__quiz_data.quizzes)):
            quiz = self.__quiz_data.quizzes[i]
            max_choice = len(self.__quiz_data.quizzes[i].choices)
            while True:
                print('-'*30)
                quiz = self.__quiz_data.quizzes[i]
                print(f"[문제 {i+1}]")
                print(quiz.question)

                for j, choice in enumerate(quiz.choices):
                    print(f"{j+1}. {choice}")
                with menu_input_handler():
                    user_answer = int(input("정답 입력: "))

                    if user_answer < 1 or user_answer > max_choice:
                        print("잘못된 입력입니다. 다시 시도하세요.")
                        continue

                    if user_answer == quiz.answer:
                        print("정답입니다!")
                        current_score += 1
                        print(f"\n 현재 점수: {current_score} / {len(self.__quiz_data.quizzes)}")
                    else:
                        print(f"틀렸습니다! 정답은 {quiz.answer}번입니다.")
                    
                    break
                print('-'*30)
        print(f"\n🎮 퀴즈 종료! 최종 점수: {current_score} / {len(self.__quiz_data.quizzes)}")

        # 최고 점수 갱신 확인
        if current_score > self.__quiz_data.best_score:
            print(f"축하합니다! 최고 점수가 갱신되었습니다: {self.__quiz_data.best_score} -> {current_score}")
            self.__quiz_data.best_score = current_score
            
            # 파일에 즉시 저장하여 데이터 영속성 확보
            save_quiz_data('state.json', self.__quiz_data)
        else:
            print(f"현재 최고 점수: {self.__quiz_data.best_score}")

    # 퀴즈 추가
    def add_quiz(self):
        print("➕새로운 퀴즈를 추가합니다.")
        # 1. 문제 입력 (문자열이라 예외 확률은 낮지만 일관성을 위해 유지)
        while True:
            with menu_input_handler():
                new_question = input("문제를 입력하세요: ").strip()
                if not new_question:
                    print("문제가 비어있습니다. 다시 입력하세요.")
                    continue
                break

        # 2. 선택지 입력
        new_choices = []
        num_of_choices = len(self.__quiz_data.quizzes[0].choices)
        i = 0
        while i < num_of_choices:
            with menu_input_handler():
                choice = input(f"선택지 {i+1}: ").strip()
                if not choice:
                    print("선택지가 비어있습니다.")
                    continue
                new_choices.append(choice)
                i += 1  # 성공적으로 입력했을 때만 다음 인덱스로

        # 3. 정답 번호 입력
        while True:
            with menu_input_handler():
                new_answer = int(input(f"정답 번호 (1~{num_of_choices}): "))
                if 1 <= new_answer <= num_of_choices:
                    break
                else:
                    print(f"1에서 {num_of_choices} 사이의 숫자를 입력하세요.")

        # 4. 객체 생성 및 저장
        new_quiz = Quiz(question=new_question, choices=new_choices, answer=new_answer)
        self.__quiz_data.quizzes.append(new_quiz)
        save_quiz_data('state.json', self.__quiz_data)
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
    menu_names = tuple(menu_dict.keys())
    MAX_MENU = len(menu_names)

    while True:
        print('='*30)
        print('🎲나만의 퀴즈 게임🎲')
        print('='*30)

        for i, menu in enumerate(menu_names):
            print(f"{i+1}. {menu}")
        print('='*30)
        
        with menu_input_handler():
            input_num = int(input("메뉴를 선택하세요: "))
            
            if input_num < 1 or input_num > MAX_MENU:
                print("잘못된 입력입니다. 다시 시도하세요.")
                continue
            
            input_num -= 1

            print(menu_names[input_num])
            menu_dict[menu_names[input_num]]()
        
        
        
