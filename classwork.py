# import random
# import time


# print("welcome to rock, paper, scissors")
# name = input("Enter Your Name: ").upper()
# time.sleep(1)

# print(f"Hello {name}, shall we play?")
# time.sleep(2)

# print("rules:\n Scissors beats paper \n Paper beats rock \n Rock beats scissors")
# print("The game is about to start!")
# print("Let's play Hangman!")
# time.sleep(3)

# s = "scissors"
# r = "rock"
# p = "paper"
# list1 = [s, r, p]
# computer_choice = random.choice(list1)
# players_choice = input("what are you throwing: ").lower()


# for player_choice in list1:
#     if players_choice not in computer_choice:
#         print("invalid input")

#     if computer_choice == p and players_choice == s:
#         print(f"you win, computer chose: {computer_choice}")
#     elif computer_choice == p and players_choice == r:
#             print("computer won, you lose!")
#     else:
#         print("it's a tie, try again")

#     if computer_choice == r and players_choice == p:
#         print(f"you win, computer chose: {computer_choice}")
#     elif computer_choice == r and players_choice == s:
#         print(f"computer won, you lose!, computer chose: {computer_choice}")
# #     else:
#         print("it's a tie!, try again") 

    # if computer_choice == s and players_choice == p:
    #     print(f"you win, computer chose: {computer_choice}")
    # elif  computer_choice == s and players_choice == r:
    #         print(f"computer won, you lose!, computer chose: {computer_choice}")
    # else: 
    #     print("it's a tie, try again")


array1 = (input("enter numbers: ")).split(",")
array2 = list(array1)
print(array2)
mapped  = map(int, array2)


