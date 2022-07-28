import random, os

os.system('clear')

def initiation():
    user_input = None
    while not user_input:
        user_input = input('Hey there! Wanna play rock, paper, scissors?(Y/N): ').lower().strip()
        if user_input == 'y':
            print("Alright, let's go!")
            play()
        elif user_input == 'n':
            print("Oh, alright. Maybe next time. See ya later!")
            break
        else:
            print("Sorry what was that? Please try again")
            user_input = None
    
def play():
    user_input = None
    while not user_input:
        user_input = input("Choose 'r' for rock, 'p' for paper, 's' for scissors: ").lower().strip()
        computer = random.choice(['r', 'p', 's'])
        if user_input == computer:
            print('Its a tie!')
        elif winner(user_input, computer):
            print('Aw, you won')
        elif not winner(user_input, computer):
            print("I won!")
    play_again()

def winner(user, computer):
    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        return True
    else:
        return False

def play_again():
    user_input = None
    while not user_input:
        user_input = input('Wanna play again?(Y/N): ').lower().strip()
        if user_input == 'y':
            print("Sweet! Lets go")
            play()
        elif user_input == 'n':
            print("Aw, okay. Next time then! See ya")
            break
        else:
            print("What was that? Sorry I dont what you said")
            user_input = None

if __name__ == '__main__':
    initiation()