# big or small game
import random

def big_or_small_v1():
    print('<<<<< GAME STARTS! >>>>>')
    bet = input('Big or Small: ').lower()
    print('<<<<< ROLL THE DICE! >>>>>')

    point1 = random.randrange(1, 7)
    point2 = random.randrange(1, 7)
    point3 = random.randrange(1, 7)

    point_list = [point1, point2, point3]
    total_point = sum(point_list)

    win_word = 'The points are [{}, {}, {}] You Win!'.format(point1, point2, point3)
    lose_word = 'The points are [{}, {}, {}] You Lose!'.format(point1, point2, point3)

    if 11 <= total_point <= 18 and bet == 'big':
        print(win_word)
    elif 3 <= total_point <= 10 and bet == 'small':
        print(win_word)
    elif 11 <= total_point <= 18 and bet == 'small':
        print(lose_word)
    elif 3 <= total_point <= 10 and 'big':
        print(lose_word)
    else:
        print('Invalid Input! Try Again!')
        return False

big_or_small_v1()

# online solution
import random
def roll_dice(numbers = 3, points = None):
    print('<<<<< ROLL THE DICE! >>>>>')
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1, 7)
        points.append(point)
        numbers = numbers - 1
    return points

def roll_result(total):
    isBig = 11 <= total <= 18
    isSmall = 3 <= total <= 10
    if isBig:
        return 'Big'.lower()
    elif isSmall:
        return 'Small'.lower()

def start_game():
    print('<<<<< GAME STARTS! >>>>>')
    choices = ['Big', 'Small']
    your_choice = input('Big or Small :')
    if your_choice in choices:
        points = roll_dice()
        total = sum(points)
        youWin = your_choice == roll_result(total)

        if youWin:
            print('The points are', points, 'You win!')
        else:
            print('The points are', points, 'You lose!')
    else:
        print('Invalid Words')
        start_game()

start_game()

# another solution
import random

def big_or_small():
    print('<<<<< GAME STARTS! >>>>>')
    # lower function turns all the letters into small cap
    bet = input('Big or Small: ').lower()
    print('<<<<< ROLL THE DICE! >>>>>')

    point_list = [random.randrange(1, 7), random.randrange(1, 7), random.randrange(1, 7)]
    total_point = sum(point_list)

    isWin = False
    if 11 <= total_point <= 18 and bet == 'big':
        isWin = True
    elif 3 <= total_point <= 10 and bet == 'small':
        isWin = True
    elif 11 <= total_point <= 18 and bet == 'small':
        isWin = False
    elif 3 <= total_point <= 10 and bet == 'big':
        isWin = False
    else:
        print('Invalid Input, try again')
        return False

    print('The points are {} You {}!'.format(point_list, 'win' if isWin else 'lose'))
    return True

while (True):
    if big_or_small() == True:
        break


# upgraded version (adding elements of wager and odds)
# initial amount would be $1000
# odds will be 100%

def start_game_v1():
    c_amount = 1000
    while c_amount > 0:
        print('<<<<< GAME STARTS! >>>>>')
        choices = ['big', 'small']
        your_choice = input('Big or Small :').lower()

        if your_choice in choices:
            bet_choice = int(input('How much you wanna bet? - '))
            points = roll_dice()
            total = sum(points)
            youWin = your_choice == roll_result(total)

            if youWin:
                print('The point is', points, 'You Win!')
                print('You gain {}, you have {} now'.format(bet_choice, c_amount + bet_choice))
                c_amount = c_amount + bet_choice
            else:
                print('The point is', points, 'You Lose!')
                print('You lost {}, you have {} now'.format(bet_choice, c_amount - bet_choice))
                c_amount = c_amount - bet_choice
        else:
            print('Invalid Input!')
    else:
        print('GAME OVER')

while True:
    if start_game_v1() == True:
        break
