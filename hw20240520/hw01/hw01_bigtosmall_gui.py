import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Test", prompt=text)

def toggle_text(text: str):
    alphabet = []
    for gulja in text:
        if ord(gulja)>=ord('a') and ord(gulja)<=ord('z'):
            alphabet += chr( ord(gulja) + ord('A') - ord('a'))
        elif ord(gulja)>=ord('A') and ord(gulja)<=ord('Z'):
            alphabet += chr( ord(gulja) - ord('A') + ord('a') )
        else:
            print("영어 단어를 입력해주세요")
    return alphabet

def main():
    text = gui_input("대/소문자로 변경할 영어 단어를 입력해주세요(대문자->소문자/소문자->대문자) : ")
    print(''.join(toggle_text(text)))

if __name__ == "__main__":
    main()