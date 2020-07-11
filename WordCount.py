# https://blog.csdn.net/lqzdreamer/article/details/76549256
# if your code has decoding issue, check this one that may help solving the problem
# another method is adding a encoding option of utf-8
# the file is encoding writing as utf-8 to transform as gbk form
path1 = 'C://Users/aleny/Desktop/Walden.txt'
file = open(path1, encoding='gb18030', errors='ignore')
file2 = open('C://Users/aleny/Desktop/Walden2.txt', 'w')
file2.write(file.read())
file.close()
file2.close()

with open('C://Users/aleny/Desktop/Walden.txt','r', encoding='utf-8') as text:
    words = text.read().split()
    print(words)
    for word in words:
        print('{}-{} times'.format(word,words.count(word)))

# some problems are showing up with direct counting
# some punctuated words are counted individually
# some words show the number of occurrences more than once
# because Python is case-sensitive, words that begin with an uppercase are counted separately
# we need to handle the file from the beginning

import string
with open(path1, 'r', encoding='utf-8') as text:
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    words_index = set(words)
    counts_dict = {index:words.count(index) for index in words_index}

for word in sorted(counts_dict, key=lambda x: counts_dict[x], reverse=True):
    print('{} -- {} times'.format(word, counts_dict[word]))
