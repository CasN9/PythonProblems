import timeit
#for a in range(10,15):
#    b = 2*a + 1
#    print(b)
#    if b > 42:
#        continue
#in_file = open("lab7.txt")
#for line in in_file:
#    print("line: ", line)
#in_file.close()
#def x(y):
#    a,b = 2,1
#    while b-1 < len(y):
#        a += y[b-1]
#        b = b + a//a
#    a -= 2
#    return a


#def x(y):
##    a = 0
##    for i in y:
##        a += i
##    return a
#    return sum(y)
#
#z = [42, 3, 6, 0, -2, 1]
#print(x(z))

#my_dict = {1:'a', 2:2, 3:'c', 4:'d', 5:27}
#for i in my_dict.keys():
#    if type(my_dict[i]) == str:
#        my_dict[i] = my_dict[i].upper()
#    else:
#        my_dict[i] *= 2
#print(my_dict)
#def sum_list(a_list):
#    n = 0
#    while len(a_list) > 0:
#        n += a_list.pop(0)
#    return n
#
#my_list = [6,3,6,5,7,9]
#print("Sum is ", sum_list(my_list))
#print("Average is ", sum_list(my_list) / len(my_list))
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def median(seq):
    assert len(seq) % 2 == 1
    for elem in seq:
        n = 0
        for item in seq:
            if item < elem:
                n += 1
        if n == len(seq) // 2:
            return elem

banana = list(range(1, 2002))
bananas = list(range(1, 4002))
wrapped = wrapper(median, banana)
print(timeit.timeit(wrapped,number=1))

wrapped = wrapper(median, bananas)
print(timeit.timeit(wrapped,number=1))
