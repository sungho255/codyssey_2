from dataclasses import dataclass

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
