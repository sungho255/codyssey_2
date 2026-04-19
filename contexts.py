from contextlib import contextmanager
from json import JSONDecodeError

@contextmanager
def menu_input_handler():
    # ValueError: int() 변환 실패 - 공백 or 문자 or 기호, KeyboardInterrupt: Ctrl+C, EOFError: Ctrl+Z
    try:
        yield
    except (ValueError):
        print("잘못된 입력입니다. 다시 시도하세요.")
    except (KeyboardInterrupt, EOFError):
        print("\n잘못된 입력입니다. 다시 시도하세요.1")

@contextmanager
def load_file_handler(primary_path: str, fallback_path: str = "./state.json"):
    f = None
    try:
        # 1. 메인 경로 시도
        try:
            f = open(primary_path, 'r', encoding='utf-8')
            # 파일은 열었지만 내용이 비어있거나 문법이 틀린지 미리 체크 (Optional)
            yield f
        except (FileNotFoundError, JSONDecodeError):
            print("파일이 존재하지 않습니다. 기존 데이터가 생성됩니다.")
            if f: f.close()
            print(f"⚠️ {primary_path} 로드 실패. 백업 경로({fallback_path})를 시도합니다.")
            
            # 2. 백업 경로 시도
            f = open(fallback_path, 'r', encoding='utf-8')
            yield f
    except Exception as e:
        print("파일이 존재하지 않습니다. 기존 데이터가 생성됩니다.")