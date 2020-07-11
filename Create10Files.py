# design a function that creates 10 txt file on Desktop and name them with number

def text_creator_10():
    desktop_path = 'C://Users/aleny/Desktop/'
    Total = 10
    while Total > 0:
        full_path = desktop_path + str(Total) + '.txt'
        Total = Total - 1
        file = open(full_path, 'w')
        file.close()
    else:
        print('Done!')

text_creator_10()

# online solution
def text_creation():
    desktop_path = 'C://Users/aleny/Desktop/'
    for name in range (1, 11):
        with open(desktop_path + str(name) + '.txt', 'w') as text:
            text.write(str(name))
            text.close()
            print('Done')

text_creation()