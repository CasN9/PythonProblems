# Author: Caspian Nicholls, u1027945
# Institution: Australian National University
# Course: COMP1730
# Project assignment

### THINGS TO DO
# See https://wattlecourses.anu.edu.au/mod/forum/discuss.php?d=428886
# https://wattlecourses.anu.edu.au/mod/forum/discuss.php?d=433141
# important consideration for data analysis
# Gaps

import csv

print("Once in a hundred years assignment - u1027945")
print("Would you like to use data that has not been quality checked? Enter 'Y' or 'N':")
yn = input()
print("Choose a method: A or B:")
method = input()
print("Please enter a file path:")
file_path = input()
print("Enter 'day', 'month', 'year' or 'specific month' to choose a " +
      "time-series aggegration method:")
time = input()
print("Would you like to consider exceptionally high or exceptionally " +
      " low values?")
print("Enter 'HIGH' or 'LOW' to continue:")
choice = input()
print("Choose a frequency of event you would like to use. Your " +
      "choice, F, will represent once in every F units of time that you " +
      "chose earlier. Please enter an integer value.")
frequency = input()

open_file = open(str(file_path), 'r')
open_file.readline()
reader = csv.reader(open_file)
rainfall = []
year = []
month = []
day = []
period = []
for row in reader:
    if str(yn) == 'Y':
        if row[5] == '':
            pass
        elif row[6] == '':
            year.append(int(row[2]))
            month.append(int(row[3]))
            day.append(int(row[4]))
            rainfall.append(float(row[5]))
            period.append(1)
        else:
            year.append(int(row[2]))
            month.append(int(row[3]))
            day.append(int(row[4]))
            rainfall.append(float(row[5]))
            period.append(int(row[6]))
    else:
        if row[7] == 'N' or row[5] == '':  # Checking for quality of the data.
            pass
        elif row[6] == '':
            year.append(int(row[2]))
            month.append(int(row[3]))
            day.append(int(row[4]))
            rainfall.append(float(row[5]))
            period.append(1)
        else:
            year.append(int(row[2]))
            month.append(int(row[3]))
            day.append(int(row[4]))
            rainfall.append(float(row[5]))
            period.append(int(row[6]))


def overlap():
    '''Checks if there are any months where the rainfall has been recorded
    over two adjacent months/years.'''
    i = 0
    while i < len(day):
        if day[i] - period[i] < 0:
            print(str(year[i]) + str(month[i]) + str(day[i]))
            i += 1
        else:
            i += 1


def day_aggregate():
    '''Computes the time-series of daily values.'''
    return rainfall

months = list(range(1, 13))
years = list(range(min(year), max(year)+1))
dates = [(i, j) for j in years for i in months]


def month_aggregate():  # May want to neaten this up, time permitting.
    '''Computes the time-series of monthly totals.'''
    i = 0
    data = []
    month_param = month[0]
    year_param = year[0]
    while i < len(year):
            while i < len(year) and year[i] == year_param:
                aggregate = []
                while i < len(year) and month[i] == month_param:
                    aggregate.append(float(rainfall[i]))
                    i += 1
                data.append(sum(aggregate))
                month_param += 1
            year_param += 1
            month_param = 1
    i = 0
    year_param = max(year)
    month_param = 1
    while i < len(year):
        if year[i] == year_param:
            while i < len(year) and month_param < 13:
                aggregate = []
                while i < len(year) and month[i] == month_param:
                    aggregate.append(float(rainfall[i]))
                    i += 1
                data.append(sum(aggregate))
                month_param += 1
        else:
            i += 1
    return data


def year_aggregate():
    '''Computes the time-series of yearly values.'''
    i = 0
    year_param = year[0]
    data = []
    while year_param < max(year):
        aggregate = []
        while year[i] == year_param:
            aggregate.append(float(rainfall[i]))
            i += 1
        data.append(sum(aggregate))
        year_param += 1
    i = 0
    year_param = max(year)
    while i < len(year):
        aggregate = []
        while i < len(year) and year[i] == year_param:
            aggregate.append(float(rainfall[i]))
            i += 1
        i += 1
    data.append(sum(aggregate))
    return data


