# Let's play rock, paper, scissors!
import random 

def play():
    choice = ['r', 'p', 's']
    name = input("Please enter your name: ")
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors! \n").lower()
    
    winner = ""
    while winner == "":
        computer = random.choice(choice)
        if user =='r':
            if computer == 'r':
                print("Draw! Try again ")
            elif computer == 's':
                winner = name
            elif computer == 'p':
                winner = "Computer"
        elif user == 'p':
            if computer == 'r':
                winner = name
            elif computer == 's':
                winner = "Computer"
            elif computer == 'p':
                print("Draw! Try again ")
        elif user == 's':
            if computer == 'r':
                winner = "Computer"
            elif computer == 's':
                print("Draw! Try again ")
            elif computer == 'p':
                winner = name
    print(f"The computer chose {computer} and you chose {user}. \n The winner is {winner}!")

play() 
    
def simple_play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors! \n").lower()
    computer = random.choice(['r', 'p', 's'])
    print(f"You chose {user} and the computer chose {computer}.\n")
    if user == computer:
        return print("It's a tie!\n")

    if win(user, computer):
        print("Congrats, you won!\n")
    else:
        print("The computer won.\n")

def win(player,opponent):
    # r > s, p > r, s > p
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
    

simple_play()
