import bs4
import requests as req
from bokeh.plotting import figure, show, output_file
# req documentation: http://docs.python-requests.org/en/latest/user/quickstart/


def intersection(list1, list2):
    result = [i for i in list1 if i in list2]
    return set(result)


def first_last(number_list):
    return number_list[0:len(number_list):len(number_list)-1]


def fibonacci(n):
    fibs = [0, 1]
    i = n - 2
    while i > 0:
        fibs.append(fibs[-1] + fibs[-2])
        i -= 1
    return fibs


#print("How many Fibonacci numbers would you like?")
#number = int(input())
#print("The first %s Fibonacci numbers are " % str(number), end="")
#for i in fibonacci(number)[0:-1]:
#    print(i, end=", ")
#print("and %s." % fibonacci(number)[-1])

def no_dupes(list1):
    result = []
    for i in list1:
        if i in result:
            pass
        else:
            result.append(i)
    return result


def no_whitespace(string_list):
    for i in string_list:
        a = i.split()
        b = " ".join(j for j in a)
        string_list[string_list.index(i)] = b
    return string_list


def no_dupes_set(list1):
    return list(set(list1))


# Reading a HTML file.
#r = req.get("https://www.nytimes.com/")
#r_html = r.text
#soup = bs4.BeautifulSoup(r_html, "lxml")
#for story_heading in soup.find_all(class_="story-heading"):
#    if story_heading.a:
#        print(story_heading.a.text.replace("\n", " ").strip())
#    else:
#        print(story_heading.contents[0].strip())

file_obj = open("birthdays.txt", 'r')
names = []
month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
dates = []
for line in file_obj:
    names.append(line[0:-11].strip(' ').strip(','))
    dates.append(line[-11:-1].strip(' ').strip(','))
months = {}
for i in dates:
    j = 1
    while j < 13:
        if int(i[-7:-5].strip('/')) == j:
            if month_list[j-1] in months.keys():
                months[month_list[j-1]] += 1
                j = 14
            else:
                months[month_list[j-1]] = 1
                j = 14
        else:
            j += 1

output_file("plot.html")
x_list = []
for i in months.keys():
    j = 0
    while j < 12:
        if month_list[j] == i:
            x_list.append(j+1)
            j = 13
        else:
            j += 1
y_list = list(months.values())
p = figure(title="Number of birthdays of my friends by month")
p.vbar(x=x_list, top=y_list, width=0.5)
p.xaxis.axis_label = "Birthday month"
p.yaxis.axis_label = "Number of birthdays"
show(p)
