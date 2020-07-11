import pandas as pd

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
mnames = ['movie_id', 'title', 'genres']

uadd = 'D://PycharmProject/Python Learning/ml-1m/users.dat'
radd = 'D://PycharmProject/Python Learning/ml-1m/ratings.dat'
madd = 'D://PycharmProject/Python Learning/ml-1m/movies.dat'

users = pd.read_table(uadd, sep = '::', header = None, names = unames)
ratings = pd.read_table(radd, sep = '::', header = None, names = rnames)
movies = pd.read_table(madd, sep = '::', header = None, names = mnames)

# there could be parser warning here as the 'sep' is longer than 1 char and different from '\s+'
# read pandas read_table documentation: If sep is None, the C engine cannot automatically detect the separator, but the Python parsing engine can
# the C engine is faster while the python engine is more feature-complete
# to avoid such parser warning, simply add a engine = 'python' line

users = pd.read_table(uadd, sep = '::', header = None, names = unames, engine = 'python')
ratings = pd.read_table(radd, sep = '::', header = None, names = rnames, engine = 'python')
movies = pd.read_table(madd, sep = '::', header = None, names = mnames, engine = 'python')

# verify the results
users[:5]
ratings[:5]
movies[:5]
ratings

# merge three tables so we can easily manipulate the data
data = pd.merge(pd.merge(ratings, users), movies)

# to get mean movie ratings for each film grouped by gender, use pivot_table
# in pandas 1.0.1, cols need to be written in columns (full), and rows are replaced by index
mean_ratings = data.pivot_table('ratings', index = 'title', columns = 'gender', aggfunc = 'mean')
mean_ratings[:5]

# filter down movies that received at least 250 ratings
# group the data by title and use size() to get a series of group sizes for each title
ratings_by_title = data.groupby('title').size()
ratings_by_title[:10]

active_titles = ratings_by_title.index[ratings_by_title >= 250]
active_titles
# this can be used to select rows from mean_ratings above
mean_ratings = mean_ratings.ix[active_titles]
mean_ratings

# to see the top films among female viewers
top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)
top_female_ratings[:10]

# to find the movies that are most divisive between male and female
# 1st way is to add a column to mean_ratings containing the difference in means
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_index(by='diff')
sorted_by_diff[:15] # here u get movies that are preferred by women
sorted_by_diff[::-1][:15] # reverse the order, now u have by men

# variance of the ratings can show disagreement in movies
# standard deviation of rating grouped by title
rating_std_by_title = data.groupby('title')['rating'].std()
# filter down to active titles
rating_std_by_title = rating_std_by_title.ix[active_titles]
# order series by value in descending order
rating_std_by_title.order(ascending=False)[:10]
