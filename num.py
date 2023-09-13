import random

#METHOD 1
""" play_again = True
while play_again:
    print("Welcome to the number guessing game")
    print("I'm thinking of a number between 1 to 100")
    
    #Function to choose level of difficulty
    def difficulty():
        global number_of_guesses
        level = input("Choose Difficulty Type 'Easy' or 'Hard':").lower()
        if level == 'easy':
            number_of_guesses = 10 
        elif level == 'hard':
            number_of_guesses = 5
        else:
            return
        print(f"You have {number_of_guesses} remaining")
        
    difficulty()
    
    play_game = True
    while play_game:
        user_guess = int(input("Make a guess:"))
        answer = random.randint(1, 100)
        #print(answer)
        if answer != user_guess:
            number_of_guesses -= 1
            if user_guess > answer:
                print(f"{user_guess} is too high! You have {number_of_guesses} attempts remaining to guess")
            elif user_guess < answer:
                print(f"{user_guess} is too low! You have {number_of_guesses} attempts remaining to guess")
        else:
            play_game = False
                
        if user_guess == answer:
            print(f"Congratulations you got it right! The answer was {answer}")
        elif number_of_guesses == 0:
            print(f"You have ran out of guesses. The answer was {answer}")
            play_game = False
    
    try_again = input("Would you like to continue? Type 'y' or 'n':").lower()
    if try_again != 'y':
        play_again = False
         """

#Method 2

from random import randint



EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
def difficulty():
    
    level = input("Choose difficulty. Type 'easy' or 'hard':").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    
    
    
def check_answer(guess,answer,turns):
    if guess > answer:
        print("Too high!")
       
        return turns - 1
        
        
    elif guess < answer:
        print("Too low!")
        
        return turns - 1
    elif guess == answer:
        print(f"You got it right! The answer is {answer}")


def game():
    
    print("Welcome to the number guessing game")
    print("I'm thinking of a number between 1 to 100")
    turns = difficulty()
    #print(f"You have {turns} remaining to guess the number")
    
    comp_answer = randint(1, 100) 
    print(comp_answer)
    guess = 0
    while guess != comp_answer:
        if turns == 0:
            print("You have ran out of guesses. You lose!")
            break
        else:
            print(f"You have {turns} attempts remaining to guess the number")
            guess = int(input("Make a guess:"))
        
        turns = check_answer(guess,comp_answer,turns)
    
    
    
game()
    
    
    