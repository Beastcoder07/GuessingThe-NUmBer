
import random
num=random.randint(1,10)
print("THe GUEssing GAMe")
print("Guess a number between 1 to 10")

chances=4  
while chances > 1:
    print("chances number", 5-chances)
    guess=int(input("enter your guess"))
    if guess==num:
        print("U defeated the code created by a 15year old in other words u WONNNN ")
        break
    elif guess<num:
       print("U guessed a low number , chose a higher number than this",guess) 
       chances=chances-1
    elif guess<num:
       print("U guessed a high number , chose a lower number than this",guess) 
       chances=chances-1   
    else:
        chances=chances-1
        break
if not chances >1:
    print("u LOST to A code created by a 15year old well Better LUCK next time and the anSwer is ",num)    
       


