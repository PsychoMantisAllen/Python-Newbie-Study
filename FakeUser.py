# when using python for data analysis or develop a web, we sometimes need meaningless fake data
# lets create a tool to fill up a fake user data

# lets process the first name and last name doc first
ln_path = 'C://Users/aleny/Desktop/last_name.txt'
fn_path = 'C://Users/aleny/Desktop/first_name.txt'
fn  = []
ln1 = [] # single char last name
ln2 = [] # double char last name
with open(fn_path,'r', encoding='utf-8') as f:
    for line in f.readlines():
        fn.append(line.split('\n')[0]) # if dont understand, try to split one line of it and see the return
print(fn)
with open(ln_path,'r', encoding='utf-8') as f:
    for line in f.readlines():
        if len(line.split('\n')[0]) == 1:
            ln1.append(line.split('\n')[0])
        else:
            ln2.append(line.split('\n')[0])
print(ln1)
print('='*70)
print(ln2)

# after print we need to change fn, ln1, ln2 to tuple, as tuple save more memories than lists
# copy the print result to tuplep, we need to transform them into constant

# now we can define our class FakeUser
import random
class FakeUser:
    def fake_name(self, one_word = False, two_words = False):
        if one_word:
            full_name = random.choice(fn) + random.choice(ln1)
        elif two_words:
            full_name = random.choice(fn) + random.choice(ln2)
        else:
            full_name = random.choice(fn) + random.choice(ln1 + ln2)
        print(full_name)

    def fake_gender(self):
        gender = random.choice(['Male', 'Female', 'Unspecified'])
        print(gender)

# now we define the subclass (inheritance)
class SnsUser(FakeUser):
    def get_followers(self, few = True, a_lot = False):
        if few:
            followers = random.randrange(1, 50)
        elif a_lot:
            followers = random.randrange(200, 10000)
        print(followers)


user_a = FakeUser()
user_b = SnsUser()
user_a.fake_name(two_words=True)
user_b.get_followers(a_lot=True)

# however, such method still requires us to manually generate random names
# replace all print() to yield function and put an extra loop
# we can use it like a range function as such
class FakeUser():
    def fake_name(self, amount = 1, one_word = False, two_words = False):
        n = 0
        while n <= amount:
            if one_word:
                full_name = random.choice(fn) + random.choice(ln1)
            elif two_words:
                full_name = random.choice(fn) + random.choice(ln2)
            else:
                full_name = random.choice(fn) + random.choice(ln1 + ln2)
            yield full_name
            n += 1
    def fake_gender(self, amount = 1):
        n = 0
        while n <= amount:
            gender = random.choice(['Male', 'Female', 'Unspecified'])
            yield gender
            n += 1

class SnsUser(FakeUser):
    def get_followers(self, amount = 1, few = True, a_lot = False):
        n = 0
        while n <= amount:
            if few:
                followers = random.randrange(1, 50)
            elif a_lot:
                followers = random.randrange(200, 10000)
            yield followers
            n += 1

user_a = FakeUser()
user_b = SnsUser()
for name in user_a.fake_name(30):
    print(name)
for gender in user_a.fake_gender(30):
    print(gender)

# here we use a new concept called generator
# if we yield a return in any loop, we can get sth like range() function

