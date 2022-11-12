from tkinter import *
import time

root = Tk()
root.geometry("150x200")

#переменная, которая показывает сколько раз нажали
chet = 0
#эта переменная говорит нам, впервый ли раз мы нажали на кнопку
start = True

#функция, которая всё время обновляет время
def update_time() :
    global now_minutes, now_second, start_time, label2

    now_time = round(time.time() - start_time, 2)

    label2.configure(text=f"Прошло {now_time}")

    root.after(10, update_time)

#функция, которая добавляет 1 к переменной chet, а также если кнопку нажимается впервый раз, то запускает таймер
def plus():
    global start, start_time, chet

    #проверяем нажати кнопка впервый раз или нет
    if start==True:
        start=False
        start_time = time.time()
        update_time()

    #добавляем к переменной chet плюс один и изменяем надпись в окне
    chet+=1
    label.configure(text=chet)

label = Label(root, text=chet)
label.place(relheight=0.2, relwidth=0.8, rely=0.4, relx=0.1)

button1 = Button(root, text="+", command=plus)
button1.place(relheight=0.2, relwidth=0.8, rely=0.1, relx=0.1)

label2 = Button(root, text="")
label2.place(relheight=0.2, relwidth=0.8, rely=0.7, relx=0.1)

root.mainloop()