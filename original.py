from tkinter import *
import speech_recognition as s


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def mod(a, b):
    return a % b


def lcm(a, b):
    L = a if a > b else b
    while L <= a * b:
        if L % a == 0 and L % b == 0:
            return L
        L += 1


def hcf(a, b):
    H = a if a < b else b
    while H >= 1:
        if a % H == 0 and b % H == 0:
            return H
            H -= 1


def extraxt_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l


def calculate(event=" "):
    text = textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extraxt_from_text(text)
                r = operations[word.upper()](l[0], l[1])
                list.delete(0, END)
                list.insert(END, r)
            except:
                list.delete(0, END)
                list.insert(END, 'Something went wrong please type again')
            finally:
                break

        elif word.upper() not in operations.keys():
            list.delete(0, END)
            list.insert(END, 'Something went wrong please type again')


operations = {'+': add, 'ADD': add, 'ADDITION': add, 'SUM': add, 'PLUS': add,

              '-': sub, 'SUB': sub, 'DIFFERENCE': sub, 'MINUS': sub, 'SUBTRACT': sub,
              'LCM': lcm, 'HCF': hcf, '*': mul, 'PRODUCT': mul, 'MULTIPLICATION': mul,
              'MULTIPLY BY': mul, '/': div, 'DIVISION': div, 'DIV': div, 'DIVIDE': div, 'DIVIDED BY': div, '%': mod,

              'MOD': mod,

              'REMAINDER': mod, 'MODULUS': mod, }

win = Tk()
win.geometry('500x300')
win.title('RSC Voice Calculator')
win.configure(bg='black')


photo = PhotoImage(file='C:\\Users\\CHANDAN\\Downloads\\mic.png').subsample(13, 13)
l1 = Label(win, text='RSC SMART CALCULATOR ', bg='skyblue', width=20, padx=20)
l1.place(x=160, y=60)



def buttonClick():
    # create a object of recognizer

    sr = s.Recognizer()
    with s.Microphone() as m:
        audio = sr.listen(m, timeout=5)
        query = sr.recognize_google(audio, language='eng-in')
        e1.focus()
        e1.insert(0, query)


textin = StringVar()
e1 = Entry(win, width=40, textvariable=textin)
e1.place(x=130, y=100)
b1 = Button(win, image=photo, command=buttonClick, bd=0, activebackground='#c1bfbf', overrelief='groove',
            relief='sunken')
b1.place(x=380, y=100)
b2 = Button(win, text='click here', command=calculate)
b2.place(x=220, y=150)
win.bind('<Enter>', calculate)
list = Listbox(win, width=20, height=2)
list.place(x=185, y=200)

win.mainloop()
