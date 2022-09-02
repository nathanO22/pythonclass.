###### QUESTION 1 ######

a = float(input(" Please Enter the First Number: ")) 
b = float(input(" Please Enter the second number: "))
c = float(input(" Please Enter the third number: "))
sum_of_three = (a + b + c)
frequency = 3
average = sum_of_three / frequency

print("The average of the three numbers is", average)

###### QUESTION 2 ######
sentence = (input("Please Enter Any Sentence: "))
new_sent = sentence.capitalize()
print(new_sent)


###### QUESTION 3 ######
my_sentence = "I am learning python"
my_new_sent = my_sentence.replace("I", "you")
print(my_new_sent)

###### QUESTION 4 ######

first_string = "i hope you had fun today in class"
num1 = first_string.count("a")

print("the number of 'a's in the sentence is", num1)


###### QUESTION 5 ######
#Fermat’s Last Theorem says that there are no positive integers a, b, and c such that a^n + b^n = c^n for any values of n greater than 2

def check_fermat(a, b, c, n):
    if n > 2 and (a**n + b**n) == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("no that does'nt work")

print(check_fermat(4, 6, 8, 30))

###### QUESTION 6 ######

def check_numbers():
    a = int(input("Choose a number for a: "))
    b = int(input("Choose a number for b: "))
    c = int(input("Choose a number for c: "))
    n = int(input("Choose a number for n: "))
    return check_fermat(a, b, c, n)

print(check_numbers())



