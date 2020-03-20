
import random
minimumValue = int
maximummValue = int

loop = True
print ("WELCOME TO THE RANDOM NUMBER GUESSING GAME")


while (loop == True):
    minimumValue = float(input("please type in a minimum value for the random number generator"))
    maximumValue = float(input("please type in a maximum value for the random numver generator"))
    number = random.randint((minimumValue),(maximumValue))
    print ("Start Guessing!")
    loop2 = True
    count = 1;

    while (loop2 == True):
        guess = float (input("Type in your guess: "))
        if (guess > number):
            print ("Too high :(")
            count = count + 1;
        
        if (guess < number):
            print ("Too low :)")
            count = count + 1;

        if (guess == number):
            print ("You got it! :)")
            print("You took " + (str(count)) + " guesses")
            loop2 = False
    print ("Want to play again?")
    terminate = int(input("Type 1 and hit enter to terminate this program, or type any other integer and hit enter to play again"))
    if (terminate == 1):
        loop = False
        print ("Thanks for playing! :)")

    else:
        loop = True

            
        

            

                      
                
    
