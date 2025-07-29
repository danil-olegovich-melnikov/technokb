import tkinter as tk
import random

def press():
    value = input1.get()
    input1.delete(0, "end")
    if value:
        # input1.insert(0, 'True')
        if value.isdigit():
            input1.insert(0, 'число')
            text2['text'] = f'Вы ввели число: {value}, вы получили баллов: {random.randint(-int(value), int(value))}'
        else:
            input1.insert(0, 'текст')
        input1['bg'] = 'black'
    else:
        # input1.insert(0, 'False')
        input1['bg'] = 'red'
    
    text1.place_forget()
    input1.place_forget()
    button1.place_forget()

    

window = tk.Tk()
window.geometry("400x400")
window.title('Проектная работа')


text1 = tk.Label(window, text="Определитель", font="Times 24", fg='purple')
text1.place(x=200, y=40, anchor=tk.CENTER)

input1 = tk.Entry(window, bg='black')
input1.place(x=200, y=80, anchor=tk.CENTER, width=200)

button1 = tk.Button(window, text='Нажми на меня', command=press, bg='green')
button1.place(x=200, y=150, anchor=tk.CENTER, width=200, height=50)

text2 = tk.Label(window, text="", font="Times 12", fg='green')
text2.place(x=200, y=300, anchor=tk.CENTER)


window.mainloop()