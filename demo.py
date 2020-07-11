name = 'My Name is Mike'

print(name[0])
print(name[-4])
print(name[11:14])
print(name[11:15])
print(name[5:])
print(name[:5])

word = 'friends'
find_the_evil_in_your_friends = word[0] + word[2:4] + word[-3:-1]
print(find_the_evil_in_your_friends)


url = 'http://ww1.site.cn/14d2e8ejw1exjogbxdxhj20ci0kuwex.jpg'
file_name = url[-10:]
# try replacing the -10: with :-10 and see what happened
print(file_name)

phone_number = '139-2485-9401'
hiding_number = phone_number.replace(phone_number[:9],'*' * 9)
# replace(what you wanna to be replaced, contents)
print(hiding_number)

search = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0006'

print(search + ' is at ' + str(num_a.find(search) + 1) + ' to ' + str(num_a.find(search) + len(search)) + ' of num_a')
# "find" will look for the array of the word where it locate
# but be careful that such find will only locate the first letter of your string
print(search + ' is at ' + str(num_b.find(search) + 1) + ' to ' + str(num_b.find(search) + len(search)) + ' of num_b')

print('{} a word she can get what she {} for.'.format('with', 'came'))
print('{preposition} a word she can get what she {verb} for.'.format(preposition = 'with', verb  ='came'))
print('{0} a word she can get what she {1} for.'.format('with', 'came'))

city = input("write down the name of city:") # you can try typing Foshan or others
url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)

def cel(fa):
    celsius = (fa - 32) * 5 / 9
    return str(celsius) + 'C'

# after defining a function, u need to call to use it
# just like the len() function

lyric_length = len('I cry out for magic!')
# len() function will include spaces and symbols
print(lyric_length)

F2C = cel(103)
print(F2C)

# now try replacing the last funciton with a new way

def cel(fa):
    celsius = (fa - 32) * 5 / 9
    print(str(celsius) + 'C')

F2C = cel(103)
print(F2C)

# there will be a "none" at the end of execution
# that is bc "print" is only a function but "return" is a key
# "return" is optional in python, without it, the def function still works
# but it would just return a "none" value at the end

def weight_converter(g):
    kg = g / 1000
    return str(kg) + 'kg'

weight_test_1 = weight_converter(1000)
print(weight_test_1)

# a more convenient way
def g2kg(g):
    return str(g/1000) + 'kg'

print(g2kg(2000))

from math import sqrt
# although sqrt is a built-in function in python
# it is actually in the 'math' package
# we need to import such function for further utilization

def pythagorean(side_1 , side_2):
    hypotenuse = sqrt(side_1**2 + side_2**2)
    # 3 ways to represent square of a given number
    # by multiplying numbers two times: side_1 * side_1
    # by using exponent operator: side_1 ** 2
    # by using math.pow() method
    return "The right triangle third side's length (hypotenuse) is " + str(hypotenuse)

pytha_test_1 = pythagorean(3,4)
print(pytha_test_1)

# another way to present such result
def pythagorean_theorem(a,b):
    return 'The right triangle third side\'s length is {}'.format((a**2 + b**2)**(1/2))

print(pythagorean_theorem(3,4))

def trapezoid_area(base_up, base_down, height):
    return 1/2 * (base_up + base_down) * height

trapezoid_area(1,2,3)   # this is called positional argument
trapezoid_area(base_up=1, base_down=2, height=3) # keyword argument
# just like going to a canteen, u get a code by your name (keyword argument)
# meals however, is delivered via your table number (positional argument)
# u can test the following codes to see what happened
trapezoid_area(height=3, base_down=2, base_up=1)   # RIGHT!
trapezoid_area(height=3, base_down=2, 1)
# WRONG! it reverses the inputs, but the last argument shall be height
# and there has been an input for height already, counteracting itself
trapezoid_area(base_up=1, base_down=2, 3)          # RIGHT!
trapezoid_area(1, 2, height=3)                     # RIGHT!

print('  *',' * *','* * *','  | ')
# replacing each print argument with a new paragraph
print('  *',' * *','* * *','  | ', sep = '\n')
# and then u have a christmas tree~

# when we are defining function, we can set up default input for argument
def trapezoid_area(base_up, base_down, height = 3):
    return 1/2 * (base_up + base_down) * height
