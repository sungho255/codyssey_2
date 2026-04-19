# 🎲 나만의 퀴즈 게임 (CLI Quiz Engine)

본 프로젝트는 파이썬의 객체지향 설계와 예외 처리 메커니즘을 활용하여 구축된 **CLI 기반 퀴즈 엔진**입니다. 단순한 기능 구현을 넘어 데이터 영속성(Persistence)과 견고한 에러 핸들링을 아키텍처 레벨에서 관리하도록 설계되었습니다.

---

## 1. 실행 방법

본 프로젝트는 Python 3.7+ 환경에 최적화되어 있습니다.

1.  **레포지토리 클론**
    ```bash
    git clone [https://github.com/username/quiz-game.git](https://github.com/username/quiz-game.git)
    cd quiz-game
    ```
2.  **프로그램 실행**
    ```bash
    python main.py
    ```
    *주의: 최초 실행 시 `state.json` 파일이 없을 경우 기본 템플릿으로 자동 생성됩니다.*

---

## 2. 기능 목록
<img src="./screenshot/퀴즈 메뉴.png" width="300px" alt="설명">
* **퀴즈 풀기 (Play Mode):** 등록된 퀴즈를 순차적으로 풀며 실시간 점수 계산 및 최고 점수 기록 기능을 제공합니다.
<img src="./screenshot/퀴즈 풀기.png" width="300px" alt="설명">
* **퀴즈 추가 (Management):** 대화형 인터페이스를 통해 새로운 문제를 동적으로 추가하며 즉시 JSON DB에 반영합니다.
<img src="./screenshot/퀴즈 추가.png" width="300px" alt="설명">
<img src="./screenshot/퀴즈 추가1.png" width="300px" alt="설명">
* **목록 조회:** 현재 등록된 모든 퀴즈의 타이틀을 확인합니다.
<img src="./screenshot/퀴즈 목록.png" width="300px" alt="설명">
* **최고 점수 추적:** 파일 시스템에 기록된 최고 점수를 확인하고 갱신 시 업데이트합니다.
<img src="./screenshot/점수 확인.png" width="300px" alt="설명">
* **안전한 입출력 관리:** 커스텀 `menu_input_handler`를 통해 잘못된 입력이나 강제 종료 시에도 우아한(Graceful) 처리를 지원합니다.
<img src="./screenshot/예외 처리1.png" width="300px" alt="설명">
<img src="./screenshot/예외 처리2.png" width="300px" alt="설명">

---

## 3. 파일 구조

모듈 간 결합도를 낮추기 위해 다음과 같이 기능을 분리했습니다.

```text
.
├── main.py             # Entry Point (QuizGame 클래스 및 메인 루프)
├── quiz.py             # Data Models (Dataclass를 활용한 데이터 구조 정의)
├── json_util.py        # Persistence Layer (JSON Load/Save 유틸리티)
├── contexts.py         # Infrastructure (Context Manager 기반 예외 처리)
└── state.json          # Database (퀴즈 데이터 및 상태 기록용 JSON)