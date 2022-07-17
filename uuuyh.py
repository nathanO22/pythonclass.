

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


from lingua import moer
print(moer)
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
import re
for line in moer:
    line = line.rstrip()
    if re.search("the", line):
        print(line)


