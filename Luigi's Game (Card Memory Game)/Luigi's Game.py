import tkinter as tk # Python 3.x Version
import time
import random
from random import randint
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import font

lay=[]
root = Tk()#Window for your applications
root.title("Luigi's Game") #Gives window a title
root.geometry("800x400")

top = Toplevel
lay.append(top)

#defining images
bg = PhotoImage (file="/Users/alexflorinski/OneDrive - NSW Department of Education/Work/SDD/2021/Major Project 2021/Code/main background.png")
bg2 = PhotoImage(file="/Users/alexflorinski/OneDrive - NSW Department of Education/Work/SDD/2021/Major Project 2021/Code/gamebackground2.png")
beginb = PhotoImage(file="/Users/alexflorinski/OneDrive - NSW Department of Education/Work/SDD/2021/Major Project 2021/Code/begin_b.png")
login_btn = PhotoImage(file="/Users/alexflorinski/OneDrive - NSW Department of Education/Work/SDD/2021/Major Project 2021/Code/p_button.png")
instru = PhotoImage(file="/Users/alexflorinski/OneDrive - NSW Department of Education/Work/SDD/2021/Major Project 2021/Code/inst_button.png")
exi = PhotoImage(file="/Users/alexflorinski/OneDrive - NSW Department of Education/Work/SDD/2021/Major Project 2021/Code/exit_b.png")
clo = PhotoImage(file="/Users/alexflorinski/OneDrive - NSW Department of Education/Work/SDD/2021/Major Project 2021/Code/close_b.png")
mayn = PhotoImage(file="/Users/alexflorinski/OneDrive - NSW Department of Education/Work/SDD/2021/Major Project 2021/Code/main_title.png")
yesb = PhotoImage(file="/Users/alexflorinski/OneDrive - NSW Department of Education/Work/SDD/2021/Major Project 2021/Code/yes button.png")
nob = PhotoImage(file="/Users/alexflorinski/OneDrive - NSW Department of Education/Work/SDD/2021/Major Project 2021/Code/no button.png")
carddown = PhotoImage(file="/Users/alexflorinski/OneDrive - NSW Department of Education/Work/SDD/2021/Major Project 2021/Code/card down.png")
coincard = PhotoImage(file="/Users/alexflorinski/OneDrive - NSW Department of Education/Work/SDD/2021/Major Project 2021/Code/coin_card.png") 
feathercard = PhotoImage(file="/Users/alexflorinski/OneDrive - NSW Department of Education/Work/SDD/2021/Major Project 2021/Code/feather_card.png")
flowercard = PhotoImage(file="/Users/alexflorinski/OneDrive - NSW Department of Education/Work/SDD/2021/Major Project 2021/Code/flower_card.png")
starcard = PhotoImage(file="/Users/alexflorinski/OneDrive - NSW Department of Education/Work/SDD/2021/Major Project 2021/Code/star_card.png")

#create font styles
font_heading = font.Font(family='Segoe UI Black', size=30, weight='bold')
font_button = font.Font(family='Montserrat Black', size=20, weight='bold')
font_button2 = font.Font(family='Montserrat Black', size=10, weight='bold')

def add_image():
    global my_image
    my_image = PhotoImage(file="main background.png")

def add_image2():
    global my_image2
    my_image2 = PhotoImage(file="game background.png")

