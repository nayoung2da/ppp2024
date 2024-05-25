import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
 return simpledialog.askstring(title="Test", prompt=text)

def update_shown_answer_list(shown_answer, hidden_answer, x):
    for i in range(len(shown_answer)):
        if shown_answer[i] == "_" and x == hidden_answer[i]:
            shown_answer[i] = x
    return shown_answer

def main():
    hidden_answer = "apple"
    shown_answer = ["_" for x in range(len(hidden_answer))]
    trial = 3

    while True:
        x = gui_input(f"{' '.join(shown_answer)} / 목숨 : {trial} /  글자를 입력하시오=>?")
        if x in hidden_answer:
            shown_answer = update_shown_answer_list(shown_answer, hidden_answer, x)
        else:
            trial -= 1

        if "_" not in shown_answer:
            print("정답입니다.")
            break

        if trial <= 0:
            print("GAME OVER!")
            print(f"정답은 {hidden_answer}입니다.")
            break

if __name__ == "__main__":
    main()