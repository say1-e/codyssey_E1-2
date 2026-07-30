class QuizGame : # class = 설계도
    def __init__(self) : # 생성자 - 객체 생성 시 자동 실행 메서드 / self라는 변수에 현재 객체 자기 자신에 대한 참조가 들어옴
        self.quizzes = []
        self.best_score =0

    def show_menu(self) : # 일반 함수 - 객체의 행동
        print ("=" * 40)
        print("🎯 나만의 퀴즈 게임 🎯")
        print ("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print ("=" * 40)


def main():
    game = QuizGame() # 클래스라는 설계도로 객체 생성
    game.show_menu()

"""
__name__ : 파이썬 실행 시 현재 모듈(파이썬 파일)의 이름을 자동으로 담아주는 내장 변수
    직접 실행된 파일의 __name__ = "__main__"
    다른 파일에서 import 됐을 때의 __name__ = [해당 모듈 이름]
"""

# 진입점 Entry Point
# 이 파일이 직접 실행됐을 때에만 main() 실행 -> import된 다른 코드들까지 멋대로 실행되는 것 방지
if __name__ == "__main__": 
    main()