# we can now only insert 2 arguments
trapezoid_area(1, 2)
# we can call up a new value for height if we want to
trapezoid_area(1, 2, height = 15)

# we will see lots of default value in the future in a function
requests.get(url, headers = header)
# not filling the header when requesting the header of the website
img.save(img_new, img_format, quality = 100)
# adding a watermark on pic while defaulting the quality as 100

# lets create a txt file on destop named text
# try to open it with the 'open' function
open('C://Users/aleny/Desktop/text.txt')
# looks like nothing is happening right?
# how about trying the 'write' function?
file = open('C://Users/aleny/Desktop/text.txt', 'w')
file.write('Hello World')
# check the file now, u should be able to see Hello World written

# now lets write a function that creates a file and inserts content into the file on the desktop
# if there is no such file on the desktop then we just create a new one and continue writing
def text_creator(name, msg):
    desktop_path = 'C://Users/aleny/Desktop/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    # if no such file, create one
    # if such file exits, override the file with new content
    file.write(msg)
    file.close()
    print('Done')
text_creator('hello', 'hellow world') # modifying the argument

# now write a function that filters sensitive words
# assuming the censored word is 'lame' and replacement is 'awesome'
def text_filter(word, censored_word = 'lame', changed_word = 'Awesome'):
    return word.replace(censored_word, changed_word)
text_filter('Python is lame!') # modifying the argument

# combine two function together
def text_creator_filter(name, msg, censored_word = 'lame', changed_word = 'Awesome'):
    desktop_path = 'C://Users/aleny/Desktop/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg.replace(censored_word, changed_word))
    file.close()
    print('Done!')
text_creator_filter('Surprise', 'lame! lame! lame!')

# or there is another way since we've created two functions before
def censored_text_create(name, msg):
    clean_msg = text_filter(msg)
    text_creator(name, clean_msg)
censored_text_create('Try', 'lame! lame! lame!')

# now its the time for membership & identify operators
# lets first create a list
album = []
# we need to put sth into the list
album = ['Black Star', 'David Bowie', 25, True]
# if we want to add new elements into the list, we need 'append'
album.append('New Song')
# index from the list
print(album[0], album[-1])
# check the 'in' membership operator (in or not in)
'Black Star' in album

# 'is' or 'is not' are the identify operators
# every object in python has three elements - identity, type and value
the_Eddie = 'Eddie'
name = 'Eddie'
the_Eddie == name
the_Eddie is name

# every object in python can be determined its boolean value
# except for 0, NONE and empty list or set that will return false
# every other value will be true
# use bool() to determine
bool(0)
bool([])
bool('')
bool(False)
bool(None)

# now its the funny part, lets talk about if..else statment!
def account_login():
    password = input('Password:')
    if password == '12345':
        print('Login success!')
    else:
        print('Wrong password or invalid input!')

        account_login()
        # if password is wrong, rerun the function again to ask for password again
account_login()

# multiple conditions: use 'elif'
password_list = ['*#*#', '12345']
def account_login():
    password = input('Password:')
    password_correct = password == password_list[-1]
    password_reset = password == password_list[0]
    if password_correct:
        print('Login success!')
    elif password_reset:
        new_password = input('Enter a new password:')
        password_list.append(new_password)
        print('Your password has changed usccessfully!')
        account_login()
    else:
        print('Wrong password or invalid input!')
        account_login()
account_login()

# for loop time
# for item in iterable: do something
for every_letter in 'Hellw world':
    print(every_letter)

for num in range(1, 11): # not include 11, actual range is 1 ~ 10
    print(str(num) + ' + 1 =', num + 1)

songslist = ['Holy Diver', 'Thunderstruck', 'Rebel Rebel']
for song in songslist:
    if song == 'Holy Diver':
        print(song, ' - Dio')
    elif song == 'Thunderstruck':
        print(song, ' - AC/DC')
    elif song == 'Rebel Rebel':
        print(song, ' - David Bowie')

# another loop is called nested loop
# multiplication table
for i in range(1, 10):
    for j in range(1, 10):
        print('{} X {} = {}'.format(i, j, i*j))

# while loop example
# caution!!!!!!
# remember to stop running the program
# otherwise it will keep printing until your cpu is overheat
# we call such loop as infinite loop
while 1 < 3:
    print('1 is smaller than 3')
