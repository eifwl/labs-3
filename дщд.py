from tkinter import *


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times, serif", 58, "bold"), bg="#369", foreground="#FCF")

        self.lbl.place(x=20, y=50)

        btns = [
            "C", "DEL", "*", "=",
            "one", "two", "three", "/",
            "four", "five", "six", "+",
            "seven", "eight", "nine", "-",
            "(", "0", ")", "X^2"
        ]

        x = 10
        y = 140

        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#FCC",
                   font=("SketchItalic", 30),
                   command=com).place(x=x, y=y,
                                      width=116,
                                      height=90)
            x += 117
            if x > 400:
                x = 10
                y += 81

    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "X^2":
            self.formula = str((eval(self.formula))**2)
        elif operation == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#098"
    root.geometry("485x560+250+250")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()



