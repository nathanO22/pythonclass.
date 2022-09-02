
string = "50"
number = 10
my_new_int = int(string)
print(my_new_int)
print(type(my_new_int))
print(my_new_int + number)
a = 10
b = 5
print(a != b)

π = 3.142
r = 5
x = (4 * π * r**3)
y = 3
print(x / y)

cover_price = 24.95 * 0.6 
cover_price = 14.95
first_copy_cost = 3
additional_price_for59 = (59 * 0.75)
additional_price_for60copies =first_copy_cost + additional_price_for59
cover_price_for60 = 60 * 14.97
overall_cost = (additional_price_for60copies + cover_price_for60)
print(overall_cost)

###### question 3 ######
start_time = (6*60 + 52) *60
easy_pace = (8*60 + 15) *2
tempo_pace = (7*60 + 12) *3

run_time = easy_pace + tempo_pace

home_time = start_time + run_time

break_fast_hour = home_time//3600
break_fast_min = (home_time%3600) //60
break_fast_sec = (home_time%3600) % 60

print(f"{break_fast_hour}:{break_fast_min}:{break_fast_sec}am")

status = "i am very hungry o, "
question = "when is the break time, "
status_quo = "the package has landed boys."
print(status + question +status_quo)

 ##### classwork #####
first_name = "nathaniel"
last_name = "olowu"
f = first_name[6:9]
y = last_name[0:3]
username = f + y
print(username)
first_name = first_name[6:9]

strung = "dolapo"
print(strung.lower())
print(strung.upper())
print(strung.title())
print(strung.capitalize())
print(strung.count("a"))
bo = strung.replace("dolapo", "nathan")
print(bo)