class Quiz : 
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        print(self.question)

        for index, choice in enumerate(self.choices, start=1): # enumerate() 리스트 같은 순서 있는 자료형을 받아 인덱스와 값을 도잇에 함께 튜플 형태로 리턴해주는 내장 함수
            print(f"{index}. {choice}")

    def check_answer(self, user_answer):
        return self.answer == user_answer

    

class QuizGame : # class = 설계도
    def __init__(self) : # 생성자 - 객체 생성 시 자동 실행 메서드 / self라는 변수에 현재 객체 자기 자신에 대한 참조가 들어옴
        self.quizzes = self.create_default_quizzes()
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
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                print("퀴즈 목록을 선택했습니다.")
            elif choice == 4:
                print("점수 확인을 선택했습니다.")
            elif choice == 5:
                print("게임을 종료합니다.")
                break

            else:
                print("잘못된 입력입니다.")

    def create_default_quizzes(self):
        return [
            Quiz(
                "Python에서 문자열을 나타내는 자료형은?",
                ["int", "str", "bool", "list"],
                2
            ),
            Quiz(
                "Python에서 참과 거짓을 나타내는 자료형은?",
                ["str", "dict", "bool", "float"],
                3
            ),
            Quiz(
                "리스트를 만들 때 사용하는 기호는?",
                ["()", "{}", "[]", "<>"],
                3
            ),
            Quiz(
                "조건문을 작성할 때 사용하는 키워드는?",
                ["if", "for", "def", "class"],
                1
            ),
            Quiz(
                "함수를 정의할 때 사용하는 키워드는?",
                ["func", "function", "return", "def"],
                4
            ),
        ]

    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        correct_count = 0

        print()
        print(f"퀴즈를 시작합니다! 총 {len(self.quizzes)}문제")

        for index, quiz in enumerate(self.quizzes, start=1):
            print()
            print("-" * 40)
            print(f"[문제 {index}]")

            quiz.display()

            user_answer = self.get_number_input("정답 입력: ", 1, 4)

            if quiz.check_answer(user_answer):
                print("정답입니다!")
                correct_count += 1
            else :
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print()
        print("=" * 40)
        print(
            f"결과: {len(self.quizzes)}문제 중 "
            f"{correct_count}문제 정답"
        )
        print("=" * 40)

    def add_quiz(self):
        print()
        print("새로운 퀴즈를 추가합니다.")

        question = input("문제를 입력하세요.: ").strip()

        while question == "":
            print("문제를 비워둘 수 없습니다.")
            question = input("문제를 입력하세요.: ").strip()

        choices = []

        for number in range(1, 5):
            choice = input(f"선택지 {number}: ").strip()

            while choice == "":
                print("선택지를 비워둘 수 없습니다.")
                choice = input(f"선택지 {number}: ").strip()

            choices.append(choice)

        answer = self.get_number_input("정답 번호 (1~4): ", 1, 4)

        new_quiz = Quiz(question, choices, answer)

        self.quizzes.append(new_quiz)

        print("퀴즈가 추가되었습니다.")



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

