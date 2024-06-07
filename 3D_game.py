from tkinter import *
from tkinter import messagebox
from random import randint

# основное окно:
root = Tk()
root.resizable(False, False)
root.title('Пятнашки')
root.geometry('400x400')
root.configure(bg='gray22')

mape = [
    'green', 'green', 'green', 'green',

    'green', 'green', 'green', 'green',

    'green', 'green', 'green', 'green',

    'green', 'green', 'green', 'green']

texts = []


def generate():
    http = -1
    for i in range(16):
        j = 0
        while j == 0:
            k = randint(0, 15)
            if not (str(k) in texts):
                if str(k) == '0':
                    http = i
                texts.append(str(k))
                j = 1

    j = randint(0, 15)
    t = texts[j]
    mape[j] = 'brown'
    texts[j] = ''
    texts[http] = t


generate()


def draw():
    but1.configure(bg=mape[0], text=texts[0])
    but2.configure(bg=mape[1], text=texts[1])
    but3.configure(bg=mape[2], text=texts[2])
    but4.configure(bg=mape[3], text=texts[3])
    but5.configure(bg=mape[4], text=texts[4])
    but6.configure(bg=mape[5], text=texts[5])
    but7.configure(bg=mape[6], text=texts[6])
    but8.configure(bg=mape[7], text=texts[7])
    but9.configure(bg=mape[8], text=texts[8])
    but10.configure(bg=mape[9], text=texts[9])
    but11.configure(bg=mape[10], text=texts[10])
    but12.configure(bg=mape[11], text=texts[11])
    but13.configure(bg=mape[12], text=texts[12])
    but14.configure(bg=mape[13], text=texts[13])
    but15.configure(bg=mape[14], text=texts[14])
    but16.configure(bg=mape[15], text=texts[15])


soots = {
    '1': (2, 5),
    '2': (1, 3, 6),
    '3': (2, 7, 4),
    '4': (3, 8),
    '5': (1, 6, 9),
    '6': (2, 5, 10, 7),
    '7': (3, 6, 11, 8),
    '8': (4, 7, 12),
    '9': (5, 10, 13),
    '10': (9, 6, 11, 14),
    '11': (10, 7, 12, 15),
    '12': (8, 11, 16),
    '13': (9, 14),
    '14': (13, 10, 15),
    '15': (14, 11, 16),
    '16': (15, 12)
}


def logic(x):
    x = x
    for i in soots[str(x)]:
        if mape[i - 1] == 'brown':
            mape[x - 1] = 'brown'
            mape[i - 1] = 'green'
            t = texts[x - 1]
            texts[x - 1] = texts[i - 1]
            texts[i - 1] = t
            break

    draw()

    if texts == ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '']:
        messagebox.showinfo('Results', 'You winner!\nGame End!')

# кнопки:
but1 = Button(root)
but1.configure(bg=mape[0], text=texts[0], command=lambda: logic(1))
but1.place(height=100, width=100, x=0, y=0)

but2 = Button(root)
but2.configure(bg=mape[1], text=texts[1], command=lambda: logic(2))
but2.place(height=100, width=100, x=100, y=0)

but3 = Button(root)
but3.configure(bg=mape[2], text=texts[2], command=lambda: logic(3))
but3.place(height=100, width=100, x=200, y=0)

but4 = Button(root)
but4.configure(bg=mape[3], text=texts[3], command=lambda: logic(4))
but4.place(height=100, width=100, x=300, y=0)

but5 = Button(root)
but5.configure(bg=mape[4], text=texts[4], command=lambda: logic(5))
but5.place(height=100, width=100, x=0, y=100)

but6 = Button(root)
but6.configure(bg=mape[5], text=texts[5], command=lambda: logic(6))
but6.place(height=100, width=100, x=100, y=100)

but7 = Button(root)
but7.configure(bg=mape[6], text=texts[6], command=lambda: logic(7))
but7.place(height=100, width=100, x=200, y=100)

but8 = Button(root)
but8.configure(bg=mape[7], text=texts[7], command=lambda: logic(8))
but8.place(height=100, width=100, x=300, y=100)

but9 = Button(root)
but9.configure(bg=mape[8], text=texts[8], command=lambda: logic(9))
but9.place(height=100, width=100, x=0, y=200)

but10 = Button(root)
but10.configure(bg=mape[9], text=texts[9], command=lambda: logic(10))
but10.place(height=100, width=100, x=100, y=200)

but11 = Button(root)
but11.configure(bg=mape[10], text=texts[10], command=lambda: logic(11))

but11.place(height=100, width=100, x=200, y=200)

but12 = Button(root)
but12.configure(bg=mape[11], text=texts[11], command=lambda: logic(12))
but12.place(height=100, width=100, x=300, y=200)

but13 = Button(root)
but13.configure(bg=mape[12], text=texts[12], command=lambda: logic(13))
but13.place(height=100, width=100, x=0, y=300)

but14 = Button(root)
but14.configure(bg=mape[13], text=texts[13], command=lambda: logic(14))
but14.place(height=100, width=100, x=100, y=300)

but15 = Button(root)
but15.configure(bg=mape[14], text=texts[14], command=lambda: logic(15))
but15.place(height=100, width=100, x=200, y=300)

but16 = Button(root)
but16.configure(bg=mape[15], text=texts[15], command=lambda: logic(16))
but16.place(height=100, width=100, x=300, y=300)

# вывод на экран:
root.mainloop()

