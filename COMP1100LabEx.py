# COMP1100 Lab 2 (6/11/17)
def total_price(number_of_packets):
    if 1 <= number_of_packets <= 5:
        return 2 * number_of_packets
    elif 6 <= number_of_packets <= 10:
        return 1.8 * number_of_packets
    elif 11 <= number_of_packets <= 30:
        return 1.5 * number_of_packets
    elif 31 <= number_of_packets <= 100:
        return 1.4 * number_of_packets
    elif 101 <= number_of_packets <= 500:
        return 1.35 * number_of_packets
    elif 501 <= number_of_packets <= 1000:
        return 1.3 * number_of_packets
    else:
        return "Too many packets."


# Week 12 Lab
def average(number_list):
    total = 0
    for i in number_list:
        total += i
    return total / len(number_list)


def rectangle_size(coord1, coord2):
    '''coord1 and coord2 are tuples with two-entries.'''
    length = abs(coord1[0] - coord2[0])
    width = abs(coord1[1] - coord2[1])
    area = length * width
    return area


def within_boundary(coord1, coord2, coord3):
    '''coord1 is the test coordinate, coord2 and coord3 represent diagonally
    opposite corners of the rectangle. This function tests whether coord1 is
    within or on the boundaries of the given rectangle.'''
    test1 = coord2[0] <= coord1[0] <= coord3[0] or \
        coord3[0] <= coord1[0] <= coord2[0]
    test2 = coord2[1] <= coord1[1] <= coord3[1] or \
        coord3[1] <= coord1[1] <= coord2[1]
    return test1 and test2


def most_expensive(item_dict):
    '''Given a dictionary of items and their prices, return the most expensive
    item in the dictionary.'''
    prices = item_dict.values()
    pricy = max(prices)
    for i in item_dict.keys():
        if item_dict[i] == pricy:
            return i
        else:
            continue


def intercalate(list_arg, matrix):
    '''Inserts a given list between the rows of a given matrix and
    concatenates the rows of the resulting matrix.'''
    i = 0
    while i < len(matrix) - 1:
        matrix[i] += list_arg
        i += 1
    result = matrix[0]
    for i in matrix[1:]:
        result += i
    return result


def is_substring(string, longer_string):
    i = 0
    while i <= len(longer_string) - len(string):
        if longer_string[i:len(string)+i] == string:
            return True
        else:
            i += 1
    return False


def nth_prime(n):
    return primes(n)[-1]


def primes(n):
    '''Returns a list of the first n primes.'''
    result = []
    i = 2
    while len(result) < n:
        if is_prime(i):
            result.append(i)
            i += 1
        else:
            i += 1
    return result


def is_prime(n):
    if n < 2:
        return False
    else:
        factors = list(range(2, n))
        for i in factors:
            if n % i == 0:
                return False
            else:
                continue
        return True
