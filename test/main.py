from tkinter import *

#Функции

def new_file():
    open(txt.get(), 'w')

def save_file():
    with open(txt.get(), "w") as f:
        f.write(main.get("1.0",'end-1c'))
def open_file():
    s = open(txt.get(), "r")
    main.insert(1.0, s.read())

#Тело кода

program = Tk()
program.geometry('600x500')
program.resizable(False, False)
program.title('Ну, это типа выебываться.')

#Главная часть

lbl = Label(program, text="Текстовый редактор", font=("Arial Bold", 10))
lbl.grid(column=0, row=0)

lbl1 = Label(program, text="Название файла:", font=("Arial Bold", 10))
lbl1.grid(column=0, row=1)

txt = Entry(program, width=68, bg="lightgray")
txt.grid(row=1, column=1)

main = Text(width=65, bg="lightgray", wrap=WORD)
main.grid(row=2, column=0, columnspan=4)

scroll = Scrollbar(command=main.yview)
scroll.grid(row=2, column=2)

main.config(yscrollcommand=scroll.set)

# Кнопки

open_f = Button(program, text="Вставить содержимое файла", command=open_file)
open_f.grid(column=1, row=4)
new = Button(program, text="Создать (Очистить)", command=new_file)
new.grid(column=0, row=3)
save = Button(program, text="Сохранить", command=save_file)
save.grid(column=1, row=3)

program.mainloop()