def hello(): #beginning of game 
    def cardp(): #eight card placements
        my_label3 = tk.Label(window1, text=("You Have 3 Tries Left"), fg="black", font=font_button2)
        my_label3.place(x=550, y=20)

        global flipCount
        flipCount = 0

        global livesRemaining
        livesRemaining = 3 


        global flipped  
        flipped = [False, False, False, False, False, False, False, False]

        def cardcheck():

            global flipCount
            global flipped
            
            flipCount+=1
            if flipped[0]==True and flipped[5] == True:
                card0.destroy()
                card5.destroy()

            if flipped[1]==True and flipped[4] == True:
                card1.destroy()
                card4.destroy()

            if flipped[2]==True and flipped[6]== True:
                card2.destroy()
                card6.destroy()

            if flipped[3]==True and flipped[7]==True:
                card3.destroy()
                card7.destroy()

            if flipCount == 2:
                card0.configure(image=carddown, borderwidth=0)
                card1.configure(image=carddown, borderwidth=0)
                card2.configure(image=carddown, borderwidth=0)
                card3.configure(image=carddown, borderwidth=0)
                card4.configure(image=carddown, borderwidth=0)
                card5.configure(image=carddown, borderwidth=0)
                card6.configure(image=carddown, borderwidth=0)
                card7.configure(image=carddown, borderwidth=0)

                global livesRemaining
                livesRemaining-=1
                my_label3.configure (text=("You Have",livesRemaining, "Tries Left"))

                flipCount = 0
                flipped = [False, False, False, False, False, False, False, False]
                print(flipped)           
            
            if flipCount == 8:

                def returnmain():
                    end_window.destroy()
                    window1.destroy()

                def close1():
                    root.destroy()

                end_window=tk.Toplevel(root)
                end_window.title="Luigi's Game"
                label3 = tk.Label(end_window, text="You Won! \n What Would You Like To Do?")
                label3.grid()
                button8=tk.Button(end_window, text="Exit To Menu", height=2, width=10, bg="black", fg="black", command=returnmain, borderwidth=0)
                button8.grid(padx=80, pady=5)
                button10=tk.Button(end_window, text="Exit Game", height=2, width=10, bg="black", fg="black", command=close1,borderwidth=0)
                button10.grid(padx=80, pady=15)
                
            if livesRemaining == 0:

                def returnmain():
                    end_window.destroy()
                    window1.destroy()

                def close1():
                    root.destroy()

                end_window=tk.Toplevel(root)    
                end_window.title="Luigi's Game"
                label3 = tk.Label(end_window, text="You Lost \n What Would You Like To Do?")
                label3.grid()
                button8=tk.Button(end_window, text="Exit To Menu", height=2, width=10, bg="black", fg="black", command=returnmain, borderwidth=0)
                button8.grid(padx=80, pady=5)
                button10=tk.Button(end_window, text="Exit Game", height=2, width=10, bg="black", fg="black", command=close1,borderwidth=0)
                button10.grid(padx=80, pady=15)
        
        def clickCard0():
            card0.configure(image=coincard, borderwidth=0)
            flipped[0]=True
            cardcheck()
        def clickCard1():
            card1.configure(image=feathercard, borderwidth=0)
            flipped[1]=True
            cardcheck()
        def clickCard2():
            card2.configure(image=flowercard, borderwidth=0)
            flipped[2]=True
            cardcheck()
        def clickCard3():
            card3.configure(image=starcard, borderwidth=0)
            flipped[3]=True
            cardcheck()
        def clickCard4():
            card4.configure(image=feathercard, borderwidth=0)
            flipped[4]=True
            cardcheck()
        def clickCard5():
            card5.configure(image=coincard, borderwidth=0)
            flipped[5]=True
            cardcheck()
        def clickCard6():
            card6.configure(image=flowercard, borderwidth=0)
            flipped[6]=True
            cardcheck()
        def clickCard7():
            card7.configure(image=starcard, borderwidth=0)
            flipped[7]=True
            cardcheck()

        #boolean array list
        placed = [False, False, False, False, False, False, False, False]
        flipped = [False, False, False, False, False, False, False, False]

        button7.destroy()
        time.sleep(1)

        card0 = tk.Button(window1, image=carddown, width=65, height=100, borderwidth=0, command=clickCard0)
        card1 = tk.Button(window1, image=carddown, width=65, height=100, borderwidth=0, command=clickCard1)
        card2 = tk.Button(window1, image=carddown, width=65, height=100, borderwidth=0, command=clickCard2)
        card3 = tk.Button(window1, image=carddown, width=65, height=100, borderwidth=0, command=clickCard3)
        card4 = tk.Button(window1, image=carddown, width=65, height=100, borderwidth=0, command=clickCard4)
        card5 = tk.Button(window1, image=carddown, width=65, height=100, borderwidth=0, command=clickCard5)
        card6 = tk.Button(window1, image=carddown, width=65, height=100, borderwidth=0, command=clickCard6)
        card7 = tk.Button(window1, image=carddown, width=65, height=100, borderwidth=0, command=clickCard7)

        selection = randint(0,7)
        #position1
        if selection==0:
            card0.place(x=230, y=110)
        elif selection==1:
            card1.place(x=230,y=110)
        elif selection==2:
            card2.place(x=230, y=110)
        elif selection==3:
            card3.place(x=230, y=110)
        elif selection==4:
            card4.place(x=230, y=110)
        elif selection==5:
            card5.place(x=230, y=110)
        elif selection==6:
            card6.place(x=230, y=110)
        elif selection==7:
            card7.place(x=230, y=110)
        placed[selection] = True

        while True:
            selection=randint(0,7) # position 2
            if placed[selection] !=True:
            
                if selection==0:
                    card0.place(x=230, y=230)
                elif selection==1:
                    card1.place(x=230,y=230)
                elif selection==2:
                    card2.place(x=230, y=230)
                elif selection==3:
                    card3.place(x=230, y=230)
                elif selection==4:
                    card4.place(x=230, y=230)
                elif selection==5:
                    card5.place(x=230, y=230)
                elif selection==6:
                    card6.place(x=230, y=230)
                elif selection==7:
                    card7.place(x=230, y=230)
                placed[selection] = True
                break
        
        while True:
            selection=randint(0,7) #position 3
            if placed[selection] !=True:

                if selection==0:
                    card0.place(x=320, y=110)
                elif selection==1:
                    card1.place(x=320,y=110)
                elif selection==2:
                    card2.place(x=320, y=110)
                elif selection==3:
                    card3.place(x=320, y=110)
                elif selection==4:
                    card4.place(x=320, y=110)
                elif selection==5:
                    card5.place(x=320, y=110)
                elif selection==6:
                    card6.place(x=320, y=110)
                elif selection==7:
                    card7.place(x=320, y=110)
                placed[selection] = True
                break

        while True:
            selection=randint(0,7) #position 4
            if placed[selection] !=True:

                if selection==0:
                    card0.place(x=320, y=230)
                elif selection==1:
                    card1.place(x=320,y=230)
                elif selection==2:
                    card2.place(x=320, y=230)
                elif selection==3:
                    card3.place(x=320, y=230)
                elif selection==4:
                    card4.place(x=320, y=230)
                elif selection==5:
                    card5.place(x=320, y=230)
                elif selection==6:
                    card6.place(x=320, y=230)
                elif selection==7:
                    card7.place(x=320, y=230)
                placed[selection] = True
                break
        
        while True:
            selection=randint(0,7) #position 5
            if placed[selection] !=True:

                if selection==0:
                    card0.place(x=410, y=110)
                elif selection==1:
                    card1.place(x=410,y=110)
                elif selection==2:
                    card2.place(x=410, y=110)
                elif selection==3:
                    card3.place(x=410, y=110)
                elif selection==4:
                    card4.place(x=410, y=110)
                elif selection==5:
                    card5.place(x=410, y=110)
                elif selection==6:
                    card6.place(x=410, y=110)
                elif selection==7:
                    card7.place(x=410, y=110)
                placed[selection] = True
                break
        
        while True:
            selection=randint(0,7) #position 6
            if placed[selection] !=True:

                if selection==0:
                    card0.place(x=410, y=230)
                elif selection==1:
                    card1.place(x=410,y=230)
                elif selection==2:
                    card2.place(x=410, y=230)
                elif selection==3:
                    card3.place(x=410, y=230)
                elif selection==4:
                    card4.place(x=410, y=230)
                elif selection==5:
                    card5.place(x=410, y=230)
                elif selection==6:
                    card6.place(x=410, y=230)
                elif selection==7:
                    card7.place(x=410, y=230)
                placed[selection] = True
                break

        while True:
            selection=randint(0,7) #position 7
            if placed[selection] !=True:

                if selection==0:
                    card0.place(x=500, y=110)
                elif selection==1:
                    card1.place(x=500,y=110)
                elif selection==2:
                    card2.place(x=500, y=110)
                elif selection==3:
                    card3.place(x=500, y=110)
                elif selection==4:
                    card4.place(x=500, y=110)
                elif selection==5:
                    card5.place(x=500, y=110)
                elif selection==6:
                    card6.place(x=500, y=110)
                elif selection==7:
                    card7.place(x=500, y=110)
                placed[selection] = True
                break

        while True:
            selection=randint(0,7) #position 8
            if placed[selection] !=True:

                if selection==0:
                    card0.place(x=500, y=230)
                elif selection==1:
                    card1.place(x=500,y=230)
                elif selection==2:
                    card2.place(x=500, y=230)
                elif selection==3:
                    card3.place(x=500, y=230)
                elif selection==4:
                    card4.place(x=500, y=230)
                elif selection==5:
                    card5.place(x=500, y=230)
                elif selection==6:
                    card6.place(x=500, y=230)
                elif selection==7:
                    card7.place(x=500, y=230)
                placed[selection] = True
                break

    msg = messagebox.showinfo("Instructions", "How To Play: \n Select one card out of all the faced down cards.\n Click on one of the cards. \n Remember your chosen card.\n Try to match your card to another card! ")
    window1 = tk.Toplevel(root)
    window1.title("Luigi's Game")
    window1.geometry("800x400")
    my_label2 = tk.Label(window1, image=bg2, compound='top')   
    my_label2.place(x=0, y=0, relwidth=1, relheight=1)
    button7 = tk.Button(window1, image=beginb, width=215, height=80, bg="black", fg="black", command=cardp, font = font_button, borderwidth=0)
    button7.grid(padx=300, pady=180)

