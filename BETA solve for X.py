#equation solver beta
#created by: Lucas McCarty
import Math
print ("WELCOME TO EQUATION SOLVER BETA")
print ("This program can solve simple equations following this model - integer (operand * or /) variable (operand + or -) integer2 = integer3")
print ("For example if the equation was 5x - 5 = 0 then the answer that the computer would give is X=1")
print ("once again the equation model is:  integer1 * or / variable + or - integer2 = integer3 ")
loop = True
while (loop):
       integer1 = float ( input( "Type integer1 and press enter"))
       integer2 = float ( input ( "Type integer2 and press enter"))
       integer3 = float ( input ( "Type integer3 and press enter"))
       operand1 = float (input ( "Type one and press enter for multiply or type two and press enter for divide"))
       operand2 = float ( input ( "Type in one and press enter for add or two and press enter for subtract"))
       if (operand2 == 1):
          integer4 = (integer3 - integer2)
          if (operand1 == 1):
             integer5 = (integer4/integer1)
             print ("the equation that you gave was: " + str(integer1) + "*" + "x" + " + " + str(integer2) + " = " + str(integer3)) 
             print ("X = " + str(integer5))
          elif  (operand1 == 2):
              integer5 = (integer4*integer1)
              print ("the equation that you gave was: " + str(integer1) + "/" + "x" + " + " + str(integer2) + " = " + str(integer3))
              print ("X = " + str(integer5))
          
       elif (operand2 == 2):
           integer4 = (integer3 + integer2)
           if (operand1 == 2):
               print ("the equation that you gave was: " + str(integer1) + "/" + "x" + " - " + str(integer2) + " = " + str(integer3))
               integer5 = (integer4*integer1)
               print ("X = " + str(integer5))
           elif (operand1 == 1):
             integer5 = (integer4/integer1)
             print ("the equation that you gave was: " + str(integer1) + "*" + "x" + " - " + str(integer2) + " = " + str(integer3))
             print ("X = " + str(integer5))

#Thats the entire program. It has been tested and it does work. It's only limitation is that it can only accept three integers.
#Some simplification might be needed before this program can be run.
            
                
                
       
       
    
