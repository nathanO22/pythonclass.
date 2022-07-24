

# import statistics
# populated = statistics.pstdev([6, 6, 3, 9, 4, 3, 6, 9, 7, 8])
# sample = statistics.stdev([6, 6, 3, 9, 4, 3, 6, 9, 7, 8])
# print(populated)
# print(sample)

# import statistics
# print(statistics.pvariance([6, 6, 3, 9, 4, 3, 6, 9, 7, 8]))
# print(statistics.variance([6, 6, 3, 9, 4, 3, 6, 9, 7, 8]))

# counts = { 'quincy' : "emma" , 'mrugesh' : "beauty", 'beau': "touch", '0': "hinn"}
# for keys,values in counts.items():
#     print(keys, values)

# c = {"a":10, "c":61, "d":78, "k":99, "m":65, "z":56}
# tmp = list()
# for k, v in c.items():
#     tmp.append( (v, k))
# print(tmp)
# tmp = sorted(tmp, reverse=True)
# print(tmp)


# from lingua import moer
# print(moer)
# counts = dict()
# for line in moer:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)

# lst = list()
# for key, val in counts.items():
#     newtup = (val, key)
#     lst.append(newtup)

# lst = sorted(lst, reverse=True)

# for val, key in lst[:10]:
#     print(key, val)
# import re
# for line in moer:
#     line = line.rstrip()
#     if re.search("the", line):
#         print(line)

# for number in range(1, 6):
#     for nums in range(1, number + 1):
#         print(nums, end= ' ')

#     print(" ")

# b = [10, 11, 11, 13, 12, 140,1,1,1,1,1,1,1,1, 12, 13, 13, 15, 15, 15, 15, 140, 140, 140, 140]

# counts = {}
# for value in b:
#     if value not in counts:
#         counts[value] = 1
#     else:
#         counts[value] = counts[value] + 1
# rearranged_list = []
# for key, value in counts.items():
#     rearranged_list.append((value,key))
# rearranged_list = sorted(rearranged_list, reverse=True)
# ba = []
# for v,k in rearranged_list:
#     ba.append((k))
# print(f"the most frequent value is: {ba[0]}")
    

# import random

# def guess_game(trial:int, score:int):
#     """This function allows users to guess what the computer has selected.j
    
    
#     Args:
#         trial (int): This is the total number of trials selected
#         score (int): This is the score of the user at the time of function call.
        
#     Returns:
#         trial (int): This is the total trials left after the function call
#         score (int): This is the total score left after the function call."""  
    
    
#     num = list(range(53, 60))
#     # random.shuffle(num)

#     print("You can select from the list below.")
#     print(num)
#     com_choice = random.choice(num)
#     user_choice = int(input(">"))

#     if user_choice in num:
#         if user_choice == com_choice:
#             print("You win!")
#             print("You just got an extra trial!")
#             score+=3
#         else:
#             trial -=1
#             if user_choice > com_choice:
#                 print("Too High")
#             else:
#                 print("Too low")
                
#         print(f"Computer choice: {com_choice}")
#     else:
#         trial -=1 
#         print("Invalid input")
#     return score, trial 


# def login(data:dict):
    
#     """This function takes a dictionary, asks the user for the name and adds their name to the dictionary.
    
#     Args:
#         data(dict) : This is the dictionary that stores the user data
    
#     Returns:
#         name (str): This is the name of the user
#     """
    
#     while True:
#         name = input("Name: ").lower()

#         if name in data.keys():
#             print("Name taken")
#         else:
#             data[name] = score
#             break   
#     return name

# trials = 3
# score = 0
# data = {}

# name = login(data)

# while trials > 0:
    

#     score, trials = guess_game(trials, score)
    
#     if trials == 0:
        
#         if score > data[name]:
#             print(f"Your new high score is {score}")
#             data[name] = score
#         else:
#             print(f"You scored {score} points.")
        
        
#         print("Do you want to play again? Y/n?")
#         rematch = input("> ").lower() 
        
#         if rematch == "y":
#             "Print welcome back"
#             trials = 3
#             score = 0

#             name = login(data)
#         else:
#             print("Game over!")


# print(data)       


import random
from random import randint


data = {}

