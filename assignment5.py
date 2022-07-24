import random
from random import randint


data = {}

with open("bank_database.txt", "r") as rsa:
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
    return "Amount Deposited:", amount

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
            print(deposit())
        elif transaction == 3:
            print(withdraw())
        elif transaction == 4:
            print(transfer())
        else:
            print("invalid input")
        with open("bank_database.txt", "w") as rsa:
            rsa.write(str(data))
    else:
        return "incorrect pin"
    return p

def transfer():
    acc_number12 = input("input beneficiary account number: ")
    if acc_number12 in data.keys():
        confirmation = int(input("enter your transaction pin: "))
        if confirmation == data[acc_number]["transaction_pin"]:
            amount = float(input("input amount to be transferred: "))
            data[acc_number12]["balance"] += amount
            data[acc_number]["balance"] -= amount
            return "you have successfully transferred", amount
        else:
            return "incorrect pin, try again."
    else:
        return "invalid account number, try again." 

def withdraw():
    confirmation = int(input("enter your transaction pin: "))
    if confirmation == data[acc_number]["transaction_pin"]:
        amount = float(input("Enter amount to be Withdrawn: "))
        if data[acc_number]["balance"] >= amount:
            data[acc_number]["balance"] -= amount
            return " You Withdrew:", amount
        else:
            return " Insufficient balance  "
    else:
        return "incorrect pin, try again"
 
def balance():
    confirmation = int(input("enter your transaction pin: "))
    if confirmation == data[acc_number]["transaction_pin"]:
        return "Net Available Balance=", data[acc_number]["balance"]



start = "st"

print("welcome to NN BANK")
while start == "st":
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
            with open("bank_database.txt", "w") as rsa:
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
                with open("bank_database.txt", "w") as rsa:
                    rsa.write(str(data))
                while input("do you want to perform another transaction?, (yes/no): ").lower() == "yes":
                    print(continued())
            else:
                print("incorrect pin")
        else:
            print("account does not exist")
    else:
        print("Invalid input")
    break
print("Goodbye, Have a nice day!")   




