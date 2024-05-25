import time
import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
 return simpledialog.askstring(title="Test", prompt=text)
def main():
    count = int(gui_input("몇 초를 카운트하시겠습니까? : "))

    while True:
        print(f"카운트다운... {count}", end="\r")
        time.sleep(1)
        count -= 1
        if count <= 0:
            break

    print()
    print("펑~~")


if __name__ == "__main__":
    main()