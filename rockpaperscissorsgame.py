from tkinter import *
import random

root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Rock Paper Scissors')
root.config(bg='seashell3')

Label(root, text='Rock Paper Scissors', font='arial 20 bold', bg = 'seashell2').pack()

user_take = StringVar()
Label(root, text='Choose anyone: Rock, Paper, Scissors', font='arial 15 bold', bg='seashell2').place(x=20,y=70)
Entry(root, font='arial 15', textvariable=user_take, bg='antiquewhite2').place(x=90, y=130)
##
comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick == 2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'
##
Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('Tie You both have selected the same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('You have Lost. Computer have selected Paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('You have Won. Computer have selected Scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('You have Lost. Computer have selected Scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('You have Won. Computer have selected Rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('You have Lost. Computer have selected Rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('You have Won. Computer have selected Paper')
    else:
        Result.set('Invalid: Choose Any One: -- Rock, Paper, Scissors')
##
def Reset():
    Result.set("")
    user_take.set("")
    
def Exit():
    root.destroy()

Entry(root, font='arial 10 bold', textvariable=Result, bg='antiquewhite2', width=50).place(x=25, y = 250)

Button(root, font='arial 13 bold', text = 'PLAY', padx=5, bg='seashell4', command=play).place(x=150, y=190)

Button(root, font = 'arial 13 bold', text = 'RESET', padx = 5, bg = 'seashell4', command=Reset).place(x = 70, y = 310)

Button(root, font = 'arial 13 bold', text = 'EXIT', padx = 5, bg = 'seashell4', command = Exit). place(x=230, y = 310)

root.mainloop()
