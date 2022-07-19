

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

b = [10, 11, 11, 13, 12, 140,1,1,1,1,1,1,1,1, 12, 13, 13, 15, 15, 15, 15, 140, 140, 140, 140]

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
    

