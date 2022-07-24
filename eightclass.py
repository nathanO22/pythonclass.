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


###### QUESTION 4 ######
def standard_deviation(list_of_number):
    return variance(list_of_number)**0.5

def mode(ar):
    counts = {}
    for value in ar:
        if value not in counts:
            counts[value] = 1
        else:
            counts[value] = counts[value] + 1
    rearranged_list = []
    for key, value in counts.items():
        rearranged_list.append((value,key))
    rearranged_list = sorted(rearranged_list, reverse=True)
    ba = []
    for v,k in rearranged_list:
        ba.append((k))
    return ba[0]
        
    


arr = [16, 18, 18, 19, 17, 19, 20 ,18 , 21, 18, 19, 20, 18, 16, 17, 17, 19, 18, 17 ,16, 19]
means = "{: .2f}".format(mean(arr))
variances = "{: .2f}".format(variance(arr))
standard_deviations = "{: .2f}".format(standard_deviation(arr))

with open("report_log.txt", "w") as nf:
    nf.write(f"Mean age = {str(means)}\nMedian age = {str(median(arr))}\nThe most occuring age = {str(mode(arr))}\nThe variance of the given set of ages = {str(variances)}\nThe Standard deviation of the Ages = {str(standard_deviations)}")
    # print()
    # nf.write(f"mean of the ages = {str(mean(arr))}")
