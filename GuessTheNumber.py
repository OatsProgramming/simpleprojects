import random
import os

os.system('clear')

# User guesses
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number btwn 1 and {x}: "))
        if guess < random_number:
            print("Guess is too low. Try again.")
        elif guess > random_number:
            print("Guess is too high. Try again.")
    print(f"You got it right. You guessed {random_number}")
    user_input = None
    while not user_input:
        user_input = input('Wanna play again?(Y/N): ').lower().strip()
        if user_input == 'y':
            initiation()
        elif user_input == 'n':
            print("See ya next time then!")
            break
        else:
            print('Sorry, what was that? Please try again')
            user_input = None



#Now the guessing game for the computer
def computer_guess(x):
    low = 1
    high = x
    feedback = " "
    while feedback != "correct":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} ur number? Too high? Too low? or Correct?: ").lower().strip()
        # Pretty much binary search
        if feedback == "too high":
            high = guess - 1
        elif feedback == "too low":
            low = guess + 1
    print(f"Success. Your number was {guess}")
    user_input = None
    while not user_input:
        user_input = input('Wanna play again?(Y/N): ').lower().strip()
        if user_input == 'y':
            initiation()
        elif user_input == 'n':
            print("See ya next time then!")
            break
        else:
            print('Sorry, what was that? Please try again')
            user_input = None

        
def initiation():
    user_input = None
    while not user_input:
        user_input = input('Lets play the guessing game. Would you like for me (type computer) to guess or for you (type user) to guess?: ').lower().strip()
        if user_input == 'user':
            user_number = None
            while not user_number:
                try:
                    user_number = int(input('Give me a number any number thats at least one: '))
                except ValueError:
                    print('Sorry, thats not a valid integer. Please try again.')
                    user_number = None
                else:
                    print("Alright, here we go...")
                    guess(user_number)
                
        elif user_input == 'computer':
            user_number = None
            while not user_number:
                try:
                    user_number = int(input('Give me a number any number thats at least one: '))
                except ValueError:
                    print('Sorry, thats not a valid integer. Please try again.')
                    user_number = None
                else:
                    print("Alright, here we go...")
                    computer_guess(user_number)
        else:
            print('Sorry, I didnt quite get that. Please try again.')
            user_input = None

# For good practice
if __name__ == '__main__':
    initiation()
   