#### QUESTION 1 ####
def mean(list_of_numbers):
    total = 0
    for numbers in list_of_numbers:
        total += numbers
    return total / len(list_of_numbers)
     
######### OR ##############
# def mean_number(*numbers):
#     numerator = sum(numbers)
#     denominator = len(numbers)
#     mean = numerator2/denominator2
#     return mean


##### QUESTION 2 ######

def median(list_of_numbers):
    list_of_numbers.sort()
    if len(list_of_numbers) % 2 == 1:
        middle_num = int((len(list_of_numbers) -1) / 2)
        return list_of_numbers[middle_num] 
    elif len(list_of_numbers) % 2 == 0:
        middle_num1 = int(len(list_of_numbers) / 2)
        middle_num2 = int(len(list_of_numbers) / 2) -1
        mean_of_median = mean([list_of_numbers[middle_num1],list_of_numbers[middle_num2]])
        return mean_of_median


# print(median([6,4,4,4,5,8,9,10,90,58]))

##### QUESTION 3 ######
def variance(list_of_numbers):
    """this function calculates the variance of a given list of numbers
    formula for variance is: s**2 = sum(x1 - x2) / n
        where s is the variance
        x1  is the value of a number in the observation, represented by "x"
        x2 is the mean value of the list value, represented by "mean" 
        n is the total number of value in the list of numbers, represented by "numb"
    
    """
    numb = len(list_of_numbers)
    mean = sum(list_of_numbers) / numb
    dev = [(x - mean) ** 2 for x in list_of_numbers]
    variance = (sum(dev) / numb)
    return variance

# print(variance([6, 6, 3, 9, 4, 3, 6, 9, 7, 8]))

###### QUESTION 4 ######
def standard_deviation(list_of_number):
    return variance(list_of_number)**0.5


def skewness(list_of_numbers):
    numb = len(list_of_numbers)
    mean = sum(list_of_numbers) / numb
    dev = [(x - mean)**3 for x in list_of_numbers]
    dev2 = sum(dev)
    dem = numb * standard_deviation(list_of_numbers)**3
    sknw = dev2 / dem
    return sknw 

print(skewness([6, 6, 3, 9, 4, 3, 6, 9, 7, 8]))

