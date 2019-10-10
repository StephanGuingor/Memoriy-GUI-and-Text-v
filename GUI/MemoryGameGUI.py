from random import shuffle
import time
import tkinter as tk

#Plan


score = 0

def set_board(size):
    board = []
    i=-1
    for element in range(size):
        i =0
        board += [[str(i)]]
    for element in range(size):
        i+=1
        for element in range(size):
            board[element] += str(i)
    return board

def set_cards(cards,board2):
    i=-1
    board = []
    for element in range(board2):
        board += [[]]
    for element in range(board2):
        i += 1
        board[element] += cards[i]
        i+= 1
        board[element] += cards[i]
        i+= 1
        board[element] += cards[i]
        i+= 1
        board[element] += cards[i]
    return board     

#Popup shows that asks to restart or quit
def popup():

    def leavemini():
        global root1
        popup.destroy()
        root1.destroy()

    def restart():
        global root1
        global score 
        score = 0
        root1.destroy()
        MainLoop2()
        popup.destroy()

    popup = tk.Tk()
    label = tk.Label(popup,text="YOU WIN!",font=40,bg="yellow")
    label.pack(side="top",fill="x",pady=10)
    B1 = tk.Button(popup,text="Quit",command=leavemini)
    B1.pack()
    B2=tk.Button(popup,text="Restart",command=restart)
    B2.pack()
    popup.mainloop()

control_flow = []
# vars = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12]
def new_click(x,text):
    global control_flow
    if len(control_flow) < 2:
        x.config(image="",bg="white",text=(text),font=5,activebackground="white")
        control_flow.append(text)
        print(control_flow)

control_2=[]
#Checks if there are more than two items selected
def checker(photo):
    global score
    global score1
    global control_flow
    global control_2
    global x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12

    vars = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12]
    print(vars)
    if len(control_flow) >= 2:
        if control_flow[0] == control_flow[1]:
            if vars[cards.index([control_flow[0]])] in control_2 or vars[cards.index([control_flow[1]])] in control_2:
                print("Cheater")
            print("CONTROL",control_flow[0])
            index1 = cards.index([control_flow[0]])
            print(index1,"uno")

            control_2.append(vars[index1])
            del cards[index1]
            cards.insert(index1,"FAKE")
            index2 = cards.index([control_flow[1]])
            print(index2,"dos")
            del cards[index1]
            

            cards.insert(index1,[control_flow[0]])
            
            control_2.append(vars[index2])
            print(control_2)
            control_flow = []
            if score <= 0:
                score+=1
            else:
                score+=1
            score1.config(text="Pairs gotten: "+str(score))
            if score >= 6:
                popup()

        else:
            control_flow = []
            if len(control_2)  >= 1:
                print("CONTROL 2",control_2)
                for x in vars:
                    if x in control_2:
                        continue
                    else:
                        x.config(image=photo,bg="white",text="",font=5,activebackground="white")
                  
            else:
                for x in vars:
                    x.config(image=photo,bg="white",text="",font=5,activebackground="white")
                 
        
#MAIN LOOP

root = tk.Tk()


def click(root=root):
    root.destroy()
    MainLoop2()

def MainLoop(root=root):
    height = 700
    width = 700
   


    #Loop Start
    root.title("Memory")
    canvas = tk.Canvas(root,height=height, width=width)
    canvas.pack()
#MENU
    # menu.set_menu(root,height,width)
    bg = tk.PhotoImage(file="bgmenu.png")
    bg_label = tk.Label(root,image=bg)
    bg_label.place(relheight=1,relwidth=1)

    lower_frame = tk.Frame(root,bg="#37A1F2",bd=10)
    lower_frame.place(relx=0.25,rely=0.537,relwidth=0.5,relheight=0.3)

    button = tk.Button(lower_frame, text="Play!",font=40,relief="ridge",command = click)
    button.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

    upper_frame = tk.Frame(root,bg="#37A1F2",bd=10)
    upper_frame.place(relx=0.25,rely=0.05,relwidth=0.5,relheight=0.2)

    upper_frame2 = tk.Frame(upper_frame,bg="#4C4CB7",bd=15)
    upper_frame2.place(relx=0,rely=0,relwidth=1,relheight=1)

    name_label = tk.Label(upper_frame2,text="Memory", font="40",bg="#4C4CB7")
    name_label.pack(side="top",fill="x")

    by = tk.Label(upper_frame2,text="By:", font="40",bg="#4C4CB7")
    by.pack(side="top",fill="x")

    name = tk.Label(upper_frame2,text="Stephan", font="40",bg="#4C4CB7")
    name.pack(side="top",fill="x")
#END MENU
   #Loop End
    root.mainloop()

