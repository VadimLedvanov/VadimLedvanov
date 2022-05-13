import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

con = sqlite3.connect("gruz.bd")


# БАЗА ДАННЫХ
class BusyBases:
    def create_busyBD(self):
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS busy_transport(
                    ID int PRIMARY KEY,
                    Тип text, 
                    Грузоподъёмность real, 
                    Длина real,
                    Ширина real,
                    Высота real   
                    )''')
        con.commit()

    def Insert_busy(self, request):
        cur = con.cursor()
        info = request
        cur.executemany("INSERT INTO busy_transport VALUES (?, ?, ?, ?, ?, ?)", info)
        con.commit()


class FreeBases:
    def create_freeBD(self):
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS free_transport(
                    ID int PRIMARY KEY,
                    Тип text, 
                    Грузоподъёмность real, 
                    Длина real,
                    Ширина real,
                    Высота real   
                    )''')
        con.commit()

    def Insert_free(self, id, name, m, l, w, h):
        cur = con.cursor()
        info = [(id, name, m, l, w, h)]
        cur.executemany("INSERT INTO free_transport VALUES (?, ?, ?, ?, ?, ?)", info)
        con.commit()

    def delete_from_Free(self, id):
        cur = con.cursor()
        cur.execute(f"DELETE FROM free_transport WHERE ID={id}")


