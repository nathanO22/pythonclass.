
# a = [3, 4, 5, 6, 7, 4]
# from cmath import sqrt
# import math

# def number_checker(x:int): 
#     for i in range(2, int(sqrt(x)) + 1):
#         if x % i == 0:
#             return False
#     else:
#         return True
# print(number_checker(88))

s1 = "tech"
s2 = "chet"

def anagrams(s1, s2):
    if  (sorted(s1) == sorted(s2)):
        print("it is an anagram")
    else:
        print("not an anagram")
anagrams(s1, s2)




    