def spec_month_agg(spec_month):
    '''Series of totals for a specific month.'''
    i = 0
    data = []
    year_param = year[0]
    while year_param < max(year):
        aggregate = []
        while year[i] == year_param:
            if month[i] == spec_month:
                aggregate.append(float(rainfall[i]))
                i += 1
            else:
                i += 1
        data.append(sum(aggregate))
        year_param += 1
    i = 0
    year_param = max(year)
    while i < len(year):
        aggregate = []
        while i < len(year) and year[i] == year_param and month[i] == spec_month:
            aggregate.append(float(rainfall[i]))
            i += 1
        i += 1
    data.append(sum(aggregate))
    return data

if 'Queanbeyan' in file_path:
    print("Location: Queanbeyan.")
elif 'Canberra' in file_path:
    print("Location: Canberra.")
elif 'Sydney' in file_path:
    print("Location: Sydney.")
else:
    print("")

# Method A - WIP
if method == 'A':
    print("Chosen method: A.")
    if choice == 'HIGH':
        print("Considering extraordinarily high values.")
        if time == 'day':
            timeseries = rainfall
            serial = day_aggregate()[0:len(day_aggregate())]
            serial.sort()
            i = -1
            while i > -len(timeseries):
                threshold = round(serial[-i], 2)
                exceeds = [j for j in timeseries if j >= threshold]
                indices = [timeseries.index(j) for j in exceeds]
                indices.sort()
                diff = [abs(k - j) for k in indices for j in indices if k != j]
                if diff == []:
                    i -= 1
                elif min(diff) > int(frequency):
                    print(threshold)
                    i = -(10 ** 20)
                else:
                    i -= 1
            i = 0
            print("A once in " + str(frequency) + " " + str(time) + "s rainfall is " + str(threshold) + " mm.")
            print("This threshold was reached or exceeded on the following dates: ")
            while i < len(rainfall):
                if round(rainfall[i], 2) >= threshold:
                    print(day[i], month[i], year[i])
                    i += 1
                else:
                    i += 1
        elif time == 'month':
            timeseries = month_aggregate()
            serial = month_aggregate()[0:len(month_aggregate())]
            serial.sort()
            i = -1
            while i > -len(timeseries):
                threshold = round(serial[-i], 2)
                exceeds = [j for j in timeseries if j >= threshold]
                indices = [timeseries.index(j) for j in exceeds]
                indices.sort()
                diff = [abs(k - j) for k in indices for j in indices if k != j]
                if diff == []:
                    i -= 1
                elif min(diff) > int(frequency):
                    print(threshold)
                    i = -(10 ** 20)
                else:
                    i -= 1
            i = 0
            datum = month_aggregate()
            print("A once in " + str(frequency) + " " + str(time) + "s rainfall is " + str(threshold) + " mm.")
            print("This threshold was reached or exceeded in the following months: ")
            while i < len(datum):
                if round(datum[i], 2) >= threshold:
                    print(dates[i])
                    i += 1
                else:
                    i += 1
        elif time == 'year':
            timeseries = year_aggregate()
            serial = year_aggregate()[0:len(year_aggregate())]
            serial.sort()
            i = -1
            while i > -len(timeseries):
                threshold = round(serial[-i], 2)
                exceeds = [j for j in timeseries if j >= threshold]
                indices = [timeseries.index(j) for j in exceeds]
                indices.sort()
                diff = [abs(k - j) for k in indices for j in indices if k != j]
                if diff == []:
                    i -= 1
                elif min(diff) > int(frequency):
                    print(threshold)
                    i = -(10 ** 20)
                else:
                    i -= 1
            i = 0
            datum = year_aggregate()
            print("A once in " + str(frequency) + " " + str(time) + "s rainfall is " + str(threshold) + " mm.")
            print("This threshold was reached or exceeded in the following years: ")
            while i < len(datum):
                if round(datum[i], 2) >= threshold:
                    print(years[i])
                    i += 1
                else:
                    i += 1
        elif time == 'specific month':
            print("Choose a month, between 1 and 12, where 1 represents " +
                  "January and 12 represents December:")
            chosen_month = input()
            timeseries = spec_month_agg(int(chosen_month))
            serial = spec_month_agg(int(chosen_month))[0:len(spec_month_agg(int(chosen_month)))]
            serial.sort()
            i = -1
            while i > -len(timeseries):
                threshold = round(serial[-i], 2)
                exceeds = [j for j in timeseries if j >= threshold]
                indices = [timeseries.index(j) for j in exceeds]
                indices.sort()
                diff = [abs(k - j) for k in indices for j in indices if k != j]
                if diff == []:
                    i -= 1
                elif min(diff) > int(frequency):
                    print(threshold)
                    i = -(10 ** 20)
                else:
                    i -= 1
            i = 0
            datum = spec_month_agg(int(chosen_month))
            print("A once in " + str(frequency) + " " + str(time) + "s rainfall is " + str(threshold) + " mm.")
            print("This threshold was reached or exceeded in the following years: ")
            while i < len(datum):
                if round(datum[i], 2) >= threshold:
                    print(years[i])
                    i += 1
                else:
                    i += 1
        else:
            print("Error 1: invalid time choice")
    elif choice == 'LOW':
        print("Considering extraordinarily low values.")
        if time == 'day':
            serial = day_aggregate()[0:len(day_aggregate())]
            serial.sort()
            i = 0
            while i < len(rainfall):
                threshold = round(serial[i], 2)
                exceeds = [j for j in rainfall if j <= threshold]
                indices = [rainfall.index(j) for j in exceeds]
                indices.sort()
                diff = [abs(k - j) for k in indices for j in indices if k != j]
                if diff == []:
                    i += 1
                elif min(diff) > int(frequency):
                    print(threshold)
                    i = 10 ** 20
                else:
                    i += 1
            if threshold <= min(rainfall):
                print("No threshold value greater than the minimum entry in the time-series was found.")
            else:
                i = 0
                print("A once in " + str(frequency) + " " + str(time) + "s rainfall is " + str(threshold) + " mm.")
                print("This threshold was reached or exceeded on the following dates: ")
                while i < len(rainfall):
                    if round(rainfall[i], 2) <= threshold:
                        print(day[i], month[i], year[i])
                        i += 1
                    else:
                        i += 1
        elif time == 'month':
            timeseries = month_aggregate()
            serial = month_aggregate()[0:len(month_aggregate())]
            serial.sort()
            i = 1
            while i < len(timeseries):
                threshold = round(serial[i], 2)
                exceeds = [j for j in timeseries if j <= threshold]
                indices = [timeseries.index(j) for j in exceeds]
                indices.sort()
                diff = [abs(k - j) for k in indices for j in indices if k != j]
                if diff == []:
                    i += 1
                elif min(diff) > int(frequency):
                    print(threshold)
                    i = 10 ** 20
                else:
                    i += 1
            if threshold >= min(timeseries):
                print("No threshold value greater than the minimum entry in the time-series was found.")
            else:
                i = 0
                datum = month_aggregate()
                print("A once in " + str(frequency) + " " + str(time) + "s rainfall is " + str(threshold) + " mm.")
                print("This threshold was reached or exceeded in the following months: ")
                while i < len(datum):
                    if round(datum[i], 2) <= threshold:
                        print(dates[i])
                        i += 1
                    else:
                        i += 1
        elif time == 'year':
            timeseries = year_aggregate()
            serial = year_aggregate()[0:len(year_aggregate())]
            serial.sort()
            i = 0
            while i < len(timeseries):
                threshold = round(serial[i], 2)
                exceeds = [j for j in timeseries if j <= threshold]
                indices = [timeseries.index(j) for j in exceeds]
                indices.sort()
                diff = [abs(k - j) for k in indices for j in indices if k != j]
                if diff == []:
                    i += 1
                elif min(diff) > int(frequency):
                    print(threshold)
                    i = 10 ** 20
                else:
                    i += 1
            if threshold <= min(timeseries):
                print("No threshold value greater than the minimum entry in the time-series was found.")
            else:
                i = 0
                datum = year_aggregate()
                print("A once in " + str(frequency) + " " + str(time) + "s rainfall is " + str(threshold) + " mm.")
                print("This threshold was reached or exceeded in the following years: ")
                while i < len(datum):
                    if round(datum[i], 2) <= threshold:
                        print(years[i])
                        i += 1
                    else:
                        i += 1
        elif time == 'specific month':
            print("Choose a month, between 1 and 12, where 1 represents " +
                  "January and 12 represents December:")
            chosen_month = input()
            timeseries = spec_month_agg(int(chosen_month))
            serial = spec_month_agg(int(chosen_month))[0:len(spec_month_agg(int(chosen_month)))]
            serial.sort()
            i = 0
            while i < len(timeseries):
                threshold = round(serial[i], 2)
                exceeds = [j for j in timeseries if j <= threshold]
                indices = [timeseries.index(j) for j in exceeds]
                indices.sort()
                diff = [abs(k - j) for k in indices for j in indices if k != j]
                if diff == []:
                    i += 1
                elif min(diff) > int(frequency):
                    print(threshold)
                    i = 10 ** 20
                else:
                    i += 1
            if threshold <= min(timeseries):
                print("No threshold value greater than the minimum entry in the time-series was found.")
            else:       
                i = 0
                datum = spec_month_agg(int(chosen_month))
                print("A once in " + str(frequency) + " " + str(time) + "s rainfall is " + str(threshold) + " mm.")
                print("This threshold was reached or exceeded in the following months: ")
                while i < len(datum):
                    if round(datum[i], 2) <= threshold:
                        print(years[i])
                        i += 1
                    else:
                        i += 1
        else:
            print("Error 2 - invalid time choice")
    else:
        print("Error 3 - invalid value type choice")

