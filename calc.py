from tkinter import *
from tkinter import messagebox
from tkinter import Menu
import random

m = ["#FCD975", "#5F9EA0", "#A52A2A", "#FFF8E7", "#FBEC5D", "#E6E6FA", "#DB7093"]


class Test():
    def __init__(self):
        self.window = Tk()
        self.window.title("Калькулятор")
        self.window.geometry('500x360+700+300')
        self.window.resizable(False, False)
        t = "Простой калькулятор"
        t_font = ("Comic Sans MS", 20)
        self.lbl = Label(self.window, text=t, font=t_font)
        self.lbl.pack(side=TOP)
        # радиобатон
        self.lbl3 = Label(self.window, text="Режимы", font=("Comic Sans MS", 17))
        self.lbl3.place(x=0, y=80)
        self.r_var = BooleanVar()
        self.r_var.set(0)
        self.b1 = Radiobutton(self.window, text="Калькулятор", variable=self.r_var, value=0, background="light blue")
        self.b1.place(x=0, y=120)
        self.b2 = Radiobutton(self.window, text="Прямоугольник", variable=self.r_var, value=1, background="light blue")
        self.b2.place(x=0, y=150)
        # вход, операции
        self.Operations = Label(self.window, text="Операции с числами", font=("Comic Sans MS", 18))
        self.Operations.place(x=250, y=200)
        self.INPUT = Label(self.window, text="Входные данные", font=("Comic Sans MS", 18))
        self.INPUT.place(x=0, y=200)
        t1 = "Введите первое значение"
        t2 = "Введите второе значение"
        self.lbl1 = Label(self.window, text=t1, bg="#FBCEB1", relief=RIDGE, font=("Comic Sans MS", 10))
        self.lbl1.place(x=0, y=250)
        self.lbl2 = Label(self.window, text=t2, bg="#FBCEB1", relief=RIDGE, font=("Comic Sans MS", 10))
        self.lbl2.place(x=0, y=300)
        self.txt = Entry(self.window)
        self.txt.place(x=170, y=250, width=50, height=24)
        self.txt1 = Entry(self.window)
        self.txt1.place(x=170, y=300, width=50, height=24)

        # операции
        self.b_plus = Button(self.window, text="+", width=8, height=2, font=("Comic Sans MS", 10),
                             command=self.plus, activebackground="#FAF0E6").place(x=250, y=240)
        self.b_munis = Button(self.window, text="-", width=8, height=2, font=("Comic Sans MS", 10),
                              command=self.minus, activebackground="#FAF0E6").place(
            x=250, y=291)
        self.b_proiz = Button(self.window, text="*", width=8, height=2, font=("Comic Sans MS", 10),
                              command=self.pr, activebackground="#FAF0E6").place(
            x=335, y=240)
        self.b_del = Button(self.window, text="/", width=8, height=2, font=("Comic Sans MS", 10),
                            command=self.Del, activebackground="#FAF0E6").place(x=335,
                                                                                y=291)
        self.b_Per = Button(self.window, text="Perimeter", width=8, height=2, font=("Comic Sans MS", 10),
                            command=self.Per, activebackground="#FAF0E6").place(x=420, y=240)
        self.b_Square = Button(self.window, text="Square", width=8, height=2, font=("Comic Sans MS", 10),
                               command=self.Square, activebackground="#FAF0E6").place(x=420, y=290)
        # кнопки change, clear, exit
        self.exit = Button(self.window, text="Выход", width=7, height=1, font=("Comic Sans MS", 10),
                           command=self.exit, activebackground='#0095B6').place(x=432, y=0)
        self.clear = Button(self.window, text="Clear", width=6, height=1, font=("Comic Sans MS", 10),
                            command=self.clear_all, activebackground="#A2ADD0").place(x=1, y=326)
        self.change = Button(self.window, text="Change", width=6, height=1, font=("Comic Sans MS", 10),
                             command=self.change_values, activebackground="#F3A505").place(x=100, y=326)
        # Результат
        self.res = Label(self.window, text="Результат", width=10, height=1, font=("Comic Sans MS", 20))
        self.res.place(x=175, y=60)
        self.answer = Label(self.window, text="", width=15, height=1, bg="#FFDEAD", relief=RAISED,
                            font=("Comic Sans MS", 10))
        self.answer.place(x=195, y=100)
        # Меню
        self.mainmenu = Menu(self.window)
        self.filemenu = Menu(self.mainmenu, tearoff=0)
        self.filemenu.add_command(label="Автор", command=self.OpenInfo)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Выход', command=self.window.destroy)
        self.mainmenu.add_cascade(label="Файл", menu=self.filemenu)
        self.window.config(menu=self.mainmenu)
        self.window.mainloop()

    # логика кнопок
    def OpenInfo(self):
        root = Tk()
        root.geometry("360x100+770+420")
        root.resizable(False, False)
        label1 = Label(root, text="Создатель - Ледванов Вадим", font=("Comic Sans MS", 15))
        label1.pack(side=TOP)
        btn1 = Button(root, text="Закрыть", font=("Comic Sans MS", 10),
                      command=root.destroy)
        btn1.pack(side=BOTTOM)

        root.mainloop()

    def Square(self):
        try:
            a = int(self.txt.get())
            b = int(self.txt1.get())
            if self.r_var.get() == 1:
                if a > 0 and b > 0:
                    self.answer['text'] = str(a * b)
                    self.answer['bg'] = random.choice(m)
                else:
                    self.error2()
            else:
                self.error4()
        except:
            self.error()

    def Per(self):
        try:
            a = int(self.txt.get())
            b = int(self.txt1.get())
            if self.r_var.get() == 1:
                if a > 0 and b > 0:
                    self.answer['text'] = str(2 * (a + b))
                    self.answer['bg'] = random.choice(m)
                else:
                    self.error2()
            else:
                self.error4()
        except:
            self.error()

    def exit(self):
        self.window.destroy()

    def clear_all(self):
        self.txt.delete(0, END)
        self.txt1.delete(0, END)
        self.answer['text'] = ''

    def change_values(self):
        a = self.txt.get()
        b = self.txt1.get()
        self.clear_all()
        self.txt.insert(0, b)
        self.txt1.insert(0, a)

    def plus(self):
        try:
            a = int(self.txt.get())
            b = int(self.txt1.get())
            if self.r_var.get() == 0:
                self.answer['text'] = str(a + b)
                self.answer['bg'] = random.choice(m)
            else:
                self.error3()
        except:
            self.error()

    def minus(self):
        try:
            a = int(self.txt.get())
            b = int(self.txt1.get())
            if self.r_var.get() == 0:
                self.answer['text'] = str(a - b)
                self.answer['bg'] = random.choice(m)
            else:
                self.error3()
        except:
            self.error()

    def pr(self):
        try:
            a = int(self.txt.get())
            b = int(self.txt1.get())
            if self.r_var.get() == 0:
                self.answer['text'] = str(a * b)
                self.answer['bg'] = random.choice(m)
            else:
                self.error3()
        except:
            self.error()

    def Del(self):
        try:
            a = int(self.txt.get())
            b = int(self.txt1.get())
            if self.r_var.get() == 0:
                self.answer['text'] = str(round(a / b, 5))
                self.answer['bg'] = random.choice(m)
            else:
                self.error3()
        except:
            self.error()

    def error(self):
        messagebox.showinfo("Ошибка", "Неверный ввод данных")

    def error2(self):
        messagebox.showinfo("Ошибка", "Стороны прямоугольника должны быть положительными")

    def error3(self):
        messagebox.showinfo("Ошибка", "Нельзя выполнить данную операцию в режиме Прямоугольник")

    def error4(self):
        messagebox.showinfo("Ошибка", "Нельзая выполнить данную операцию в режиме Калькулятор")


app = Test()
