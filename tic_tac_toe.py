"""Tic Tac Toe"""

from tkinter import *
root=Tk()
root.geometry("220x250")
root.title("Tic Tac Toe")
frame1=Frame(root)
frame1.pack()
frame2=Frame(root)
frame2.pack()
labeltitle=Label(frame1,text="Tic Tac Toe",font=("Arial",15),bg="orange",width=20)
labeltitle.grid(row=0,column=0)

dict={1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:""}

turn="X"
game_end=False

def checkfordraw():
    for i in dict.keys():
        if dict[i]=="":
            return False
    return True


def play(event):
    global turn,game_end
    if game_end:
        return
    button=event.widget
    btntext=str(button)
    clicked=btntext[-1]
    if clicked=="n":
        clicked=1
    else:
        clicked=int(clicked)

    if button["text"]=="":
        button["text"]="X"

        if turn=="X":
            button["text"]="X"
            dict[clicked]=turn
            if checkforWin(turn):
                labelwin=Label(frame1,text=f"{turn} wins the game",bg="orange",font=("Arial",15),width=20)
                labelwin.grid(row=0,column=0,columnspan=3)
                game_end = True
            turn="O"
        elif turn=="O":
            button["text"]="O"
            dict[clicked]=turn
            if checkforWin(turn):
                labelwin=Label(frame1,text=f"{turn} wins the game",bg="orange",font=("Arial",15),width=20)
                labelwin.grid(row=0,column=0,columnspan=3)
                game_end = True
            turn="X"
    if checkfordraw():
        drawlabel=Label(frame1,text="Game Draw",bg="orange",font=("Arial",15),width=20)
        drawlabel.grid(row=0,column=0,columnspan=3)

def restartGame():
    global game_end
    game_end = False
    for button in buttons:
        button["text"]=""

    for i in dict.keys():
        dict[i]=""
    labeltitle = Label(frame1, text="Tic Tac Toe", font=("Arial", 15), bg="orange", width=20)
    labeltitle.grid(row=0, column=0)


def checkforWin(player):
    # Row Condition
    if dict[1]==dict[2] and dict[2]==dict[3] and dict[3]==player:
        return True
    elif dict[4]==dict[5] and dict[5]==dict[6] and dict[6]==player:
        return True
    elif dict[7]==dict[8] and dict[8]==dict[9] and dict[9]==player:
        return True
    # Column Condition
    elif dict[1]==dict[4] and dict[4]==dict[7] and dict[7]==player:
        return True
    elif dict[2]==dict[5] and dict[5]==dict[8] and dict[8]==player:
        return True
    elif dict[3]==dict[6] and dict[6]==dict[9] and dict[9]==player:
        return True
    # Diagonals Condition
    elif dict[1]==dict[5] and dict[5]==dict[9] and dict[9]==player:
        return True
    elif dict[3]==dict[5] and dict[5]==dict[7] and dict[7]==player:
        return True

# Tic Tac Toe Board

# First Row
btn1=Button(frame2,text="",font=("Arial",20),width=3,height=1,bg="yellow")
btn1.grid(row=0,column=0)
btn1.bind("<Button-1>",play)
btn2=Button(frame2,text="",font=("Arial",20),width=3,height=1,bg="yellow")
btn2.grid(row=0,column=1)
btn2.bind("<Button-1>",play)
btn3=Button(frame2,text="",font=("Arial",20),width=3,height=1,bg="yellow")
btn3.grid(row=0,column=2)
btn3.bind("<Button-1>",play)

# Second Row
btn4=Button(frame2,text="",font=("Arial",20),width=3,height=1,bg="yellow")
btn4.grid(row=1,column=0)
btn4.bind("<Button-1>",play)
btn5=Button(frame2,text="",font=("Arial",20),width=3,height=1,bg="yellow")
btn5.grid(row=1,column=1)
btn5.bind("<Button-1>",play)
btn6=Button(frame2,text="",font=("Arial",20),width=3,height=1,bg="yellow")
btn6.grid(row=1,column=2)
btn6.bind("<Button-1>",play)

# Third Row
btn7=Button(frame2,text="",font=("Arial",20),width=3,height=1,bg="yellow")
btn7.grid(row=2,column=0)
btn7.bind("<Button-1>",play)
btn8=Button(frame2,text="",font=("Arial",20),width=3,height=1,bg="yellow")
btn8.grid(row=2,column=1)
btn8.bind("<Button-1>",play)
btn9=Button(frame2,text="",font=("Arial",20),width=3,height=1,bg="yellow")
btn9.grid(row=2,column=2)
btn9.bind("<Button-1>",play)
restartbutton=Button(frame2,text="Restart Game",font=("Arial",15),bg="green",command=restartGame)
restartbutton.grid(row=3,column=0,columnspan=3)


buttons=[btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9]
root.mainloop()