# A Digital Version of Boggle
# Author: LmcCarty




#import statements
import random
import time
from tkinter import *
import winsound
from threading import *
import tkinter as tk
import tkinter.messagebox



class timVar:
    countdown = 5




class Application(tk.Frame):
    """"Simple timer application using tkinter."""



    def fireitup():
        """Main loop which creates program."""
        global root
        root = tk.Tk()
        root.title("TIMER")
        Application(root).pack(side="top", fill="both", expand=True)
        root.mainloop()
        
    def JustDoIt():
        Application.reset()
        Application.start()




    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.running = False
        self.time = 180
        self.hours = 0
        self.mins = 3
        self.secs = 0
        self.build_interface()

    def build_interface(self):
        """The interface function."""
        self.time_entry = tk.Entry(self)

        self.clock = tk.Label(self, text="00:03:00", font=("Courier", 20), width=10)
        self.clock.grid(row=1, column=1, stick="S")

        self.time_label = tk.Label(self, text="hour min sec", font=("Courier", 10), width=15)
        self.time_label.grid(row=2, column=1, sticky="N")

        self.power_button = tk.Button(self, text="Start", command=lambda: self.start())
        self.power_button.grid(row=3, column=0, sticky="NE")

        self.reset_button = tk.Button(self, text="Reset", command=lambda: self.reset())
        self.reset_button.grid(row=3, column=1, sticky="NW")

        self.quit_button = tk.Button(self, text="Quit", command=lambda: self.quit())
        self.quit_button.grid(row=3, column=3, sticky="NE")

        self.master.bind("<Return>", lambda x: self.start())
        self.time_entry.bind("<Key>", lambda v: self.update())

    def calculate(self):
        """Calculates the time"""
        self.hours = self.time // 3600
        self.mins = (self.time // 60) % 60
        self.secs = self.time % 60
        return "{:02d}:{:02d}:{:02d}".format(self.hours, self.mins, self.secs)

    def update(self):
        """Checks if valid time entered and updates the timer"""
        self.time = int(self.time_entry.get())
        try:
            self.clock.configure(text=self.calculate())
        except:
            self.clock.configure(text="00:00:00")

    def timer(self):
        """Calculates the time to be displayed"""
        frequency = 5000 # Set Frequency To 2500 Hertz
        duration = 500  # Set Duration To 1000 ms == 1 second
        if self.running:
            if self.time <= 0:
                print("Game End: _____________________________________________________")
                print("You are out of time. Now count the number of words that you recognized. To play again, please restart the timer.")
                self.clock.configure(text="Time's up!")
                winsound.Beep(frequency, duration)
                time.sleep(0.5)
                self.clock.configure(text="Time's up!")
                winsound.Beep(frequency, duration)
                time.sleep(0.5)
                self.clock.configure(text="Time's up!")
                winsound.Beep(frequency, duration)

            else:
                self.clock.configure(text=self.calculate())
                self.time -= 1
                self.after(1000, self.timer)

    def start(self):
        """Begins the timer"""
        try:
            print("Game Start: __________________________________________________")
            self.time = int(self.time_entry.get())
            self.time_entry.delete(0, 'end')
        except:
            self.time = self.time
        self.power_button.configure(text="Stop", command=lambda: self.stop())
        self.master.bind("<Return>", lambda x: self.stop())
        self.running = True
        self.timer()

    def stop(self):
        """Stops the timer"""
        self.power_button.configure(text="Start", command=lambda: self.start())
        self.master.bind("<Return>", lambda x: self.start())
        self.running = False

    def reset(self):
        """Resets the timer to 0."""
        print("Game Reset: __________________________________________________")
        self.power_button.configure(text="Start", command=lambda: self.start())
        self.master.bind("<Return>", lambda x: self.start())
        self.running = False
        self.time = 180
        self.clock["text"] = "00:03:00"

    def quit(self):
        """Ask user if they want to close program."""
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()
            print("Timer End: __________________________________________________")





#class for timer on one thread
class tim(Thread):

    
    def run(self):
        Application.fireitup()






#class for main game on a second thread
class goodStuff(Thread):

    initial = True

    timerPrinter = str(timVar.countdown)
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
                if(goodStuff.initial==True):
                    ti.start()
                    goodStuff.initial = False;
                else:
                   print("The timer has already been opened. Please use the opened timer window to control the timer or restart the program to open another timer.")
            except:
                print("To open another timer, please restart the program")

            

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
        Button(window, text="OPEN TIMER", width = 20, command= tip).grid(row=14,column=0,sticky=N)

     
        



        def pop():
            if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
                window.destroy()
                print("Program End: _____________________________________________________")


            

       #kill window button button
        Button(window, text="KILL PROGRAM", width = 25, command= pop).grid(row=17,column=0,sticky=N)

        

        


        #start the window
        window.mainloop()

        


#create two separate objects for each of the classes
bigboy = goodStuff()
ti = tim()


#start main thread
bigboy.start()










