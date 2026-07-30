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

    def get_number_input(self, message, min_value, max_value):
        while True:
            user_input = input(message).strip() # .strip() = 문자열의 양 끝에 있는 공백, 지정한 문자 제거 메소드

            if user_input == "":
                print("값을 입력해주세요.")
                continue

            """
            try - except 구문
                try = 오류날 수 있는 코드 실행
                except [에러] = 특정 에러 발생 시 실행
                continue = 현재 반복 중단 후 while 처음으로 돌아감 
            """
            try:
                number = int(user_input)
            except ValueError: 
                print("숫자를 입력해주세요.")
                continue

            if number < min_value or number > max_value:
                print(f"{min_value}~{max_value} 사이의 숫자를 입력해주세요.")
                continue

            return number

    def run(self):
        while True:
            self.show_menu()

            choice = self.get_number_input("선택: ", 1, 5)

            if choice == 1:
                print("퀴즈 풀기를 선택했습니다.")
            elif choice == 2:
                print("퀴즈 추가를 선택했습니다.")
            elif choice == 3:
                print("퀴즈 목록을 선택했습니다.")
            elif choice == 4:
                print("점수 확인을 선택했습니다.")
            elif choice == 5:
                print("게임을 종료합니다.")
                break

            else:
                print("잘못된 입력입니다.")


def main():
    game = QuizGame() # 클래스라는 설계도로 객체 생성
    game.run()

"""
__name__ : 파이썬 실행 시 현재 모듈(파이썬 파일)의 이름을 자동으로 담아주는 내장 변수
    직접 실행된 파일의 __name__ = "__main__"
    다른 파일에서 import 됐을 때의 __name__ = [해당 모듈 이름]
"""

# 진입점 Entry Point
# 이 파일이 직접 실행됐을 때에만 main() 실행 -> import된 다른 코드들까지 멋대로 실행되는 것 방지
if __name__ == "__main__": 
    main()

