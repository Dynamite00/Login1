import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Login App")  # 앱 제목

        # 로그인 아이디 라벨 및 항목
        self.id_label = tk.Label(master, text="ID:")
        self.id_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.id_entry = tk.Entry(master)
        self.id_entry.grid(row=0, column=1, padx=10, pady=5)

        # 로그인 패스워드 라벨 및 항목
        self.password_label = tk.Label(master, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        # 로그인 버튼
        self.login_button = tk.Button(master, text="로그인", command=self.login)
        self.login_button.grid(row=2, column=0, padx=5, pady=10)

        # 회원가입 버튼
        self.signup_button = tk.Button(master, text="회원가입", command=self.signup)
        self.signup_button.grid(row=2, column=1, padx=5, pady=10)

        # 사용자 자격 증명을 저장, 사용자 아이디와 패스워드
        self.users = {}

    def login(self):
        # 입력한 아이디와 패스워드
        entered_id = self.id_entry.get()
        entered_password = self.password_entry.get()

        # 아이디와 패스워드가 일치하는지 확인
        if entered_id in self.users and self.users[entered_id] == entered_password:
            messagebox.showinfo("Login Successful", f"환영합니다, {entered_id}님!")
        else:
            messagebox.showerror("Login Failed", "아이디 또는 비밀번호가 잘못되었습니다. 다시 시도해 주세요.")

    def signup(self):
        # 회원가입을 위한 새 창
        signup_window = tk.Toplevel(self.master)
        signup_window.title("Signup")

        # 회원가입 아이디 라벨 및 항목
        id_label = tk.Label(signup_window, text="New ID:")
        id_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        id_entry = tk.Entry(signup_window)
        id_entry.grid(row=0, column=1, padx=10, pady=5)

        # 회원가입 패스워드 라벨 및 항목
        password_label = tk.Label(signup_window, text="New Password:")
        password_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        password_entry = tk.Entry(signup_window, show="*")
        password_entry.grid(row=1, column=1, padx=10, pady=5)

        # 회원가입 버튼
        signup_button = tk.Button(signup_window, text="Create Account", command=lambda: self.create_account(signup_window, id_entry.get(), password_entry.get()))
        signup_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def create_account(self, window, new_id, new_password):
        if new_id not in self.users:
            self.users[new_id] = new_password
            messagebox.showinfo("Account Created", f"새 계정이 생성되었습니다. '{new_id}'")
            window.destroy()
        else:
            messagebox.showerror("Error", "사용자 ID가 이미 존재합니다. 다른 아이디를 선택해주세요.")

def main():
    root = tk.Tk()
    root.title("Login App")
    root.geometry("250x120")  # 앱의 창 크기 설정
    root.resizable(False, False)  # 앱의 창 크기 조절 비활성화
    app = LoginApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


#     앱 창 크기 조절 가능
#     def main():
#     root = tk.Tk()
#     app = LoginApp(root)
#     root.mainloop()