import random 
import time 
print('WELCOME TO MY GUESS GAME!!')
time.sleep(1)
print('How to play: guess the randomly obtained number correctly and get 100 points')
time.sleep(2)
name = input('what is your name: ').upper()
time.sleep(1.5)
print(f'WELCOME {name}')


def guess_game():
    num1 = list(range(67, 75))
    score = 0
    games_played = 0
    limit = 5
    st = "start"
    while st == "start":
        print(num1)
        user_choice = int(input('Enter your guess: '))
        com_choice = random.choice(num1)    
        if user_choice in num1:
            print()
            print(f'computer pick: {com_choice}')
            if user_choice == com_choice:
                score += 100
                print('correct!, You won!, 100 points added to total score')
                print(f'you have {limit} trial(s) left')
                print()
            else:
                limit -= 1
                print('wrong!, Try again')
                print(f'you have {limit} trial(s) left')
                print()
        else:
            print('invalid input')      
    
        if limit == 0:
            games_played += 1
            continue1 = input('if you wish to continue insert "yes" or insert anything to stop: ').lower()
            if continue1 == "yes":
                limit = 5
                continue
            else:
                print(f'Total points accumulated: {score}')
                print(f'Total correct guess(es): {score//100}')
                print(f'Total game played: {games_played}')     
                break
    while input("Do you want to play again (Y/N): ").upper() == "Y":
        return guess_game()
    print("GOODBYE :)")

guess_game()