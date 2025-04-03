import tkinter as tk
import os

#main window
root = tk.Tk()
root.title("tic tac toe")
root.geometry("375x225")

turn = 1 # 1 is x, -1 is o
btn1 = 0 
btn2 = 0
btn3 = 0
btn4 = 0
btn5 = 0
btn6 = 0
btn7 = 0
btn8 = 0
btn9 = 0

#functions
def checkwin():
    if btn1 == 1 and btn2 == 1 and btn3 == 1:
        winlabel.config(text= "X WINS!!! top row")
    if btn4 == 1 and btn5 == 1 and btn6 == 1:
        winlabel.config(text= "X WINS!!! middle row")
    if btn7 == 1 and btn8 == 1 and btn9 == 1:
        winlabel.config(text= "X WINS!!! bottom row")
    if btn1 == 1 and btn4 == 1 and btn7 == 1:
        winlabel.config(text= "X WINS!!! left column")
    if btn3 == 1 and btn5 == 1 and btn8 == 1:
        winlabel.config(text= "X WINS!!! middle column")
    if btn3 == 1 and btn6 == 1 and btn9 == 1:
        winlabel.config(text= "X WINS!!! right column")
    if btn1 == 1 and btn5 == 1 and btn9 == 1:
        winlabel.config(text= "X WINS!!! left to right across")
    if btn3 == 1 and btn5 == 1 and btn7 == 1:
        winlabel.config(text= "X WINS!!! right to left across")
    if btn1 == 1 and btn2 == 1 and btn3 == 1:
        winlabel.config(text= "O WINS!!! top row")
    if btn4 == -1 and btn5 == -1 and btn6 == -1:
        winlabel.config(text= "O WINS!!! middle row")
    if btn7 == -1 and btn8 == -1 and btn9 == -1:
        winlabel.config(text= "O WINS!!! bottom row")
    if btn1 == -1 and btn4 == -1 and btn7 == -1:
        winlabel.config(text= "O WINS!!! left column")
    if btn3 == -1 and btn5 == -1 and btn8 == -1:
        winlabel.config(text= "O WINS!!! middle column")
    if btn3 == -1 and btn6 == -1 and btn9 == -1:
        winlabel.config(text= "O WINS!!! right column")
    if btn1 == -1 and btn5 == -1 and btn9 == -1:
        winlabel.config(text= "O WINS!!! left to right across")
    if btn3 == -1 and btn5 == -1 and btn7 == -1:
        winlabel.config(text= "O WINS!!! right to left across")
def onClick1():
    global turn
    global btn1
    if turn > 0:
        button1.config(text="X", fg="red")
        turnlabel.config(text="O turn", fg="green")
        btn1 = 1
    if turn < 0:
        button1.config(text="O", fg="green")
        turnlabel.config(text="X turn", fg="red")
        btn1 = -1
    turn = turn * -1
    button1.config(state="disabled")
    checkwin()
def onClick2():
    global turn
    global btn2
    if turn > 0:
        button2.config(text="X", fg="red")
        turnlabel.config(text="O turn", fg="green")
        btn2 = 1
    if turn < 0:
        button2.config(text="O", fg="green")
        turnlabel.config(text="X turn", fg="red")
        btn2 = -1
    turn = turn * -1
    button2.config(state="disabled")
    checkwin()
def onClick3():
    global turn
    global btn3
    if turn > 0:
        button3.config(text="X", fg="red")
        turnlabel.config(text="O turn", fg="green")
        btn3 = 1
    if turn < 0:
        button3.config(text="O", fg="green")
        turnlabel.config(text="X turn", fg="red")
        btn3 = -1
    turn = turn * -1
    button3.config(state="disabled")
    checkwin()
def onClick4():
    global turn
    global btn4
    if turn > 0:
        button4.config(text="X", fg="red")
        turnlabel.config(text="O turn", fg="green")
        btn4 = 1
    if turn < 0:
        button4.config(text="O", fg="green")
        turnlabel.config(text="X turn", fg="red")
        btn4 = -1
    turn = turn * -1
    button4.config(state="disabled")
    checkwin()
def onClick5():
    global turn
    global btn5
    if turn > 0:
        button5.config(text="X", fg="red")
        turnlabel.config(text="O turn", fg="green")
        btn5 = 1
    if turn < 0:
        button5.config(text="O", fg="green")
        turnlabel.config(text="X turn", fg="red")
        btn5 = -1
    turn = turn * -1
    button5.config(state="disabled")
    checkwin()
