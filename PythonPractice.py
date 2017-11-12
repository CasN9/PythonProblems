import bs4
import requests as req
import json
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

birthday_dict = {'Caspian Nicholls': '31/5/1998',
                 'Fergus Orr': '22/10/1998',
                 'Georgia Ketels': '12/1/1998',
                 'Cin Cheng': '17/1/1998',
                 'Renee Aun': '24/2/1998',
                 'Eliot Vogel': '7/4/1998',
                 'Tom Crawford': '14/4/1998',
                 'Amelia Powell': '28/4/1998',
                 'Alex Williams': '15/5/1998',
                 'Bec Finocchiaro': '30/5/1998',
                 'Nina Fujii': '4/6/1998',
                 'Emily Townsend': '18/6/1998',
                 'Cameron Pollaers': '25/6/1998',
                 'Matt Cooke': '3/7/1998',
                 'Aaqil Zaheed': '5/7/1998',
                 'Oliver Holt': '7/7/1998',
                 'Elly Hartnett': '9/7/1998',
                 'Jess Blakeney': '27/7/1998',
                 'Amy Kayman': '31/7/1998',
                 'Kimmy Fernandes-Kemp': '21/12/1997',
                 'Tim Bliss': '25/12/1997'}
names = list(birthday_dict.keys())
print("Welcome to the birthday dictionary. We know the birthdays of: ")
for i in names:
    print(i)
print("Who's birthday would you like to know?")
user = input()
print(user + "'s birthday is on %s." % birthday_dict[user])
file_obj = open("birthdays.txt", 'w+')
for i in names:
    file_obj.write(i + ", " + birthday_dict[i] + "\n")
with open("birthdays.json", "w") as f:
    json.dump(birthday_dict, f)
month_total_dict = {}
with open("birthdays.json", "r") as g:
    for line in g:
        print(line)
        a = line
