import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Test", prompt=text)

def caesar_encode(text: str, shift: int = 3) -> str:
    encode_str = []
    for alphabet in text:
        if (65 <= ord(alphabet) and ord(alphabet) <= 90):
            x = chr((ord(alphabet) - 65 + shift) % 26 + 65)
            encode_str.append(x)

        elif (97 <= ord(alphabet) and ord(alphabet) <= 122):
            x = chr((ord(alphabet) - 97 + shift) % 26 + 97)
            encode_str.append(x)
        else:
            print("영어로 입력하세요.")

    return encode_str


def caesar_decode(text: str, shift: int = 3) -> str:
    decode_str = []
    for alphabet in text:
        if (65 <= ord(alphabet) and ord(alphabet) <= 90):
            x = chr((ord(alphabet) - 65 - shift) % 26 + 65)
            decode_str.append(x)
        elif (97 <= ord(alphabet) and ord(alphabet) <= 122):
            x = chr((ord(alphabet) - 97 - shift) % 26 + 97)
            decode_str.append(x)
        else:
            print("영어로 입력하세요.")

    return decode_str


def main():
    in_or_en = gui_input("인코딩과 디코딩 중 하고 싶은 것을 입력해주세요 : ")
    if in_or_en == "인코딩":
        sel_encode = gui_input("인코딩할 암호를 입력하세요 : ")
        print(''.join(caesar_encode(sel_encode)))
    elif in_or_en == "디코딩":
        sel_decode = gui_input("디코딩할 암호를 입력하세요. : ")
        caesar_decode(sel_decode)
        print(''.join(caesar_decode(sel_decode)))
    else:
        print("인코딩/디코딩 둘 중 하나를 정확하게 입력하세요.")


if __name__ == "__main__":
    main()