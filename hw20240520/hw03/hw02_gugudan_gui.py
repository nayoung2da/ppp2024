import random
import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
 return simpledialog.askstring(title="Test", prompt=text)
def gugudan():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    result = num1 * num2
    return num1, num2, result


def main():
    questions = int(gui_input("구구단 퀴즈 몇 개를 푸시겠습니까? : "))
    correct_count = 0

    for _ in range(questions):
        num1, num2, correct_result = gugudan()
        user_result = int(gui_input(f"{num1} * {num2} = "))

        if correct_result == user_result:
            print("정답입니다.")
            correct_count += 1
        else:
            print("오답입니다.")

    print(f"총 {questions}문제 중 {correct_count}문제 맞췄습니다.")


if __name__ == "__main__":
    main()