from random import randint



e = 5
ct = 10





def check_answer(guess,answer, turns):
    if guess > answer:
        print("too high. ")
        return turns - 1
    elif guess < answer:
        print("too low. ")
        return turns - 1
    else:
        print(f"you got it the answer is {answer}.")
        
        
def live_rest():
    d  = input("Choose a difficulty.Type easy or hard : ")

    if d =="hard":
        
        return e

    else:
        
        return ct

def game():
    print("Welcome to the Number Guessing Game! ")
    print("I'm thinking of a number between 1 and 100! ")
    answer = randint(1, 100)
    turns = live_rest()
    guess = 0
    while answer != guess:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("choose a number : "))
        turns = check_answer(guess,answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
            

game()