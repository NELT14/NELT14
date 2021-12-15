from tkinter import Button, Event, Tk, Label, font
from math import *
import os
import keyboard

root = Tk()
cor = {'+': '+', '*': '×', '/': '÷', '-': '-', '%': 'mod', '^': '^', '1': '1', '2': '2', '3': '3',
       '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '0': '0', '.': '.', '(': '(', ')': ')', 'l': 'l', '@': '√'}
cor2 = {'+': '+', '*': '*', '/': '/', '-': '-', '%': '%', '^': '**', '1': '1', '2': '2', '3': '3',
        '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '0': '0', '.': '.', '(': '(', ')': ')', 'l': 'l', '@': '@'}
op = {'+': '+', '*': '×', '/': '÷', '-': '-',
      '%': 'mod', '^': '^', 'l': 'l', '@': '√'}
root.title('Calculator')
root.iconbitmap(rf'{os.getcwd()}\calc.ico')
root.geometry('450x550+450+200')
root.resizable(False, False)


m = ''
flag = 0
flag2 = 1


def f(button) -> None:
    global m, flag, flag2
    if type(button) == Event:
        button = button.char
    if not cor.get(button) or (len(res['text']) >= 17 and (not flag or op.get(button))):
        return
    if flag2:
        flag2 = 0
        if button == 'l':
            m = f'log10({res["text"]})'
            res['text'] = f'log({res["text"]})'
        elif button == '@':
            m = f'sqrt({res["text"]})'
            res['text'] = f'√({res["text"]})'
        else:
            m = cor2[button]
            res['text'] = cor[button]
        return
    if flag:
        flag = 0
        if not op.get(button):
            m = cor2[button]
            res['text'] = button
            return
        else:
            if button == 'l':
                m = f'log10({res["text"]})'
                res['text'] = f'log({res["text"]})'
            elif button == '@':
                m = f'sqrt({res["text"]})'
                res['text'] = f'√({res["text"]})'
            else:
                m += cor2[button]
                res['text'] += cor[button]
            return
    if button == 'l':
        m = f'log10({m})'
        res['text'] = f'log({res["text"]})'
    elif button == '@':
        m = f'sqrt({m})'
        res['text'] = f'√({res["text"]})'
    else:
        res['text'] += cor[button]
        m += cor2[button]


def enter(self=None) -> None:
    global m, flag, flag2
    rs = eval(m)
    if flag2:
        return
    if rs > 99999999999999999:
        res['text'] = 'Owerflow'
        flag = 1
        return
    rs2 = rs - int(rs)
    if rs2:
        rs2 = str(rs2)
        rs2 = len(rs2[rs2.find('.'):rs2[rs2.find('.'):].find('0')])
        if rs2 > 15:
            res['text'] = '%.15f' % rs
        else:
            res['text'] = f'%.{rs2}f' % rs
        flag = 1
        return
    flag = 1
    res['text'] = str(int(rs))


def backspace(self=None):
    global m, flag, flag2
    if len(res['text']) <= 1 or (res['text'] == 'mod'):
        m = ''
        res['text'] = '0'
        flag = 0
        flag2 = 1
        return
    if flag2 or flag:
        return
    if res['text'][-3:] == 'mod' and res['text'][-1] == ')':
        res['text'] = res['text'][:-3]
    elif res['text'][:3] == 'log' and res['text'][-1] == ')':
        res['text'] = res['text'][4:-1]
        m = m[6:-1]
        return
    elif res['text'][0] == '√' and res['text'][-1] == ')':
        res['text'] = res['text'][2:-1]
        m = m[5:-1]
        return
    else:
        res['text'] = res['text'][:-1]
    m = m[:-1]


res = Label(root, relief='solid', font='consolas 35',
            width=17, anchor='e', text='0')
res.place(x=0, y=0)

b0 = Button(root, font='consolas 35', text='0',
            width=3, relief='ridge', command=lambda c='0': f(c))
b0.place(x=185, y=450)
b1 = Button(root, font='consolas 35', text='1',
            width=3, relief='ridge', command=lambda c='1': f(c))
b1.place(x=100, y=355)
b2 = Button(root, font='consolas 35', text='2',
            width=3, relief='ridge', command=lambda c='2': f(c))
b2.place(x=185, y=355)
b3 = Button(root, font='consolas 35', text='3',
            width=3, relief='ridge', command=lambda c='3': f(c))
b3.place(x=270, y=355)
b4 = Button(root, font='consolas 35', text='4',
            width=3, relief='ridge', command=lambda c='4': f(c))
b4.place(x=100, y=260)
b5 = Button(root, font='consolas 35', text='5',
            width=3, relief='ridge', command=lambda c='5': f(c))
b5.place(x=185, y=260)
b6 = Button(root, font='consolas 35', text='6',
            width=3, relief='ridge', command=lambda c='6': f(c))
b6.place(x=270, y=260)
b7 = Button(root, font='consolas 35', text='7',
            width=3, relief='ridge', command=lambda c='7': f(c))
b7.place(x=100, y=165)
b8 = Button(root, font='consolas 35', text='8',
            width=3, relief='ridge', command=lambda c='8': f(c))
b8.place(x=185, y=165)
b9 = Button(root, font='consolas 35', text='9',
            width=3, relief='ridge', command=lambda c='9': f(c))
b9.place(x=270, y=165)
bpl = Button(root, font='consolas 35', text='+',
             width=3, relief='ridge', command=lambda c='+': f(c))
bpl.place(x=355, y=355)
bmn = Button(root, font='consolas 35', text='-',
             width=3, relief='ridge', command=lambda c='-': f(c))
bmn.place(x=355, y=260)
bdv = Button(root, font='consolas 35', text='÷',
             width=3, relief='ridge', command=lambda c='/': f(c))
bdv.place(x=355, y=70)
bml = Button(root, font='consolas 35', text='×',
             width=3, relief='ridge', command=lambda c='*': f(c))
bml.place(x=355, y=165)
bdot = Button(root, font='consolas 35', text='.',
              width=3, relief='ridge', command=lambda c='.': f(c))
bdot.place(x=270, y=450)
bEQ = Button(root, font='consolas 35', text='=',
             width=3, relief='ridge', command=enter)
bEQ.place(x=355, y=450)
bBackSpace = Button(root, font='consolas 35', text='⌫',
                    width=3, relief='ridge', command=backspace)
bBackSpace.place(x=270, y=70)
bb1 = Button(root, font='Consolas 35', text=')', width=3,
             relief='ridge', command=lambda c=')': f(c))
bb1.place(x=185, y=70)
bb2 = Button(root, font='Consolas 35', text='(', width=3,
             relief='ridge', command=lambda c='(': f(c))
bb2.place(x=100, y=70)
blog = Button(root, font='Consolas 35', text='log', width=3,
              relief='ridge', command=lambda c='l': f(c))
blog.place(x=15, y=70)
broot = Button(root, font='Consolas 35', text='√', width=3,
               relief='ridge', command=lambda c='@': f(c))
broot.place(x=15, y=165)
root.bind('<Return>', enter)
root.bind('<BackSpace>', backspace)
root.bind('<Key>', f)
root.mainloop()
