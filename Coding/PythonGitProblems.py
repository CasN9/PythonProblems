import math
import numpy as np
# Exercises from:
# https://github.com/zhiwehu/Python-programming-exercises/blob/master/100
# %2B%20Python%20challenging%20programming%20exercises.txt
numbers = list(range(2000, 3201))
list_result = []
for i in numbers:
    if i % 7 == 0 and i % 5 != 0:
        list_result.append(i)
string = ', '.join(str(i) for i in list_result)
# print(string)

# D_values = input()
# C = 50
# H = 30
# param = D_values.split(',')
# answer = []
# for i in param:
#     result = math.sqrt((2 * C * int(i)) / H)
#     answer.append(result)
# soln = ', '.join(str(int(i)) for i in answer)
# print(soln)


def array_func(x, y):
    '''Returns an array with dimensions x by y, where the (i,j)th element
    is equal to i * j.'''
    i = 0
    total = []
    while i < x:
        row = []
        j = 0
        while j < y:
            row.append(i * j)
            j += 1
        total.append(row[:])
        i += 1
    return np.array(total)


# word_list = input()  # a comma-separated list of words input by the user
# words = word_list.split(',')
# words.sort()
# strung = ','.join(i for i in words)
# print(strung)

# Password checking exercise
passwords = input()  # a list of comma-separated passwords
valid_pw = []
pws = passwords.split(',')
lower_letters = 'abcdefghijklmnopqrstuvwxyz'
upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '123456789'
punc = '$#@'


def intersect(a, b):
    result = [i for i in a if i in b]
    return result


#for p in pws:
#    if len(p) < 6:
#        continue
#    elif len(p) > 12:
#        continue
#    elif intersect(p, lower_letters) == []:
#        continue
#    elif intersect(p, upper_letters) == []:
#        continue
#    elif intersect(p, numbers) == []:
#        continue
#    elif intersect(p, punc) == []:
#        continue
#    else:
#        valid_pw.append(p)
#string = ','.join(i for i in valid_pw)
#print(string)


# Sorting scores
data = []
print("Enter a name, age and score: ")
point = input()
data.append(tuple(point.split(',')))
print("Would you like to enter another name?")
user = input()
while user == "Yes":
    point = input()
    value = tuple(point.split(','))
    i = 0
    while i < len(data):
        j = 0
        while j < len(data[0]):
            if value[j] < data[i][j]:
                data.insert(i, value)
                i = math.inf
                break
            elif value[j] == data[i][j]:
                j += 1
            else:
                break
        i += 1
    if i == len(data):
        data.append(value)
    print("Would you like to enter another name?")
    user = input()