my_label = Label(root, image=bg, compound='top') #main menu background image
my_label.place(x=0, y=0, relwidth=1, relheight=1)

#Displaying Game Title
game_title = tk.Label(image=mayn, font = font_heading, borderwidth=0)
game_title.grid(padx=150, pady=10)
 # Pack it into the window

button = tk.Button(image=login_btn, width=215, height=80,command=hello, borderwidth=0) #play button
button.grid(padx=100, pady=30)

def window(): #instructions popup window
    def close2():
        extra_window.destroy()
        
    extra_window=tk.Toplevel(root)
    extra_window.title("Instructions") #Gives window a title
    label2 = tk.Label(extra_window, text="How To Play: \n Select one card out of all the faced down cards.\n Click on one of the cards. \n Remember your chosen card.\n Try to match your card to another card! ")
    label2.grid()
    button4 = tk.Button(
        extra_window,
        image=clo,
        width=100, height=40,
        bg="blue", fg="white",
        command=close2, font = font_button2, borderwidth=0
    )
    button4.grid(row=1, column=0, padx=100, pady=30)

button2 = tk.Button(image=instru, width=100, height=40, bg="Blue", fg="white",command=window, font = font_button2, borderwidth=0) #displays instructions
button2.grid()

def close():
    root.destroy()

def window2(): #exit popup window
    def close3():
        extra_window.destroy()

    extra_window=tk.Toplevel(root)
    extra_window.title("Exit") #Gives window a title
    label2 = tk.Label(extra_window, text="Are you sure you want to exit?", font = font_button)
    label2.grid(padx=80, pady=5)
    button5 = tk.Button(
        extra_window,
        image=yesb,
        width=100, height=40,
        bg="white", fg="black",
        command=close, font = font_button2, borderwidth=0
    )
    button5.grid(padx=100, pady=20)
    button6 = tk.Button(
        extra_window,
        image=nob,
        width=100, height=40,
        bg="white", fg="black",
        command=close3,
        font=font_button2, borderwidth=0
    )
    button6.grid(padx=100, pady=20)

button3 = tk.Button(image=exi, width=100, height=40, bg="blue", fg="white", command=window2, font = font_button2, borderwidth=0) #Closes the window
button3.grid(padx=50, pady=10)

root.mainloop()
