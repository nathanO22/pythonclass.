# person = input("Nationality?: ").lower()

# if person == "french" or person == "francais":
#     name = input("comment tu t'appelle? ").title()
#     going_to_school = input("Alez-vous a l'ecole? ")
#     if going_to_school == "yes":
#             print(f"Bienvenue chez au univelcity, {name}.")
#     else:
#             print("Au revoir, {name}. Bonne journee")
# elif person == "italian":
#     print("Preferisci parlare italiano?")
# else:
#     print("You are neither French nor Italian.")
#     print("So let us speak English!") 

# def factorial(n):
#     if n == 1:
#         return 1
    
#     return n * factorial(n-1)

# print(factorial(7))

# my_list = [4, 5 , 78, 7, 69, 18, 60]
# print(my_list) 

# my_list[5]= 100
# print(my_list)
import random
def guess_game():
    print("welcome to guess the number")
    num1 = list(range(67, 90))
    random.shuffle(num1)
    print(num1)
    lives = 7
    user_choice = int(input("Select a number from the given set of number: "))
    com_choice = random.choice(num1)
    
    if user_choice in num1:
        if user_choice == com_choice:
            print("Brilliant, you guessed right")
        elif user_choice > com_choice:
                print("Too high")
                print("try again")
        else:
            print("Too low")
            print("try again")
        print(com_choice)
    else:
        print("invalid input")
    while input("do you want to play again (Y/N)?: ").upper() == "Y":
        return guess_game()
    print("goodbye")
guess_game()