# control the while loop to stop at certain circumstance
count = 0
while True:
    print('Repeat this line !')
    count = count + 1
    if count == 5:
        break

# or change the condition for the while loop so it could stop automatically
password_list = ['*#*#', '12345']

def account_login():
    trials = 3
    while trials > 0:
        password = input('Password:')
        password_correct = password == password_list[-1]
        password_reset = password == password_list[0]

        if password_correct:
            print('Login success!')
        elif password_reset:
            new_password = input('Enter a new password:')
            password_list.append(new_password)
            print('Your password has changed usccessfully!')
            account_login()
        else:
            print('Wrong password or invalid input!')
            trials = trials - 1
            print(trials, 'time left')
    else:
        print('Your account has been suspended!')

account_login()

# insertion in list
fruit = ['pineapple', 'pear']
fruit.insert(1, 'grape')
print(fruit)

fruit[0:0] = ['Orange']
print(fruit)

# removal in list
fruit = ['pinapple','pear','grape']
fruit.remove('grape')
print(fruit)

# replacement in list
fruit[0] = 'Grapefruit'

# use del to declare a deletion
del fruit[0:2]
print(fruit)

# we cannot print a list to look up the specific position of the value
# it would run an error if you do so because list only accept indexing via location
# then we will need to use dictionary to index

# there must be a match between a 'key' and a 'value' in a dictionary
NASDAQ_code = {
    'BIDU':'Baidu',
    'SINA':'Sina',
    'YOKU':'Youku'
}
# if you gonna write ('BIDU':), there will be a syntax error
# trying to put a mutable element as a key
key_test = {[]:'a Test'}
print(key_test)
# there is a type error, which means a key shall not be mutable
# and values would not be repetitive, even if you do so, there will only appear once
a = {'key':123,'key':123}
print(a)

# there is no way to insert only one single element in dictionary, however there is an alternative
NASDAQ_code = {'BIDU':'Baidu','SINA':'Sina'}
NASDAQ_code['YOKU'] = 'Youku'
print(NASDAQ_code)

# while extend() is used in list to insert multiple elements, update() is used in dict
NASDAQ_code.update({'FB': 'Facebook', 'TSLA': 'Tesla'})
# del is used for deletion of element
del NASDAQ_code['FB']
# we use {} to define a dict but () to index
NASDAQ_code['TSLA']
# we cannot slice in dict
chart[1:4] # WRONG!

# tuple can be seen as a stable list, it is unchangable
# all the actions in list cannot be used except for indexing
letters = ('a','b','c','d','e','f','g')
letter[0]

# sets are similar to the mathematical meaning
# it cannot be sliced nor indexing, but calculation and insertion and deletion are acceptable
a_set = {1,2,3,4}
a_set.add(5)
a_set.discard(5)

# sorted() function does not change the element location in the list
# it first copies the list and then arrange
num_list = [6,2,7,4,1,3,5]
print(sorted(num_list))
sorted(num_list, reverse=True)

# when organizing the lists, we can use zip() to sort two lists
for a,b in zip(num,str):
    print(b, 'is', a)

# list comprehension
# a typical code for insertion of 10 elements
a = []
for i in range(1,11):
    a.append(i)
# now we use list comprehension
b = [i for i in range(1,11)]

# we can check the efficiency with time to compare both methods
import time

a = []
t0 = time.process_time()
for i in range(1, 20000):
    a.append(i)
print(time.process_time() - t0, 'seconds process time')

t0 = time.process_time()
b = [i for i in range(1, 20000)]
print(time.process_time() - t0, 'seconds process time')

# list comprehension examples
a = [i**2 for i in range(1,10)]
c = [j+1 for j in range(1,10)]
k = [n for n in range(1,10) if n % 2 ==0]
z = [letter.lower() for letter in 'ABCDEFGHIGKLMN']

# dict comprehension is a little different as it requires a value to be signed after creating a key
d = {i:i+1 for i in range(4)}

g = {i:j for i,j in zip(range(1,6),'abcde')}
g = {i:j.upper() for i,j in zip(range(1,6),'abcde')}