# Note: using values that are G.T or equal to threshold.
# Method B
elif method == 'B':
    print("Chosen method: B.")
    if choice == 'HIGH':
        print("Considering extraordinarily high values.")
        if time == 'day':
            datum = rainfall[0:len(rainfall)]
            datum.sort()
            index = len(datum) - (len(datum) // int(frequency))
            threshold = round(datum[index], 2)
            print("A once in " + str(frequency) + " " + str(time) + "s rainfall is " + str(threshold) + " mm.")
            i = 0
            print("This threshold was reached or exceeded on the following dates: ")
            while i < len(rainfall):
                if round(rainfall[i], 2) >= threshold:
                    print(day[i], month[i], year[i])
                    i += 1
                else:
                    i += 1
        elif time == 'month':
            datum = month_aggregate()[0:len(month_aggregate())]
            datum.sort()
            index = len(datum) - (len(datum) // int(frequency))
            threshold = round(datum[index], 2)
            print("A once in " + str(frequency) + " " + str(time) + "s rainfall is " + str(threshold) + " mm.")
            i = 0
            datum = month_aggregate()
            print("This threshold was reached or exceeded in the following months: ")
            while i < len(datum):
                if round(datum[i], 2) >= threshold:
                    print(dates[i])
                    i += 1
                else:
                    i += 1
        elif time == 'year':
            datum = year_aggregate()[0:len(year_aggregate())]
            datum.sort()
            index = len(datum) - (len(datum) // int(frequency))
            threshold = round(datum[index], 2)
            print("A once in " + str(frequency) + " " + str(time) + "s rainfall is " + str(threshold) + " mm.")
            i = 0
            datum = year_aggregate()
            print("This threshold was reached or exceeded in the following years: ")
            while i < len(datum):
                if round(datum[i], 2) >= threshold:
                    print(years[i])
                    i += 1
                else:
                    i += 1
        elif time == 'specific month':
            print("Choose a month, between 1 and 12, where 1 represents " +
                  "January and 12 represents December:")
            chosen_month = input()
            datum = spec_month_agg(int(chosen_month))[0:len(spec_month_agg(int(chosen_month)))]
            datum.sort()
            index = len(datum) - (len(datum) // int(frequency))
            threshold = round(datum[index], 2)
            print("A once in " + str(frequency) + " years rainfall for the " + str(chosen_month) + "th month is " + str(threshold) + " mm.")
            i = 0
            datum = spec_month_agg(int(chosen_month))
            print("This threshold was reached or exceeded in the following years: ")
            while i < len(datum):
                if round(datum[i], 2) >= threshold:
                    print(years[i])
                    i += 1
                else:
                    i += 1
        else:
            print("Error 4 - invalid time choice")
    elif choice == 'LOW':
        print("Considering extraordinarily low values.")
        if time == 'day':
            index = len(rainfall) // int(frequency)
            datum = rainfall[0:len(rainfall)]
            datum.sort()
            threshold = round(datum[index], 2)
            if threshold <= min(timeseries):
                print("No threshold value greater than the minimum entry in the time-series was found.")
            else: 
                print("A once in " + str(frequency) + " " + str(time) + "s rainfall is " + str(threshold) + " mm.")
                i = 0
                print("This threshold was reached or exceeded on the following dates: ")
                while i < len(rainfall):
                    if round(rainfall[i], 2) <= threshold:
                        print(day[i], month[i], year[i])
                        i += 1
                    else:
                        i += 1
        elif time == 'month':
            index = len(month_aggregate()) // int(frequency)
            datum = month_aggregate()[0:len(month_aggregate())]
            datum.sort()
            threshold = round(datum[index], 2)
            if threshold <= min(timeseries):
                print("No threshold value greater than the minimum entry in the time-series was found.")
            else: 
                print("A once in " + str(frequency) + " " + str(time) + "s rainfall is " + str(threshold) + " mm.")
                i = 0
                datum = month_aggregate()
                print("This threshold was reached or exceeded in the following months: ")
                while i < len(datum):
                    if round(datum[i], 2) <= threshold:
                        print(dates[i])
                        i += 1
                    else:
                        i += 1
        elif time == 'year':
            index = len(year_aggregate()) // int(frequency)
            datum = year_aggregate()[0:len(year_aggregate())]
            datum.sort()
            threshold = round(datum[index], 2)
            if threshold <= min(timeseries):
                print("No threshold value greater than the minimum entry in the time-series was found.")
            else: 
                print("A once in " + str(frequency) + " " + str(time) + "s rainfall is " + str(threshold) + " mm.")
                i = 0
                datum = year_aggregate()
                print("This threshold was reached or exceeded in the following years: ")
                while i < len(datum):
                    if round(datum[i], 2) <= threshold:
                        print(years[i])
                        i += 1
                    else:
                        i += 1
        elif time == 'specific month':
            print("Choose a month, between 1 and 12, where 1 represents " +
                  "January and 12 represents December:")
            chosen_month = input()
            datum = spec_month_agg(int(chosen_month))[0:len(spec_month_agg(int(chosen_month)))]
            datum.sort()
            index = len(spec_month_agg(chosen_month)) // int(frequency)
            threshold = round(datum[index], 2)
            if threshold <= min(timeseries):
                print("No threshold value greater than the minimum entry in the time-series was found.")
            else: 
                print("A once in " + str(frequency) + " years rainfall for the " + str(chosen_month) + "th month is " + str(threshold) + " mm.")
                i = 0
                datum = spec_month_agg(int(chosen_month))
                print("This threshold was reached or exceeded in the following years: ")
                while i < len(datum):
                    if round(datum[i], 2) <= threshold:
                        print(years[i])
                        i += 1
                    else:
                        i += 1
        else:
            print("Error 5 - invalid time choice")
    else:
        print("Error 6 - invalid value type choice")
else:
    print("Error 7: Invalid method choice")

open_file.close()
