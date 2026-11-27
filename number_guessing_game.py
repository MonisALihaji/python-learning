        
import random        
            
print("Welcome to Number Guessing Game!\nI'm thinking of a number between 1 and 100.")      

difficulty=input("Choose a difficulty: Type \"easy\" or \"hard\": ").lower().strip()      

computer_guess=random.randint(1,100)            

# print(computer_guess)  -----if yo want to win everytime  uncomment this line😂
    
if difficulty =="easy":
    attempts=10
    
    for i in range (10):
        print(f"You have {attempts} attempts remaining to guess the number. ")
        Guess=int(input(f"Make a guess: "))
        
        attempts-=1    
    
        if computer_guess>Guess:
            print("guess higher")
        
        elif computer_guess<Guess:
            print("guess lower")
                    
        else:
            print(f"You won!")  
            break   
        if attempts>0:
            print("guess again")
    else:     
        print(f"You ran out of chances.\n Heheheh  number was {computer_guess}. Better luck next time 😂")
                    
                
        
        
elif difficulty =="hard":
    attempts=5
    
    
    
    for i in range (5):
        print(f"You have {attempts} attempts remaining to guess the number. ")
    
        Guess=int(input(f"Make a guess: "))
        attempts -=1
        
        if computer_guess>Guess:
            print("guess higher")
        
        elif computer_guess<Guess:
            print("guess lower")
            
        else:
            print(f"You won!")  
            break 
        
        if attempts>0:
            print("guess again")
    
    else:    
        
        print(f"You ran out of chances.\n Heheheh  number was {computer_guess}. Better luck next time 😂")
                    
            


    
    

            

        