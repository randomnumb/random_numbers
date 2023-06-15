__author__ = 'random_numb'

import praw
import random
import pickle
import numpy as np

with open('/Users/random_numb/pycharmprojects/random_numbers/redditpw.txt') as f:
    pw = f.readline().rstrip('\n')
    secret = f.readline()

bot = praw.Reddit(user_agent='random_numbers',
                  client_id='mHHqSUoc5khbfQ',
                  client_secret=secret,
                  username='random_numb',
                  password=pw)

rand = str(random.random()*10**random.randint(0,10))
print(rand)

bot.subreddit('random_numb').submit(rand,selftext=rand)

with open('numbfile', 'rb') as fp:
        numbs = pickle.load(fp)

numbs.append(float(rand))

avg = np.mean(numbs)
std = np.std(numbs)
min = np.min(numbs)
max = np.max(numbs)
length = len(numbs)

new_sidebar = '''This is how the universe was created.

number of random numbers = ''' + str(length) + '''\n
max = ''' + str(max) + '''\n
min = ''' + str(min) + '''\n
avgerage = ''' + str(avg) + '''\n
standard deviation = ''' + str(std)

print(new_sidebar)

bot.subreddit('random_numb').mod.update(description=new_sidebar)

with open('numbfile', 'wb') as fp:
    pickle.dump(numbs, fp)


