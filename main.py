from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from hadnler import get_data

window = Tk()
window.title("Парсер справок")

window.geometry("400x300")
frame = Frame(window)
frame.pack(expand=True)


def onClick():
    print(f"Колонка: {input_col.get()}")
    print(f"Ряд: {input_row.get()}")
    col = input_col.get()
    skiprow = int(input_row.get()) - 1
    file_name = fd.askopenfilename()
    get_data(file_name, col, skiprow)


label1 = ttk.Label(frame, text="Введите название колонки с инн:")
label1.pack()
input_col = ttk.Entry(frame)
input_col.pack()
label2 = ttk.Label(frame, text="Введите с какой строки начинаются инн:")
label2.pack()
input_row = ttk.Entry(frame)
input_row.pack()

head = Label(frame, text="Загрузите эксель файл")
head.pack()

btn = ttk.Button(text="Загрузить", command=onClick)
btn.pack()
window.mainloop()
