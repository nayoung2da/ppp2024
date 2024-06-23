import tkinter as tk
from tkinter import simpledialog, messagebox, PhotoImage, Canvas, Button, Listbox, Scrollbar
import csv
import os
import random
from datetime import datetime
from PIL import ImageTk, Image

DB_FILE = "books.csv"
RECOMMENDED_BOOKS = [
    {"title": "이방인", "author": "알베르 까뮈"},
    {"title": "카라마조프의 형제들", "author": "도스토예프스키"},
    {"title": "부활", "author": "톨스토이"},
    {"title": "노인과 바다", "author": "헤밍웨이"},
    {"title": "변신", "author": "카프카"},
    {"title": "신곡", "author": "단테"},
    {"title": "돈키호테", "author": "세르반테스"},
    {"title": "레 미제라블", "author": "빅토르 위고"}
]

class OpeningWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("오프닝 창")
        self.root.geometry("594x750")
        self.root.resizable(width=False, height=False)

        # Canvas 생성
        self.canvas = tk.Canvas(root, width=594, height=614)
        self.canvas.pack()

        # 배경 이미지 로드
        self.image_path = "opening.jpg"  # 사용할 이미지 파일 경로
        self.butten_image_path = "opening_butten.jpg"  # 시작 버튼 이미지 파일 경로

        try:
            img = Image.open(self.image_path)
            img = img.resize((594, 614), Image.LANCZOS)  # 이미지 사이즈 조정 (LANCZOS 사용)
            self.img = ImageTk.PhotoImage(img)

            self.canvas.create_image(0, 0, anchor="nw", image=self.img)

            try:
                button_img = Image.open(self.butten_image_path)
                button_img = button_img.resize((240, 120), Image.LANCZOS)
                self.button_img = ImageTk.PhotoImage(button_img)
                start_button = tk.Button(self.root, image=self.button_img, command=self.open_main_window)
                start_button.pack(pady=10)

            except FileNotFoundError:
                messagebox.showerror("에러", "버튼 이미지를 찾을 수 없습니다.")
                self.root.destroy()  # 에러 발생 시 창 닫기

        except FileNotFoundError:
            messagebox.showerror("에러", "이미지를 찾을 수 없습니다.")
            self.root.destroy()  # 에러 발생 시 창 닫기

    def open_main_window(self):
        # 메인 창 열기
        self.root.destroy()  # 현재 창 닫기
        root = tk.Tk()  # 새로운 Tk 인스턴스 생성
        app = BookTrackerApp(root)
        root.mainloop()





class BookTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("하루라도 책을 읽지 않으면 입 안에 가시가 돋는다")
        self.root.geometry("594x614")

        self.books = self.load_books()

        # UI 구성 요소
        self.read_books_count_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.read_books_count_label.pack(pady=10)
        self.update_read_books_count()

        self.recommendation_label = tk.Label(self.root, text="📖오늘의 추천 책📖", font=("Arial", 14))
        self.recommendation_label.pack(pady=10)

        self.recommend_book = self.get_recommended_book()
        self.recommendation_text = tk.Label(self.root, text=self.recommend_book)
        self.recommendation_text.pack(pady=10)

        # Frame을 사용하여 리스트박스와 스크롤바를 하나의 묶음으로 만듭니다.
        frame = tk.Frame(self.root)
        frame.pack(pady=20, padx=10)

        # Listbox와 Scrollbar 생성
        self.book_listbox = Listbox(frame, height=15, width=60)
        self.book_listbox.pack(side="left")

        scrollbar = Scrollbar(frame, orient="vertical", command=self.book_listbox.yview)
        scrollbar.pack(side="right", fill="y")

        self.book_listbox.config(yscrollcommand=scrollbar.set)

        # 버튼 추가
        self.add_book_button = tk.Button(self.root, text="책 추가", command=self.add_book)
        self.add_book_button.pack(pady=5)

        self.update_status_button = tk.Button(self.root, text="상태 변경", command=self.update_status)
        self.update_status_button.pack(pady=5)

        self.add_review_button = tk.Button(self.root, text="리뷰 추가", command=self.add_review)
        self.add_review_button.pack(pady=5)

        self.view_review_button = tk.Button(self.root, text="리뷰 보기", command=self.view_review)
        self.view_review_button.pack(pady=5)

        self.remove_book_button = tk.Button(self.root, text="책 삭제", command=self.remove_book)
        self.remove_book_button.pack(pady=5)

        self.refresh_listbox()

    def load_books(self):
        books = []
        if os.path.exists(DB_FILE):
            with open(DB_FILE, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                books = [{'title': row[0], 'author': row[1], 'publisher': row[2], 'status': row[3], 'pages_read': row[4],
                           'review': row[5], 'rating': row[6], 'date_read': row[7]} for row in reader]
        return books

    def save_books(self):
        with open(DB_FILE, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            for book in self.books:
                writer.writerow([book['title'], book['author'], book['publisher'], book['status'], book['pages_read'],
                                 book['review'], book['rating'], book['date_read']])

    def refresh_listbox(self):
        self.book_listbox.delete(0, tk.END)
        for book in self.books:
            date_read = book['date_read'] if book['date_read'] else "읽은 날짜 없음"
            self.book_listbox.insert(tk.END, f"{book['title']} ({book['status']}) - {book['author']}"
                                             f" - {book['publisher']} - {date_read}")

    def update_read_books_count(self):
        read_books_count = sum(1 for book in self.books if book['status'] == "읽음")
        self.read_books_count_label.config(text=f"오늘까지 읽은 책 수: {read_books_count}")

    def get_recommended_book(self):
        recommended_book = random.choice(RECOMMENDED_BOOKS)
        return f"{recommended_book['title']} / {recommended_book['author']}"

    def add_book(self):
        title = simpledialog.askstring("책 추가", "책 제목을 입력하세요:")
        author = simpledialog.askstring("지은이 추가", "지은이 입력하세요:")
        publisher = simpledialog.askstring("출판사 추가", "출판사를 입력하세요:")
        status = "읽는 중"
        pages_read = "0"
        date_read = ""

        if title and author and publisher:
            if messagebox.askyesno("책 상태", "책을 다 읽으셨나요?"):
                status = "읽음"
                pages_read = ""
                date_read = datetime.now().strftime("%Y-%m-%d")
            else:
                pages_read = simpledialog.askstring("읽은 쪽수", "수고하셨어요!\n몇 쪽까지 읽으셨나요?", initialvalue="0")

            self.books.append({"title": title, "author": author, "publisher": publisher, "status": status, "pages_read": pages_read,
                               "review": "", "rating": "", "date_read": date_read})
            self.save_books()
            self.refresh_listbox()
            self.update_read_books_count()
        else:
            messagebox.showwarning("입력 오류", "모든 정보를 올바르게 입력하세요.")

    def update_status(self):
        try:
            selected_index = self.book_listbox.curselection()[0]
            current_status = self.books[selected_index]['status']
            if messagebox.askyesno("책 상태", "책을 다 읽으셨나요?"):
                new_status = "읽음"
                self.books[selected_index]['pages_read'] = ""
                self.books[selected_index]['date_read'] = datetime.now().strftime("%Y-%m-%d")
            else:
                new_status = "읽는 중"
                pages_read = simpledialog.askstring("읽은 쪽수", "수고하셨어요!\n몇 쪽까지 읽으셨나요?:",
                                                    initialvalue=self.books[selected_index]['pages_read'])
                self.books[selected_index]['pages_read'] = pages_read
                self.books[selected_index]['date_read'] = ""

            self.books[selected_index]['status'] = new_status
            self.save_books()
            self.refresh_listbox()
            self.update_read_books_count()
        except IndexError:
            messagebox.showwarning("선택 오류", "상태를 변경할 책을 선택하세요.")

    def add_review(self):
        try:
            selected_index = self.book_listbox.curselection()[0]
            current_review = self.books[selected_index]['review']
            review_window = tk.Toplevel(self.root)
            review_window.title("리뷰 추가")
            review_window.geometry('400x400')

            review_label = tk.Label(review_window, text="리뷰를 입력하세요:")
            review_label.pack(pady=10)
            review_text = tk.Text(review_window, height=10, width=40)
            review_text.pack()
            review_text.insert(tk.END, current_review)

            rating_label = tk.Label(review_window, text="별점을 선택하세요:")
            rating_label.pack(pady=10)
            rating_var = tk.IntVar()

            def set_rating(rating):
                rating_var.set(rating)
                review = review_text.get("1.0", tk.END).strip()
                self.books[selected_index]['review'] = review
                self.books[selected_index]['rating'] = rating
                self.save_books()
                review_window.destroy()

            stars_frame = tk.Frame(review_window)
            stars_frame.pack(pady=10)
            for i in range(1, 4):
                star_button = tk.Button(stars_frame, text="★" * i, command=lambda i=i: set_rating(i))
                star_button.pack(side=tk.LEFT, padx=5)

        except IndexError:
            messagebox.showwarning("선택 오류", "리뷰를 추가할 책을 선택하세요.")

    def view_review(self):
        try:
            selected_index = self.book_listbox.curselection()[0]
            book = self.books[selected_index]
            review_window = tk.Toplevel(self.root)
            review_window.title("리뷰 보기")
            review_window.geometry('400x400')

            title_label = tk.Label(review_window, text=f"제목: {book['title']}")
            title_label.pack(pady=5)
            author_label = tk.Label(riew_window, text=f"작가: {book['author']}")
            author_label.pack(pady=5)
            publisher_label = tk.Label(review_window, text=f"출판사: {book['publisher']}")
            publisher_label.pack(pady=5)
            status_label = tk.Label(review_window, text=f"상태: {book['status']}")
            status_label.pack(pady=5)
            if book['status'] == "읽는 중":
                pages_read_label = tk.Label(review_window, text=f"읽은 쪽수: {book['pages_read']}")
                pages_read_label.pack(pady=5)
            review_label = tk.Label(review_window, text="리뷰:")
            review_label.pack(pady=5)
            review_text = tk.Text(review_window, height=10, width=40)
            review_text.pack()
            review_text.insert(tk.END, book['review'])
            review_text.config(state=tk.DISABLED)

            rating_label = tk.Label(review_window, text=f"별점: {book['rating']}개")
            rating_label.pack(pady=5)

        except IndexError:
            messagebox.showwarning("선택 오류", "리뷰를 추가할 책을 선택하세요.")

    def view_review(self):
        try:
            selected_index = self.book_listbox.curselection()[0]
            book = self.books[selected_index]
            review_window = tk.Toplevel(self.root)
            review_window.title("리뷰 보기")
            review_window.geometry('400x400')

            title_label = tk.Label(review_window, text=f"제목: {book['title']}")
            title_label.pack(pady=5)
            author_label = tk.Label(review_window, text=f"작가: {book['author']}")
            author_label.pack(pady=5)
            publisher_label = tk.Label(review_window, text=f"출판사: {book['publisher']}")
            publisher_label.pack(pady=5)
            status_label = tk.Label(review_window, text=f"상태: {book['status']}")
            status_label.pack(pady=5)
            if book['status'] == "읽는 중":
                pages_read_label = tk.Label(review_window, text=f"읽은 쪽수: {book['pages_read']}")
                pages_read_label.pack(pady=5)
            review_label = tk.Label(review_window, text="리뷰:")
            review_label.pack(pady=5)
            review_text = tk.Text(review_window, height=10, width=40)
            review_text.pack()
            review_text.insert(tk.END, book['review'])
            review_text.config(state=tk.DISABLED)

            rating_label = tk.Label(review_window, text=f"별점: {book['rating']}개")
            rating_label.pack(pady=5)

        except IndexError:
            messagebox.showwarning("선택 오류", "리뷰를 볼 책을 선택하세요.")

    def remove_book(self):
        try:
            selected_index = self.book_listbox.curselection()[0]
            del self.books[selected_index]
            self.save_books()
            self.refresh_listbox()
        except IndexError:
            messagebox.showwarning("선택 오류", "삭제할 책을 선택하세요.")


def main():
    root = tk.Tk()
    opening_window = OpeningWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()