def MainLoop2():
    global cards
    global root1
    # board = Board()
    
    
    cards = [['Spade'],['Spade'],['Ace'],['Ace'],['Dart'],['Dart'],['Computer'],['Computer'],['Smok'],['Smok'],['Book'],['Book']]
    shuffle(cards)
    print(cards)
    board_repr = set_board(3)
    board_cards = set_cards(cards,3)
    print(board_cards)
    print(board_repr)

    root1 = tk.Tk()
    height = 700
    width = 700
    root1.title("Memory")

    canvas = tk.Canvas(root1,height=height, width=width)
    canvas.pack()

    # pic = tk.PhotoImage(file="blank.png")

    bg = tk.PhotoImage(file="blue.png")
    bg_label = tk.Label(root1,image=bg)
    bg_label.place(relheight=1,relwidth=1,rely=0.2)
    
    game_frame = tk.Frame(root1,bg="#4C4CB7",bd=15)
    game_frame.place(relx=0,rely=0,relwidth=1,relheight=0.2)

    upper_frame2 = tk.Frame(game_frame,bg="white",bd=15)
    upper_frame2.place(relx=0,rely=0,relwidth=1,relheight=1)

    #FRAMES FOR CARDS
    card_frame1 = tk.Frame(root1,bg="#226467",bd=5)
    card_frame1.place(relx=0,rely=0.25,relwidth=1,relheight=0.25)

    card_frame2 = tk.Frame(root1,bg="#226467",bd=5)
    card_frame2.place(relx=0,rely=0.5,relwidth=1,relheight=0.25)

    card_frame3 = tk.Frame(root1,bg="#226467",bd=5)
    card_frame3.place(relx=0,rely=0.75,relwidth=1,relheight=0.25)

    #CARDS
    photo=tk.PhotoImage(file="new_card.png")
    #SIDE 1
    global x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12
    global control_flow
    global score
    global score1
    x1=tk.Button(card_frame1,image=photo,width="40",text="0,0",height="40",activebackground="black",bg="black", bd=2,relief="ridge",command=lambda: new_click(x1,board_cards[0][0]))
    x1.place(relx=0,rely=0,relwidth=0.25,relheight=1)
    # x_1=tk.Button(x1,width="40",text="1",height="40",activebackground="green",bg="white", bd=2,relief="ridge",command=lambda: new_click(x1,board_cards[0][0]))
    # x_1.place(relx=0.8,rely=0.8,relwidth=0.15,relheight=0.15)
    # botton_active(cards,x1,b_list,0)
    x2=tk.Button(card_frame1,image=photo,width="40",height="40",activebackground="black",bg="black", bd=2,relief="ridge",command=lambda: new_click(x2,board_cards[0][1]))
    x2.place(relx=0.25,rely=0,relwidth=0.25,relheight=1)
    # x_2=tk.Button(x2,width="40",text="1",height="40",activebackground="green",bg="white", bd=2,relief="ridge",command=lambda: new_click(x2,board_cards[0][1]))
    # x_2.place(relx=0.8,rely=0.8,relwidth=0.15,relheight=0.15)
    # botton_active(cards,x2,b_list,0)
    x3=tk.Button(card_frame1,image=photo,width="40",height="40",activebackground="black", bg="black", bd=2,relief="ridge",command=lambda: new_click(x3,board_cards[0][2]))
    x3.place(relx=0.5,rely=0,relwidth=0.25,relheight=1)
    # x_3=tk.Button(x3,width="40",text="1",height="40",activebackground="green",bg="white", bd=2,relief="ridge",command=lambda: new_click(x3,board_cards[0][2]))
    # x_3.place(relx=0.8,rely=0.8,relwidth=0.15,relheight=0.15)
    # botton_active(cards,x3,b_list,0)
    x4=tk.Button(card_frame1,image=photo,width="40",height="40",activebackground="black",
    bg="black", bd=2,relief="ridge",command=lambda: new_click(x4,board_cards[0][3]))
    x4.place(relx=0.75,rely=0,relwidth=0.25,relheight=1)
    # x_4=tk.Button(x4,width="40",text="1",height="40",activebackground="green",bg="white", bd=2,relief="ridge",command=lambda: new_click(x4,board_cards[0][3]))
    # x_4.place(relx=0.8,rely=0.8,relwidth=0.15,relheight=0.15)
    # botton_active(cards,x4,b_list,0)