def onClick6():
    global turn
    global btn6
    if turn > 0:
        button6.config(text="X", fg="red")
        turnlabel.config(text="O turn", fg="green")
        btn6 = 1
    if turn < 0:
        button6.config(text="O", fg="green")
        turnlabel.config(text="X turn", fg="red")
        btn6 = -1
    turn = turn * -1
    button6.config(state="disabled")
    checkwin()
def onClick7():
    global turn
    global btn7
    if turn > 0:
        button7.config(text="X", fg="red")
        turnlabel.config(text="O turn", fg="green")
        btn7 = 1
    if turn < 0:
        button7.config(text="O", fg="green")
        turnlabel.config(text="X turn", fg="red")
        btn7 = -1
    turn = turn * -1
    button7.config(state="disabled")
    checkwin()
def onClick8():
    global turn
    global btn8
    if turn > 0:
        button8.config(text="X", fg="red")
        turnlabel.config(text="O turn", fg="green")
        btn8 = 1
    if turn < 0:
        button8.config(text="O", fg="green")
        turnlabel.config(text="X turn", fg="red")
        btn8 = -1
    turn = turn * -1
    button8.config(state="disabled")
    checkwin()
def onClick9():
    global turn
    global btn9
    if turn > 0:
        button9.config(text="X", fg="red")
        turnlabel.config(text="O turn", fg="green")
        btn9 = 1
    if turn < 0:
        button9.config(text="O", fg="green")
        turnlabel.config(text="X turn", fg="red")
        btn9 = -1
    turn = turn * -1
    button9.config(state="disabled")
    checkwin()
def resetClick():
    global turn
    global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9
    turn = 1
    btn1 = btn2 = btn3 = btn4 = btn5 = btn6 = btn7 = btn8 = btn9 = 0

    # Reset button text, state, and color
    button1.config(text="[ ]", state="normal", fg="blue")
    button2.config(text="[ ]", state="normal", fg="blue")
    button3.config(text="[ ]", state="normal", fg="blue")
    button4.config(text="[ ]", state="normal", fg="blue")
    button5.config(text="[ ]", state="normal", fg="blue")
    button6.config(text="[ ]", state="normal", fg="blue")
    button7.config(text="[ ]", state="normal", fg="blue")
    button8.config(text="[ ]", state="normal", fg="blue")
    button9.config(text="[ ]", state="normal", fg="blue")
    winlabel.config(text=" ")
    turnlabel.config(text="X turn", fg="red")

#button and label creations
winlabel = tk.Label(root, text=" ")
winlabel.grid(row=0, column=7)
turnlabel = tk.Label(root, text="X turn", fg="red")
turnlabel.grid(row=0, column=5)
turnlabel.config(font=("Comic Sans", 20, "bold"),)
button1 = tk.Button(root, text= "[ ]", command=onClick1)
button1.config(font=("Comic Sans", 16, "bold"), fg="blue")
button1.place(x=10, y=50)
button2 = tk.Button(root, text= "[ ]", command=onClick2)
button2.config(font=("Comic Sans", 16, "bold"), fg="blue")
button2.place(x=60, y=50)
button3 = tk.Button(root, text= "[ ]", command=onClick3)
button3.config(font=("Comic Sans", 16, "bold"), fg="blue")
button3.place(x=110, y=50)
button4 = tk.Button(root, text= "[ ]", command=onClick4)
button4.config(font=("Comic Sans", 16, "bold"), fg="blue")
button4.place(x=10, y=100)
button5 = tk.Button(root, text= "[ ]", command=onClick5)
button5.config(font=("Comic Sans", 16, "bold"), fg="blue")
button5.place(x=60, y=100)
button6 = tk.Button(root, text= "[ ]", command=onClick6)
button6.config(font=("Comic Sans", 16, "bold"), fg="blue")
button6.place(x=110, y=100)
button7 = tk.Button(root, text= "[ ]", command=onClick7)
button7.config(font=("Comic Sans", 16, "bold"), fg="blue")
button7.place(x=10, y=150)
button8 = tk.Button(root, text= "[ ]", command=onClick8)
button8.config(font=("Comic Sans", 16, "bold"), fg="blue")
button8.place(x=60, y=150)
button9 = tk.Button(root, text= "[ ]", command=onClick9)
button9.config(font=("Comic Sans", 16, "bold"), fg="blue")
button9.place(x=110, y=150)
resetbutton = tk.Button(root, text="RESET", command=resetClick)
resetbutton.place(x=200, y= 150)

root.mainloop()