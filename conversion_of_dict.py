"""
# Que.1 Convert Key-Value list Dictionary to List of Lists
# Using loop + items()
td = {'shiv': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
print('The original dictionary is:', td)
res = []
for key, val in td.items():
    res.append([key] + val)
print('The converted list is:', res)

or
# Using list comprehension
td = {'shiv': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
print('The original dictionary is:', td)
res = [[key] + val for key, val in td.items()]
print('The converted list is:', res)

or
# Using map and dict.keys()
td = {'shiv': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
print('The original dictionary is:', td)
temp1 = list(td.keys())
res = list(map(lambda i: [i] + td[i], temp1))
print('The converted list is:', res)
========================================================================

# Que.2 Convert List to List of dictionaries
# Using dict comprehension + loop
tl = ['Shiv', 3, 'is', 8, 'Best', 10, 'for', 18, 'Study', 33]
print('The original list:', tl)
key_list = ['name', 'number']
n = len(tl)
res = []
for idx in range(0, n, 2):
    res.append({key_list[0]: tl[idx], key_list[1]: tl[idx + 1]})
print('The constructed dictionary list:', res)

or
# Using zip() + list comprehension
tl = ['Shiv', 3, 'is', 8, 'Best', 10, 'for', 18, 'Study', 33]
print('The original list:', tl)
key_list = ['name', 'num']
n = len(tl)
res = [{key_list[0]: tl[idx], key_list[1]: tl[idx + 1]}
       for idx in range(0, n, 2)]
print('The constructed dictionary list:', res)
================================================================

# Que.3 Convert Lists of List to Dictionary
# Using loop
ls = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
print('The original list is:', ls)
res = dict()
for sub in ls:
    res[tuple(sub[:2])] = tuple(sub[2:])
print('The mapped Dictionary:', res)

or
# Using dict comprehension
ls = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
print('The original list is:', ls)
res = {tuple(sub[:2]): tuple(sub[2:]) for sub in ls}
print('The mapped Dictionary:', res)
====================================================================

# Que.4 Convert List of Dictionaries to List of Lists
# Using loop + enumerate()
ld = [{'Nikhil': 17, 'Akash': 18, 'Akshat': 20},
             {'Nikhil': 21, 'Akash': 30, 'Akshat': 10},
             {'Nikhil': 31, 'Akash': 12, 'Akshat': 19}]
print('The original list is:', ld)
res = []
for idx, sub in enumerate(ld, start=0):
    if idx == 0:
        res.append(list(sub.keys()))
        res.append(list(sub.values()))
    else:
        res.append(list(sub.values()))
print('The converted list:', res)

or
# Using list comprehension
ld = [{'Nikhil': 17, 'Akash': 18, 'Akshat': 20},
             {'Nikhil': 21, 'Akash': 30, 'Akshat': 10},
             {'Nikhil': 31, 'Akash': 12, 'Akshat': 19}]
print('The original list is:', ld)
res = [[key for key in ld[0].keys()],
       *[list(idx.values()) for idx in ld]]
print('The converted list:', res)
==================================================================

# Que.5 Convert key-values list to flat dictionary
# Using dict() + zip()
td = {'month': [1, 2, 3], 'name': ['Jan', 'Feb', 'March']}
print('The original dictionary is:', td)
res = dict(zip(td['month'], td['name']))
print('Flattened dictionary:', res)

or
td = {'month': [1, 2, 3], 'name': ['Jan', 'Feb', 'March']}
print('The original dictionary is:', td)
x = list(td.values())
a = x[0]
b = x[1]
d = dict()
for i in range(0, len(a)):
    d[a[i]] = b[i]
print('Flattened dictionary:', d)
===================================================================

# Que.6 Convert a list of Tuples into Dictionary
# Use of setdefault()
list_1 = [('Nakul', 93), ('Shivansh', 45), ('Samved', 65),
          ('Yash', 88), ('Vidit', 70), ('Pradeep', 52)]
dict_1 = dict()
for student, score in list_1:
    dict_1.setdefault(student, []).append(score)
print(dict_1)

or
# Using dict()
tup = [('akash', 10), ('gaurav', 12), ('anand', 14),
        ('suraj', 20), ('akhil', 25), ('ashish', 30)]
di = dict(tup)
print('dictionary is:', di)
================================================================

# Que.7 Convert Nested dictionary to Mapped Tuple
# Using list comprehension
dd = {'gfg': {'x': 5, 'y': 6}, 'is': {'x': 1, 'y': 4},
             'best': {'x': 8, 'y': 3}}
print('The original dictionary is:', dd)
res = [(key, tuple(sub[key] for sub in dd.values()))
       for key in dd['gfg']]
print('The grouped dictionary:', dd)

or
# Using defaultdict() + loop
from collections import defaultdict
dd = {'gfg': {'x': 5, 'y': 6}, 'is': {'x': 1, 'y': 4},
             'best': {'x': 8, 'y': 3}}
print('The original dictionary is:', dd)
res = defaultdict(tuple)
for key, val in dd.items():
    for ele in val:
        res[ele] += (val[ele], )
print('The grouped dictionary:', res)
===============================================================

# Que.8 WAP to convert string to dictionary
str1 = 'Jan, Feb, March'
str2 = 'January | February | March'
keys = str1.split(', ')
values = str2.split('|')
dic = {}
for i in range(len(keys)):
    dic[keys[i]] = values[i]
print('convert string to dict:', dic)

or
# Using zip()
str1 = 'Jan, Feb, March'
str2 = 'January | February | March'
keys = str1.split(', ')
values = str2.split('|')
di = dict(zip(keys, values))
print('convert string to dict:', di)
==============================================================

# Que.9 Convert dictionary to K sized dictionaries
# Using loop
di = {'Gfg': 1, 'is': 2, 'best': 3, 'for': 4, 'geeks': 5, 'CS': 6}
print('The original dictionary is:', di)
K = 2
res = []
count = 0
flag = 0
indict = dict()
for key in di:
    indict[key] = di[key]
    count += 1
    if count % K == 0 and flag:
        res.append(indict)
        indict = dict()
        count = 0
    flag = 1
print('The converted list:', res)
=============================================================

# Que.10 Convert Matrix to dictionary
# Using dictionary comprehension + range()
ls = [[5, 6, 7], [8, 3, 2], [8, 2, 1]]
print('The original list is:', ls)
res = {idx + 1: ls[idx] for idx in range(len(ls))}
print('The constructed dictionary:', res)

or
# Using dictionary comprehension + enumerate()
ls = [[5, 6, 7], [8, 3, 2], [8, 2, 1]]
print('The original list is:', ls)
res = {idx: val for idx, val in enumerate(ls, start=1)}
print('The constructed dictionary:', res)
=================================================================
"""