#SIDE 2
    x5=tk.Button(card_frame2,image=photo,width="40",height="40",activebackground="black",
    bg="black", bd=2,relief="ridge",command=lambda: new_click(x5,board_cards[1][0]))
    x5.place(relx=0,rely=0,relwidth=0.25,relheight=1)
    # x_5=tk.Button(x5,width="40",text="1",height="40",activebackground="green",bg="white", bd=2,relief="ridge",command=lambda: new_click(x5,board_cards[1][0]))
    # x_5.place(relx=0.8,rely=0.8,relwidth=0.15,relheight=0.15)
    # botton_active(cards,x5,b_list,0)   
    x6=tk.Button(card_frame2,image=photo,width="40",height="40",activebackground="black",
    bg="black", bd=2,relief="ridge",command=lambda: new_click(x6,board_cards[1][1]))
    x6.place(relx=0.25,rely=0,relwidth=0.25,relheight=1)
    # x_6=tk.Button(x6,width="40",text="1",height="40",activebackground="green",bg="white", bd=2,relief="ridge",command=lambda: new_click(x6,board_cards[1][1]))
    # x_6.place(relx=0.8,rely=0.8,relwidth=0.15,relheight=0.15)
    # botton_active(cards,x6,b_list,0)
    x7=tk.Button(card_frame2,image=photo,width="40",height="40",activebackground="black",
    bg="black", bd=2,relief="ridge",command=lambda: new_click(x7,board_cards[1][2]))
    x7.place(relx=0.5,rely=0,relwidth=0.25,relheight=1)
    # x_7=tk.Button(x7,width="40",text="1",height="40",activebackground="green",bg="white", bd=2,relief="ridge",command=lambda: new_click(x7,board_cards[1][2]))
    # x_7.place(relx=0.8,rely=0.8,relwidth=0.15,relheight=0.15)
    # botton_active(cards,x7,b_list,0)
    x8=tk.Button(card_frame2,image=photo,width="40",height="40",activebackground="black",
    bg="black", bd=2,relief="ridge",command=lambda: new_click(x8,board_cards[1][3]))
    x8.place(relx=0.75,rely=0,relwidth=0.25,relheight=1)
    # x_8=tk.Button(x8,width="40",text="1",height="40",activebackground="green",bg="white", bd=2,relief="ridge",command=lambda: new_click(x8,board_cards[1][3]))
    # x_8.place(relx=0.8,rely=0.8,relwidth=0.15,relheight=0.15)
#SIDE 3
    # botton_active(cards,x8,b_list,0)
    x9=tk.Button(card_frame3,image=photo,width="40",height="40",activebackground="black",
    bg="black", bd=2,relief="ridge",command=lambda: new_click(x9,board_cards[2][0]))
    x9.place(relx=0,rely=0,relwidth=0.25,relheight=1)
    # x_9=tk.Button(x9,width="40",text="1",height="40",activebackground="green",bg="white", bd=2,relief="ridge",command=lambda: new_click(x9,board_cards[2][0]))
    # x_9.place(relx=0.8,rely=0.8,relwidth=0.15,relheight=0.15)
    # botton_active(cards,x9,b_list,0)    
    x10=tk.Button(card_frame3,image=photo,width="40",height="40",activebackground="black",
    bg="black", bd=2,relief="ridge",command=lambda: new_click(x10,board_cards[2][1]))
    x10.place(relx=0.25,rely=0,relwidth=0.25,relheight=1)
    # x_10=tk.Button(x10,width="40",text="1",height="40",activebackground="green",bg="white", bd=2,relief="ridge",command=lambda: new_click(x10,board_cards[2][1]))
    # x_10.place(relx=0.8,rely=0.8,relwidth=0.15,relheight=0.15)
    # botton_active()
    x11=tk.Button(card_frame3,image=photo,width="40",height="40",activebackground="black",
    bg="black", bd=2,relief="ridge",command=lambda: new_click(x11,board_cards[2][2]))
    x11.place(relx=0.5,rely=0,relwidth=0.25,relheight=1)
    # x_11=tk.Button(x11,width="40",text="1",height="40",activebackground="green",bg="white", bd=2,relief="ridge",command=lambda: new_click(x11,board_cards[2][2]))
    # x_11.place(relx=0.8,rely=0.8,relwidth=0.15,relheight=0.15)
    # botton_active()
    x12=tk.Button(card_frame3,image=photo,width="40",height="40",activebackground="black",
    bg="black", bd=2,relief="ridge",command=lambda: new_click(x12,board_cards[2][3]))
    x12.place(relx=0.75,rely=0,relwidth=0.25,relheight=1)
    # x_12=tk.Button(x12,width="40",text="1",height="40",activebackground="green",bg="white", bd=2,relief="ridge",command=lambda: new_click(x12,board_cards[2][3]))
    # x_12.place(relx=0.8,rely=0.8,relwidth=0.15,relheight=0.15)

    score1 = tk.Label(game_frame,text="Pairs gotten: "+str(score),font=40,bg="white")
    score1.place(relx=0,rely=0,relwidth=0.5,relheight=1)
    

    check=tk.Button(game_frame,width="40",height="40",text="Check",font=40,activebackground="green",
    bg="green", bd=2,relief="ridge",command=lambda:checker(photo))
    check.place(relx=0.5,rely=0,relwidth=0.5,relheight=1)
    # if len(control_flow) >= 2:
    #     checkers()

    
    root1.mainloop()


#GAME
MainLoop()


   