with open("bank_data.txt", "r") as rsa:
    data = eval(rsa.read())

def number_generator():
    num = "0" + str(randint(0,999999999)).rjust(9, "0")
    return num

def pin_bb():
    pin = int(input("choose your 5-digit pin: "))
    return pin

def pin_vb():
    pin = int(input("choose your 4-digit pin: "))
    return pin

def name():
    first_name = input("what is your first name?: ").capitalize()
    last_name = input("what is your last name?: ").capitalize()
    if input("do you have a middle name?, (yes/no): ").lower() == "yes":
        middle_name = input("what is your middle name?, : ").capitalize()
        name = last_name + " "  + first_name + " " + middle_name
    else:
        name = last_name + " " + first_name
    print(name) 

def deposit():
    amount = float(input("Enter amount to be Deposited: "))
    data[acc_number]["balance"] += amount
    return "\n Amount Deposited:", amount

def continued():
    p = confirmation = int(input("enter your login pin: "))
    if confirmation == data[acc_number]["login_pin"]:
            print("what would like to do?")
            print("1. check account balance\n2. deposit\n3. withdrawal\n4. transfer money")
            transaction = int(input("select a number for your transaction: "))
            if transaction == 1:
                bal = balance()
                print(bal)
            elif transaction == 2:
                deposit()
            elif transaction == 3:
                withdraw()
            elif transaction == 4:
                transfer()
            else:
                print("invalid input")
            with open("bank_data.txt", "w") as rsa:
                rsa.write(str(data))
    return p

def transfer():
    acc_number12 = input("input beneficiary account number: ")
    if acc_number12 in data.keys():
        confirmation = int(input("enter your login pin: "))
        if confirmation == data[acc_number]["login_pin"]:
            amount = float(input("input amount to be transferred: "))
            data[acc_number12]["balance"] += amount
            data[acc_number]["balance"] -= amount
            return "you have successfully transferred", amount
        else:
            return "incorrect pin, try again."
    else:
        return "invalid account number, try again." 

def withdraw():
    amount = float(input("Enter amount to be Withdrawn: "))
    if data[acc_number]["balance"] >= amount:
        data[acc_number]["balance"] -= amount
        return " You Withdrew:", amount
    else:
        return " Insufficient balance  "
 
def balance():
    return "Net Available Balance=", data[acc_number]["balance"]





print("welcome to NN BANK")

account_status = input("do you have an account already?, (yes/no): ").upper()
if account_status == "NO":
    account_number = number_generator()
    if account_number not in data.keys():
        print("your account number:", account_number)
        first_name = input("what is your first name?: ").capitalize()
        last_name = input("what is your last name?: ").capitalize()
        pin = pin_vb()
        print(f"your transaction pin is {pin}\nkeep your pin safe.\nYour pin should be only known to you")
        pin2 = pin_bb()
        print(f"your login pin is {pin2}\nkeep your pin safe.\nYour pin should be only known to you")
        balance = 0
        print(f"your balance is {balance}")
        data.update({account_number:{"first_name": first_name,"last name": last_name,"transaction_pin": pin,"login_pin":pin2,"balance":balance}})
        with open("bank_data.txt", "w") as rsa:
            rsa.write(str(data))
elif account_status == "YES":
    acc_number = str(input("enter account number to confirm: "))
    if acc_number in data.keys():
        print("Good day", data[acc_number]["first_name"])
        confirmation = int(input("enter your login pin: "))
        if confirmation == data[acc_number]["login_pin"]:
            print("what would like to do?")
            print("1. check account balance\n2. deposit\n3. withdrawal\n4. transfer money")
            transaction = int(input("select a number for your transaction: "))
            if transaction == 1:
                bal = balance()
                print(bal)
            elif transaction == 2:
                print(deposit())
            elif transaction == 3:
                print(withdraw())
            elif transaction == 4:
                print(transfer())
            else:
                print("invalid input")
            with open("bank_data.txt", "w") as rsa:
                rsa.write(str(data))
            while input("do you want to perform another transaction?, (yes/no): ").lower() == "yes":
                continued()
        else:
            print("incorrect pin")
    else:
        print("account does not exist")
else:
    print("Invalid input")