class DataBases:
    def create_bd(self):
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transport(
                    ID int PRIMARY KEY,
                    Тип text, 
                    Грузоподъёмность real, 
                    Длина real,
                    Ширина real,
                    Высота real   
                    )''')
        con.commit()

    def Insert(self, id, name, m, l, w, h):
        cur = con.cursor()
        info = [(id, name, m, l, w, h)]
        cur.executemany("INSERT INTO transport VALUES (?, ?, ?, ?, ?, ?)", info)
        con.commit()


# main menu
class W(DataBases, FreeBases, BusyBases):
    def __init__(self):
        self.window = Tk()
        self.window.geometry("350x215+1350+400")
        self.window.title("Приложение")
        self.window.resizable(False, False)

        # КНОПКИ
        self.b1 = Button(self.window, text="Просмотреть весь доступный транспорт",
                         width=40, relief=RAISED, command=self.check,
                         activebackground="#778899").pack(side=TOP)

        self.b2 = Button(self.window, text="Просмотреть транспорт по грузоподъёмности",
                         relief=RAISED, width=40, command=self.check_gruz,
                         activebackground="#778899").pack(side=TOP)

        self.b3 = Button(self.window, text="Просмотреть свободный транспорт",
                         relief=RAISED, width=40, command=self.check_free,
                         activebackground="#778899").pack(side=TOP)

        self.b4 = Button(self.window, text="Просмотреть занятый транспорт",
                         relief=RAISED, width=40, command=self.check_busy,
                         activebackground="#778899").pack(side=TOP)

        self.b5 = Button(self.window, text="Добавить грузовой транспорт",
                         relief=RAISED, width=40, command=self.add,
                         activebackground="#778899").pack(side=TOP)

        self.b6 = Button(self.window, text="Удалить грузовой транспорт",
                         relief=RAISED, width=40, command=self.delete,
                         activebackground="#778899").pack(side=TOP)
        self.b7 = Button(self.window, text="Подобрать транспорт", relief=RAISED, width=40,
                         command=self.find_tr, activebackground="#778899").pack(side=TOP)

        self.b8 = Button(self.window, text="Внести заявку по габаритам", relief=RAISED, width=40,
                         command=self.application, activebackground="#778899").pack(side=TOP)

        self.window.mainloop()

    # ЛОГИКА КНОПОК
    def application(self):
        window = W8()

    def check_busy(self):
        window = W7()

    def check_free(self):
        window6 = W6()

    def find_tr(self):
        window5 = W5()

    def check_gruz(self):
        window4 = W4()

    def check(self):
        window2 = W2()

    def add(self):
        window1 = W1()

    def delete(self):
        window3 = W3()


# Подбор груза по габаритам
class W9(FreeBases, BusyBases):
    def __init__(self, information):
        self.info = information
        self.window9 = Tk()
        self.window9.geometry("880x500+700+400")
        self.window9.resizable(0, 0)

        self.heads = ["ID", "Тип", "Грузоподъёмность, тонн", "Длина", "Ширина", "Высота"]

        self.table = ttk.Treeview(self.window9, show='headings')
        self.table['column'] = self.heads

        for header in self.heads:
            self.table.heading(header, text=header, anchor='center')
            self.table.column(header, anchor='center', width=2)

        for row in self.info:
            self.table.insert('', 'end', values=row)

        self.scroll_plane = ttk.Scrollbar(self.window9, command=self.table.yview)
        self.scroll_plane.pack(side=RIGHT, fill=Y)
        self.table.config(yscroll=self.scroll_plane.set)

        self.label1 = Label(self.window9, text="По указанным габаритам вам подходят слудующие грузы",
                            font=("Outreque", 15))
        self.label1.pack(side=TOP)

        self.table.pack(expand=YES, fill=BOTH)
        self.label2 = Label(self.window9, text="Введите ID груза, который хотите забронировать",
                            font=("Outreque", 10))
        self.label2.pack(side=TOP)
        self.entry1 = Entry(self.window9, width=10)
        self.entry1.pack(side=TOP)
        self.b1 = Button(self.window9, text="Забронировать", activebackground="#A0522D",
                         command=self.get_gruz).pack(side=BOTTOM)
        self.b2 = Button(self.window9, text="Закрыть", activebackground="#66A5AD",
                         command=self.window9.destroy).place(x=805, y=475)
        self.window9.mainloop()

    def get_gruz(self):
        try:
            id = int(self.entry1.get())
            f = 0
            if id > 0:
                for el in self.info:
                    if el[0] == id:
                        self.delete_from_Free(id)
                        self.Insert_busy([el])
                        f = 1
                        break
                if f == 0:
                    messagebox.showerror("Ошибка", "Такого ID не существует!")
                else:
                    messagebox.showinfo("Готово", "Транспорт успешно забронирован")
                    self.window9.destroy()
            else:
                messagebox.showerror("Ошибка", "Такого ID не существует!")
        except:
            messagebox.showerror("Ошибка", "Неверный ввод данных!")


# Внести заявку по габаритам
class W8(FreeBases):
    def __init__(self):
        self.window8 = Tk()
        self.window8.title("Заявка на транспорт")
        self.window8.geometry("200x100+1000+400")
        self.window8.resizable(0, 0)
        # Длина
        self.label2 = Label(self.window8, text="Длина, м")
        self.label2.grid(row=1, column=0)
        self.entry2 = Entry(self.window8)
        self.entry2.grid(row=1, column=1)
        # Ширина
        self.label3 = Label(self.window8, text="Ширина, м")
        self.label3.grid(row=2, column=0)
        self.entry3 = Entry(self.window8)
        self.entry3.grid(row=2, column=1)
        # Высота
        self.label4 = Label(self.window8, text="Высота, м")
        self.label4.grid(row=3, column=0)
        self.entry4 = Entry(self.window8)
        self.entry4.grid(row=3, column=1)

        self.b1 = Button(self.window8, text="Подобрать груз", activebackground="#E1B16A",
                         command=self.find_tr).place(x=55, y=70)

        self.window8.mainloop()

    def find_tr(self):
        try:
            l = float(self.entry2.get())
            w = float(self.entry3.get())
            h = float(self.entry4.get())
            if l > 0 and w > 0 and h > 0:
                V = l * w * h
                info = []
                c = con.cursor()
                sql = "SELECT * FROM free_transport"
                m = c.execute(sql).fetchall()
                for el in m:
                    V_cur = el[3] * el[4] * el[5]
                    if V_cur >= V:
                        info.append(el)
                self.window8.destroy()
                window9 = W9(info)
            else:
                messagebox.showerror("Ошибка", "Параметры должны быть положительными!")
        except:
            messagebox.showerror("Ошибка", "Неверный ввод данных")


# Посмотреть занятый транспорт
class W7(BusyBases):
    def __init__(self):
        self.window7 = Tk()
        self.window7.geometry("880x500+700+400")
        self.window7.resizable(0, 0)

        self.heads = ["ID", "Тип", "Грузоподъёмность, тонн", "Длина", "Ширина", "Высота"]
        sql = "SELECT * from busy_transport"
        c = con.cursor()
        q = c.execute(sql).fetchall()
        self.lst = []
        for i in q:
            self.lst.append(i)

        self.table = ttk.Treeview(self.window7, show='headings')
        self.table['column'] = self.heads

        for header in self.heads:
            self.table.heading(header, text=header, anchor='center')
            self.table.column(header, anchor='center', width=2)

        for row in self.lst:
            self.table.insert('', 'end', values=row)

        self.scroll_plane = ttk.Scrollbar(self.window7, command=self.table.yview)
        self.scroll_plane.pack(side=RIGHT, fill=Y)
        self.table.config(yscroll=self.scroll_plane.set)

        self.table.pack(expand=YES, fill=BOTH)
        self.b1 = Button(self.window7, text="Закрыть", activebackground="#A0522D",
                         command=self.window7.destroy).pack(side=TOP)
        self.window7.mainloop()


# Посмотреть свободный транспорт
class W6(FreeBases):
    def __init__(self):
        self.window6 = Tk()
        self.window6.geometry("880x500+700+400")
        self.window6.resizable(0, 0)

        self.heads = ["ID", "Тип", "Грузоподъёмность, тонн", "Длина", "Ширина", "Высота"]
        sql = "SELECT * from free_transport"
        c = con.cursor()
        q = c.execute(sql).fetchall()
        self.lst = []
        for i in q:
            self.lst.append(i)

        self.table = ttk.Treeview(self.window6, show='headings')
        self.table['column'] = self.heads

        for header in self.heads:
            self.table.heading(header, text=header, anchor='center')
            self.table.column(header, anchor='center', width=2)

        for row in self.lst:
            self.table.insert('', 'end', values=row)

        self.scroll_plane = ttk.Scrollbar(self.window6, command=self.table.yview)
        self.scroll_plane.pack(side=RIGHT, fill=Y)
        self.table.config(yscroll=self.scroll_plane.set)

        self.table.pack(expand=YES, fill=BOTH)
        self.b1 = Button(self.window6, text="Закрыть", activebackground="#A0522D",
                         command=self.window6.destroy).pack(side=TOP)
        self.window6.mainloop()


# Подбор транспорта
class W5(FreeBases, BusyBases):
    def __init__(self):
        self.window5 = Tk()
        self.window5.title("Подбор груза")
        self.window5.geometry("300x75+1000+500")
        self.window5.resizable(0, 0)
        self.label1 = Label(self.window5, text="Введите ID груза, который хотите забронировать")
        self.label1.pack(side=TOP)
        self.entry1 = Entry(self.window5)
        self.entry1.pack(side=TOP)
        self.b1 = Button(self.window5, text="Забронировать", activebackground="#FAB352",
                         command=self.get_gruz).pack(side=BOTTOM)
        self.window5.mainloop()

    def get_gruz(self):
        try:
            id = int(self.entry1.get())
            sql = f"SELECT * from free_transport WHERE ID={id}"
            c = con.cursor()
            request = c.execute(sql).fetchall()
            if len(request) == 0:
                sql_from_busy = f"SELECT * from busy_transport WHERE ID={id}"
                if len(c.execute(sql_from_busy).fetchall()) == 0:
                    messagebox.showerror("Ошибка", "Груза с таким ID не существует")
                else:
                    messagebox.showerror("Ошибка", "Груз с таким ID уже забронирован")
            else:
                self.Insert_busy(request)
                self.delete_from_Free(id)
                messagebox.showinfo("Инфо", "Вы успешно забронировали груз")
                self.window5.destroy()
        except:
            messagebox.showerror("Ошибка", "Неверный ввод данных")


# Удалить
class W3(DataBases, FreeBases, BusyBases):
    def __init__(self):
        self.window3 = Tk()
        self.window3.geometry("300x100+1000+500")
        self.label1 = Label(self.window3, text="Введите ID транспорта, который хотите удалить")
        self.label1.pack(side=TOP)
        self.entry1 = Entry(self.window3)
        self.entry1.pack(side=TOP)
        self.b1 = Button(self.window3, text="Удалить", activebackground="#87CEFA",
                         command=self.delete_from_bd).pack(side=TOP)

        self.window3.mainloop()

    def delete_from_bd(self):
        try:
            id = int(self.entry1.get())
            if id > 0:
                sql = f"DELETE FROM transport WHERE ID={id}"
                c = con.cursor()
                sql2 = f"SELECT * FROM transport WHERE ID={id}"
                if len(c.execute(sql2).fetchall()) == 0:
                    messagebox.showerror("Ошибка", "Такого ID не существует")
                else:
                    sql_free_baza = f"SELECT * FROM free_transport WHERE ID={id}"
                    sql_busy_baza = f"SELECT * FROM busy_trasport WHERE ID={id}"
                    if len(c.execute(sql_free_baza).fetchall()) != 0:
                        deleting1 = f"DELETE FROM free_transport WHERE ID={id}"
                        c.execute(deleting1)
                    else:
                        deleting2 = f"DELETE FROM busy_transport WHERE ID={id}"
                        c.execute(deleting2)
                    c.execute(sql)
                    con.commit()
                    messagebox.showinfo("Удаление", "Объект удален из базы данных")
                    self.window3.destroy()
            else:
                messagebox.showerror("Ошибка", "ID не может быть отрицательным!")
        except:
            messagebox.showerror("Ошибка", "Такого ID не существует")


# Транспорт по грузоподъёмности
class W4(FreeBases):
    def __init__(self):
        self.window2 = Tk()
        self.window2.geometry("880x500+700+400")
        self.window2.resizable(0, 0)

        self.heads = ["ID", "Тип", "Грузоподъёмность, тонн"]
        sql = "SELECT * from free_transport"
        c = con.cursor()
        q = c.execute(sql).fetchall()
        self.lst = []
        for i in q:
            self.lst.append(i)

        self.table = ttk.Treeview(self.window2, show='headings')
        self.table['column'] = self.heads

        for header in self.heads:
            self.table.heading(header, text=header, anchor='center')
            self.table.column(header, anchor='center', width=2)

        for row in self.lst:
            self.table.insert('', 'end', values=row)

        self.scroll_plane = ttk.Scrollbar(self.window2, command=self.table.yview)
        self.scroll_plane.pack(side=RIGHT, fill=Y)
        self.table.config(yscroll=self.scroll_plane.set)

        self.table.pack(expand=YES, fill=BOTH)
        self.b1 = Button(self.window2, text="Закрыть", activebackground="#A0522D",
                         command=self.window2.destroy).pack(side=TOP)
        self.window2.mainloop()


# Весь транспорт
class W2(DataBases):
    def __init__(self):
        self.window2 = Tk()
        self.window2.geometry("880x500+700+400")
        self.window2.resizable(0, 0)

        self.heads = ["ID", "Тип", "Грузоподъёмность, тонн", "Длина", "Ширина", "Высота"]
        sql = "SELECT * from transport"
        c = con.cursor()
        q = c.execute(sql).fetchall()
        self.lst = []
        for i in q:
            self.lst.append(i)

        self.table = ttk.Treeview(self.window2, show='headings')
        self.table['column'] = self.heads

        for header in self.heads:
            self.table.heading(header, text=header, anchor='center')
            self.table.column(header, anchor='center', width=2)

        for row in self.lst:
            self.table.insert('', 'end', values=row)

        self.scroll_plane = ttk.Scrollbar(self.window2, command=self.table.yview)
        self.scroll_plane.pack(side=RIGHT, fill=Y)
        self.table.config(yscroll=self.scroll_plane.set)

        self.table.pack(expand=YES, fill=BOTH)
        self.b1 = Button(self.window2, text="Закрыть", activebackground="#A0522D",
                         command=self.window2.destroy).pack(side=TOP)
        self.window2.mainloop()


# Добавить новый транспорт
class W1(DataBases, FreeBases):
    def __init__(self):
        self.window1 = Tk()
        self.window1.geometry("230x160+1350+400")
        self.window1.resizable(0, 0)
        self.label0 = Label(self.window1, text="ID")
        self.label0.grid(row=0, column=0)
        self.entry0 = Entry(self.window1, width=10)
        self.entry0.grid(row=0, column=1)
        # ТИП
        self.label1 = Label(self.window1, text="Тип")
        self.label1.grid(row=1, column=0)
        self.entry1 = Entry(self.window1, width=10)
        self.entry1.grid(row=1, column=1)
        # Грузоподъёмность, тонн
        self.label2 = Label(self.window1, text="Грузоподъёмность, тонн")
        self.label2.grid(row=2, column=0)
        self.entry2 = Entry(self.window1, width=10)
        self.entry2.grid(row=2, column=1)
        # ДЛИНА
        self.label3 = Label(self.window1, text="Длина")
        self.label3.grid(row=3, column=0)
        self.entry3 = Entry(self.window1, width=10)
        self.entry3.grid(row=3, column=1)
        # ШИРИНА
        self.label4 = Label(self.window1, text="Ширина")
        self.label4.grid(row=4, column=0)
        self.entry4 = Entry(self.window1, width=10)
        self.entry4.grid(row=4, column=1)
        # ВЫСОТА
        self.label5 = Label(self.window1, text="Высота")
        self.label5.grid(row=5, column=0)
        self.entry5 = Entry(self.window1, width=10)
        self.entry5.grid(row=5, column=1)
        self.b1 = Button(self.window1, text="Добавить", activebackground="#98FB98",
                         command=self.input_info).place(x=160, y=130)
        self.window1.call('wm', 'attributes', '.', '-topmost', '1')
        self.window1.mainloop()

    def input_info(self):
        try:
            if not str(self.entry1.get()).isdigit():
                a1 = self.entry1.get()
            a0 = int(self.entry0.get())
            a2 = float(self.entry2.get())
            a3 = float(self.entry3.get())
            a4 = float(self.entry4.get())
            a5 = float(self.entry5.get())
            if a2 > 0 and a3 > 0 and a4 > 0 and a5 > 0 and a0 > 0:
                self.Insert(a0, a1, a2, a3, a4, a5)
                self.Insert_free(a0, a1, a2, a3, a4, a5)
                messagebox.showinfo("Добавление в БД", "Транспорт был успешно добавлен")
                self.window1.destroy()
            else:
                messagebox.showerror("Ошибка", "Неверный ввод данных")
        except:
            messagebox.showerror("Ошибка", "Неверный ввод данных")


if __name__ == "__main__":
    c = con.cursor()
    DB = DataBases()
    DB.create_bd()
    FreDB = FreeBases()
    FreDB.create_freeBD()
    BusyDB = BusyBases()
    BusyDB.create_busyBD()
    App = W()
