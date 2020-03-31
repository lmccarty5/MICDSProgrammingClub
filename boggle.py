#import statements
import random
import time
from tkinter import *
import winsound
from threading import *



#class for timer on one thread
class tim(Thread):
    def run(self):
        t=0
        while t<100:
            time.sleep(1)
            t=t+1
        #beep when countdown is finished
        frequency = 5000 # Set Frequency To 2500 Hertz
        duration = 500  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        time.sleep(0.5)
        winsound.Beep(frequency, duration)
        time.sleep(0.5)
        winsound.Beep(frequency, duration)
        print("You are out of time. Now count the number of words that you recognized. To play again, please restart the program.")




#class for main game on a second thread
class goodStuff(Thread):
    def run(self):
        window = Tk()
        window.title("Boggle")

        #function to determine what happens when the submit button is clicked
        def click():
            entered_text=textentry.get()
            print(entered_text)
            textentry.delete(0,END)


        #associated with timer. Allows the other thread to start when the start timer button is hit
        def tip():
            try:
                ti.start()
            except: #catches error if the thread is started twice
                print("To Play Another Game Or Reset the Timer, Please Rerun the Program")
            

        #this is building the dice:
        d0 = ['R', 'I', 'F', 'O', 'B', 'X']
        d0num = random.randint(0,5)
        d0let = d0[d0num]

        d1 = ['i','f','e','h','e','y']
        d1num = random.randint(0,5)
        d1let = d1[d1num]

        d2 = ['d','e','n','o','w','s']
        d2num = random.randint(0,5)
        d2let = d2[d2num]

        d3 = ['u','t','o','k','n','d']
        d3num = random.randint(0,5)
        d3let = d3[d3num]

        d4 = ['h','m','s','r','a','o']
        d4num = random.randint(0,5)
        d4let = d4[d4num]

        d5 = ['l','u','p','e','t','s']
        d5num = random.randint(0,5)
        d5let = d5[d5num]

        d6 = ['a','c','i','t','o','a']
        d6num = random.randint(0,5)
        d6let = d6[d6num]

        d7 = ['y','l','g','k','u','e']
        d7num = random.randint(0,5)
        d7let = d7[d7num]

        d8 = ['Qu','b','m','j','o','a']
        d8num = random.randint(0,5)
        d8let = d8[d8num]

        d9 = ['e','h','i','s','p','n']
        d9num = random.randint(0,5)
        d9let = d9[d9num]

        d10 = ['v','e','t','i','g','n']
        d10num = random.randint(0,5)
        d10let = d10[d10num]

        d11 = ['b','a', 'l','i','y','t']
        d11num = random.randint(0,5)
        d11let = d11[d11num]

        d12 = ['e','z','a','v','n','d']
        d12num = random.randint(0,5)
        d12let = d12[d12num]

        d13 = ['r','a','l','e','s','c']
        d13num = random.randint(0,5)
        d13let = d13[d13num]

        d14 = ['u','w','i','l','r','g']
        d14num = random.randint(0,5)
        d14let = d14[d14num]

        d15 = ['p','a','c','e','m','d']
        d15num = random.randint(0,5)
        d15let = d15[d15num]

        #this part assigns the grid spots
        g = [d0let, d1let, d2let, d3let, d4let, d5let, d6let, d7let, d8let, d9let, d10let, d11let, d12let, d13let, d14let, d15let]

        g11 = g[random.randint(0,(len(g)-1))]
        g.remove(g11)

        g12 = g[random.randint(0, (len(g)-1))]
        g.remove(g12)

        g13 = g[random.randint(0,(len(g)-1))]
        g.remove(g13)

        g14 = g[random.randint(0, (len(g)-1))]
        g.remove(g14)
        
        g21 = g[random.randint(0, (len(g)-1))]
        g.remove(g21)

        g22 = g[random.randint(0, (len(g)-1))]
        g.remove(g22)

        g23 = g[random.randint(0, (len(g)-1))]
        g.remove(g23)

        g24 = g[random.randint(0, (len(g)-1))]
        g.remove(g24)

        g31 = g[random.randint(0, (len(g)-1))]
        g.remove(g31)

        g32 = g[random.randint(0, (len(g)-1))]
        g.remove(g32)

        g33 = g[random.randint(0, (len(g)-1))]
        g.remove(g33)

        g34 = g[random.randint(0, (len(g)-1))]
        g.remove(g34)

        g41 = g[random.randint(0, (len(g)-1))]
        g.remove(g41)
        g42 = g[random.randint(0, (len(g)-1))]
        g.remove(g42)

        g43 = g[random.randint(0, (len(g)-1))]
        g.remove(g43)

        g44 = g[random.randint(0, (len(g)-1))]
        g.remove(g44)

        window.configure(backgroun = "black")

        #instructions for game at top of game window
        Label (window, text="Welcome to boggle. Below and to the right is a 4x4 grid of letters.", bg="black", fg = "white", font = "none 12 bold") .grid(row=0, column=0, sticky=N)

        Label (window, text="Your goal is to find as many words as possible by connecting ajacent and diagonal letters.", bg="black", fg = "white", font = "none 12 bold") .grid(row=1, column=0, sticky=N)

        Label (window, text="You have three minutes to generate words after hitting the start timer button.", bg="black", fg = "white", font = "none 12 bold") .grid(row=2, column=0, sticky=N)

        Label (window, text="Good Luck! Go find some words!", bg="black", fg = "white", font = "none 12 bold") .grid(row=3, column=0, sticky=N)


        #Code for recording the words that you come up with in the main program window
        Label (window, text="\nPlease type any words that you think of into the following text entry box:", bg="black", fg = "white", font = "none 12 bold") .grid(row=20, column=0, sticky=N)
        textentry = Entry(window, width = 20, bg = "white")
        textentry.grid(row=21, column=0, sticky=N)
        Button(window, text="SUBMIT", width = 6, command= click).grid(row=22,column=0,sticky=N)


        #large font random letter selection
        Label (window, text=g11 + "  ", bg="black", fg = "white", font = "none 48 bold") .grid(row=5, column=0, sticky=E)
        Label (window, text=g12 + "  ", bg="black", fg = "white", font = "none 48 bold") .grid(row=5, column=1, sticky=E)
        Label (window, text=g13 + "  ", bg="black", fg = "white", font = "none 48 bold") .grid(row=5, column=2, sticky=E)
        Label (window, text=g14 + "  ", bg="black", fg = "white", font = "none 48 bold") .grid(row=5, column=3, sticky=E)

        Label (window, text=g21 + "  ", bg="black", fg = "white", font = "none 48 bold") .grid(row=6, column=0, sticky=E)
        Label (window, text=g22 + "  ", bg="black", fg = "white", font = "none 48 bold") .grid(row=6, column=1, sticky=E)
        Label (window, text=g23 + "  ", bg="black", fg = "white", font = "none 48 bold") .grid(row=6, column=2, sticky=E)
        Label (window, text=g24 + "  ", bg="black", fg = "white", font = "none 48 bold") .grid(row=6, column=3, sticky=E)

        Label (window, text=g31 + "  ", bg="black", fg = "white", font = "none 48 bold") .grid(row=7, column=0, sticky=E)
        Label (window, text=g32 + "  ", bg="black", fg = "white", font = "none 48 bold") .grid(row=7, column=1, sticky=E)
        Label (window, text=g33 + "  ", bg="black", fg = "white", font = "none 48 bold") .grid(row=7, column=2, sticky=E)
        Label (window, text=g34 + "  ", bg="black", fg = "white", font = "none 48 bold") .grid(row=7, column=3, sticky=E)

        Label (window, text=g41 + "  ", bg="black", fg = "white", font = "none 48 bold") .grid(row=8, column=0, sticky=E)
        Label (window, text=g42 + "  ", bg="black", fg = "white", font = "none 48 bold") .grid(row=8, column=1, sticky=E)
        Label (window, text=g43 + "  ", bg="black", fg = "white", font = "none 48 bold") .grid(row=8, column=2, sticky=E)
        Label (window, text=g44 + "  ", bg="black", fg = "white", font = "none 48 bold") .grid(row=8, column=3, sticky=E)


        #start timer button
        Button(window, text="START TIMER", width = 20, command= tip).grid(row=14,column=0,sticky=N)

        #start the window
        window.mainloop()


#create two separate objects for each of the classes
bigboy = goodStuff()
ti = tim()


#start main thread
bigboy.start()









