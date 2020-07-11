# documents are nicely comma-separated form, use pandas.read_csv to load into a DataFrame
# pip install pandas
# pip install matplotlib
# pip install numpy
import pandas as pd
import numpy as np

names1880 = pd.read_csv('D://PycharmProject/Python Learning/names/yob1880.txt', names=['name', 'sex', 'births'])
names1880

# use the sum of the births column by sex as the total number of births in that year
names1880.groupby('sex').births.sum()

# assemble all of the data into a single DataFrame and add a year field -- using pandas.concat
# use 2010 as the last available year as an example
years = range(1880, 2011)

pieces = []
columns = ['name','sex','births']

for year in years:
    path = 'D://PycharmProject/Python Learning/names/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)

    frame['year'] = year
    pieces.append(frame)

# concatenate everything into a single DataFrame
# concat glues the DataFrame objects together row-wise by default
# if ignore_index = True, do not use the index values along the concatenation axis
# this is useful if you are concatenating objects where the concatenation axis does not have meaningful indexing info
names = pd.concat(pieces, ignore_index=True)

# aggregate the data at year and sex
# in pandas 1.0.1, cols need to be written in columns (full), and rows are replaced by index
total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
total_births.tail()
total_births.plot(title='Total Births by Sex and Year')

# insert a column prop with the fraction of babies given each name relative to the total number of births
def add_prop(group):
    births = group.births.astype(float) # integer division floors 整数相除不会有小数点，需要改成float (ignored if using python 3)

    group['prop'] = births / births.sum()
    return group
names = names.groupby(['year', 'sex']).apply(add_prop)

# sanity check to verify if prop column sums to 1
# use np.allclose to check if sums are sufficiently close to 1 (perhaps not exactly equal to)
# allcose is from numpy lib, remember to install it and import it at the beginning
np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1)

