import tkinter as tk


class Calculator:
    def _init_(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")

    def run(self) -> object:
        self.window.mainloop()

if tk == "_main_":
    calc = Calculator()
    calc.run()
