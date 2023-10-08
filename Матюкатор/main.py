from tkinter import *
import random


#Генерация оскорблений из массива и def-ы.
slovo = ['Ебучий', 'Грёбаный', 'Сучий', 'Ебланский', "Злоебучий", "Сраный", "Мудацкий", "Въебанный", "Хуев", "Обосранный", "Охуевший", "Уебанский", "Дроченный", "Обоссаный", "Долбаёбский", "Пидорский", "Писькострадательский", "Уёбищный", "Лоховской"]
osk = ['дебил', 'долбаёб', 'уёбок', 'хуила', 'eблантий', "архипиздрит", "бздло", "блядун", "выблядыш", "говнище", "гондон", "нахуйник", "пидор", "объебос", "говноед", "чмо", "уёбище", "сволочь", "пиздище", "пидарас", "конча", "мудоеб", "мудозвон", "мудоклюй", "паскуда"]

def clicked():
    label0.configure(text=f"Ты - {random.choice(slovo)} {random.choice(osk)}.")
priva = '''Привет! Это матюкатор skycar-а, нажми кнопку "сгенерировать" и я тебя обматерю!'''

#Вывод в окно.
root = Tk()

#Параметры окна
root.title("Матюкатор skycar-а.")
root.resizable(False, False)
root.geometry("1200x300+300+250")

#Текст

label0 = Label(text = priva, justify = LEFT, font=("Arial Bold", 20))
label0.place(relx = .05, rely = .3)


#Кнопка.
button1 = Button(root, text = 'Сгенерировать', bg = 'grey', command=clicked)
button1.bind('<Button-1>', clicked)
button1.pack(fill = 'both', side = 'bottom')
button1.pack()


root.mainloop()
