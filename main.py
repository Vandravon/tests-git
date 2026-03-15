import tkinter as tk

from login_app import LoginApp


def main():
    root = tk.Tk()
    LoginApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
