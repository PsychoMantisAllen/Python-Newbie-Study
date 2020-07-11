# print out the even numbers between 1 ~ 100
def even_print():
    test_num = 1
    while test_num <= 100:
        if (test_num % 2) == 0:
            print(str(test_num))
            test_num = test_num + 1
        elif test_num > 100:
            break
        else:
            test_num = test_num + 1

even_print()

# online solution
def even_print():
    for i in range(1, 101):
        if i % 2 == 0:
            print(i)
even_print()

# make it simple
num = eval(input('Number:\n'))
print('{} is '.format(num) + ('even number.' if num % 2 == 0 else 'odd number.'))

# check if the number is integer
while True:
    try:
        num = int(input('Number:\n'))
    except ValueError:
        print('This is not an integer!')
        continue
    if num % 2 == 0:
        print('Even')
    else:
        print('Odd')
    break