# how to get the exact location of each element in a list
# use enumerate()
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for num, letter in enumerate(letters):
    print(letter, 'is', num + 1)

# split() function split a context into different words
lyric = 'The night begin to shine, the night begin to shine'
words = lyric.split()

# class in python
class CocaCola():
    it_taste = 'So good!'
coke_for_bum = CocaCola()
coke_for_president = CocaCola()
print(coke_for_bum.it_taste)
print(coke_for_president.it_taste)

# adding class attribute
class Cocacola:
    formula = ['caffeine', 'sugar', 'water', 'soda']

# instance a var for class
coke_for_me = CocaCola()
coke_for_you = CocaCola()

# attribute references when typing '.' after class name
# property of attribute is indifferent to a normal var
for element in coke_for_me.formula:
    print(element)

class CocaCola:
    formula = ['caffeine', 'sugar', 'water', 'soda']
coke_for_China = CocaCola()
coke_for_China.local_logo = 'kekoukele' #create instance attribute
print(coke_for_China.local_logo) #print the instance attribute

# instance method in class
class CocaCola:
    formula = ['caffeine', 'sugar', 'water', 'soda']
    def drink(self):
        print('Energy!')
coke = CocaCola()
coke.drink()

# if we replace self with coke
class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def drink(coke):    # HERE！
        print('Energy!')

coke = CocaCola()
coke.drink()
# you can see the self is the instance itself

# there can also be an argument in instance method
class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def drink(self,how_much):

        if how_much == 'a sip':
            print('Cool~')
        elif how_much == 'whole bottle':
            print('Headache!')

ice_coke = CocaCola()
ice_coke.drink('a sip')

# __init__ is a reserved method in classes, known as a constructor in O-O concepts
# this method called when an object is created from the class
# and it allow the class to initialize the attributes of a class

class CocaCola():
    formula = ['caffeine','sugar','water','soda']
    def __init__(self):
        self.local_logo = 'KeKouKeLe'

    def drink(self):
        print('Energy!')

coke = CocaCola()
print(coke.local_logo)

# it also provides great flexibility
class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def __init__(self):

        for element in self.formula:
            print('Coke has {}!'.format(element))

    def drink(self):
        print('Energy!')

coke = CocaCola()

# except for the necessary 'self' parameter, __init__ can also have its own parameter
# it doesnt need to use such as 'obj.init()' to call such parameter
class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def __init__(self,logo_name):
        self.local_logo = logo_name

    def drink(self):
        print('Energy!')

coke = CocaCola('KeKouKele')
coke.local_logo

# new formula for CocaCola
class CocaCola:
    calories    = 140
    sodium      = 45
    total_carb  = 39
    caffeine    = 34
    ingredients =  [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
        'Caffeine'
    ]

    def __init__(self,logo_name):
        self.local_logo = logo_name

    def drink(self):
        print('You got {} cal energy!'.format(self.calories))

# inheritance of class
class CaffeineFree(CocaCola):
    caffeine = 0
    ingredients =  [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
    ]

coke_a = CaffeineFree('Cocacola-FREE')

coke_a.drink()

# If a class attribute is reassigned, will it affect the reference to the class attribute?
# Yes! It does!
class TestA:
    attr = 1
obj_a = TestA()

TestA.attr = 42
print(obj_a.attr)

# If the instance attribute is reassigned, will it affect the class attribute reference?
# No!
class TestA:
    attr = 1
obj_a = TestA()
obj_b = TestA()

obj_a.attr = 42

print(obj_b.attr)

# Class attribute has the same name as instance attributes, so what will be referenced later?
# instance attributes does!
class TestA:
    attr = 1
    def __init__(self):
        self.attr = 42

obj_a = TestA()

print(obj_a.attr)

# they all hidden in a special class attribute (_dict_)
# it is like a dictionary for storage and instance attributes
# use the third question above as the background and try these codes
print(TestA.__dict__)
print(obj_a.__dict__)

# so basically python class reference mechanism works as following:
# when obj.attr(), it first check if there is attr in instance
# yes then refer to the instance attr, if no then check if the class has attr
# yes then refer to the class attr, if no then error turns out

# these are some built-in class types
obj1 = 1
obj2 = 'String!'
obj3 = []
obj4 = {}

print(type(obj1),type(obj2),type(obj3),type(obj4))
