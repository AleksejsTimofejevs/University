from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

# Проверка корректности введенных данных и запись в файл, если нужна
def clicked():
    try:
        if (txt.get() == '') | (time1.get() == '') | (time2.get() == ''):
            messagebox.showinfo('Ошибка', 'Заполните все поля')
        elif (int(time1.get()) in range(0, 24)) & (int(time2.get()) in range(0, 60)):
            if chk_state.get() == 1:
                res1 = "Событие: {}, {} в {}:{} успешно записано!".format(txt.get(), combo.get(), time1.get(), time2.get())
                lbl4.configure(text=res1)
                f1 = open("TimeTable.txt", 'w')
                f1.write(res)
                f1.close()
            else:
                res2 = "Событие: {}, {} в {}:{}".format(txt.get(), combo.get(), time1.get(),                                                          time2.get())
                lbl4.configure(text=res2)
        else:
            messagebox.showinfo('Ошибка', 'Введите корректное время!')
    except:
        None

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')

# Название
lbl1 = Label(window, text="Название события:", padx=10)
lbl1.place(x=0, y=0, width=140)
txt = Entry(window)
txt.place(x=140, y=0, width=100)

# Выбор дня
lbl2 = Label(window, text="Выбери день:", )
lbl2.place(x=0, y=25, width=140)
combo = Combobox(window)
combo['values'] = ('пн', 'вт', 'ср', 'чт', 'пт', "сб", 'вс')
combo.current(0)
combo.place(x=140, y=25, width=100)

# Выбор времени
lbl3 = Label(window, text="Выбери время:")
lbl3.place(x=0, y=50, width=140)

time1 = Entry(window)
time1.place(x=140, y=52, width=27, height=20)
time2 = Entry(window)
time2.place(x=170, y=52, width=27, height=20)

# Чекбокс на запись в файл
chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(window, text='Записать в файл', var=chk_state)
chk.place(x=0, y=75)

# Уведомление о записи
lbl4 = Label(window)
lbl4.place(x=0, y=175)

# Кнопка
btn = Button(window, text="Записать", command=clicked)
btn.place(x=150, y=200, width=100)

window.mainloop()


