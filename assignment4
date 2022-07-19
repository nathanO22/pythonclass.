b = [10, 11, 11, 13, 12, 140, 15, 12, 13, 13, 15, 15, 15, 15, 15, 140, 140, 140, 140]

counts = {}

for value in b:
    if value not in counts:
        counts[value] = 1
    else:
        counts[value] = counts[value] + 1
# print(counts.items())
rearranged_list = []
for key, value in counts.items():
    rearranged_list.append((value,key))
# print(rearranged_list)
rearranged_list = sorted(rearranged_list, reverse=True)
# print(rearranged_list)
ba = []
for v,k in rearranged_list:
    ba.append((k))
print(f"the most frequent value is: {ba[0]}")
    



####### EXPLANATION  #######
#line 1-5, I created a dictionary for the values in the list(b)
# line 5-9, it basically just assigns new keys to the dictionary count on the condition that it does not exist before, and if it already exist then the value of the list be increased by 1
# 11 - 13; created a new list, then rearranges the key-value of the dictionary to value-key pair and adds the new arrangement to the list
# 15; it sorts the value from highest to lowest
# 17-20;  creates a new list from the sorted list that only displays the keys using the index
