import this
from tkinter import Tk, Frame, Button, LEFT, messagebox


rot13 = str.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm",
)

def main_window(root: Tk) -> Frame:
    root.title("Simple Zen Button")
    root.geometry("300x200")
    root.resizable(False, False)
    frame = Frame(root)
    frame.pack()

    zen_btn = Button(frame, text="Python Zen", command=show_zen)
    zen_btn.pack(side=LEFT, padx=10, pady=10)
    return frame

def show_zen() -> None:
    messagebox.showinfo("Python Zen", this.s.translate(rot13))

if __name__ == "__main__":
    root = Tk()
    main_window(root)
    root.mainloop()
