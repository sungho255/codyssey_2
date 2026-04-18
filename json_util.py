
from contexts import load_file_handler
from quiz import QuizData, Quiz
import json

def load_quiz_data(file_path: str) -> QuizData:
    with load_file_handler(file_path) as f:
        data = json.load(f)

        quizzes = [Quiz(**quiz) for quiz in data['quizzes']]
        best_score = data['best_score']
        return QuizData(quizzes=quizzes, best_score=best_score)

def save_quiz_data(file_path: str, quiz_data: QuizData):
    # 1. 객체 데이터를 딕셔너리 형태로 변환
    data_to_save = {
        "quizzes": [
            {
                "question": q.question,
                "choices": q.choices,
                "answer": q.answer
            } for q in quiz_data.quizzes
        ],
        "best_score": quiz_data.best_score
    }
    
    # 2. 파일에 바로 쓰기
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data_to_save, f, indent=4, ensure_ascii=False)
