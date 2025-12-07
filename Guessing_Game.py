'''Building A Guessing Game'''

secret_number = 5
guess_count = 1
guess_limit = 3

while(guess_count <= guess_limit):
    guess = int(input("Make A Guess : "))
    guess_count += 1
    
    if (guess == secret_number):
        print("You Won!")
        break

else:
    print("Sorry You Failed!")    


    
