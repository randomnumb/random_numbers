__author__ = 'random_numb'


import praw
import numpy as np
import pickle

def get_numbs():
    with open('/Users/random_numb/pycharmprojects/random_numbers/redditpw.txt') as f:
        pw = f.readline().rstrip('\n')
        secret = f.readline()

    bot = praw.Reddit(user_agent='random_numbers',
                      client_id='mHHqSUoc5khbfQ',
                      client_secret=secret,
                      username='random_numb',
                      password=pw)

    numbs = []

    for sub in bot.subreddit('random_numb').submissions():
        if str(sub.title).startswith('Random Number:'):
            numb = sub.title[14:]
            numbs.append(float(numb))
        else:
            numbs.append(float(sub.title))

    votes = []

    for sub in bot.subreddit('random_numb').submissions():
            numbs.append(float(sub.title))

    with open('numbfile', 'wb') as fp:
        pickle.dump(numbs, fp)

def update_side():
    with open('numbfile', 'rb') as fp:
        numbs = pickle.load(fp)

    avg = np.mean(numbs)
    print(avg)
    std = np.std(numbs)
    print(std)
    min = np.min(numbs)
    print(min)
    max = np.max(numbs)
    print(max)
    length= len(numbs)
    print(length)


    with open('/Users/random_numb/pycharmprojects/random_numbers/redditpw.txt') as f:
        pw = f.readline().rstrip('\n')
        secret = f.readline()

    bot = praw.Reddit(user_agent='random_numbers',
                      client_id='mHHqSUoc5khbfQ',
                      client_secret=secret,
                      username='random_numb',
                      password=pw)

    new_sidebar = '''
    number of random numbers = ''' + str(length) + '''\n
    max = ''' + str(max) + '''\n
    min = ''' + str(min) + '''\n
    avgerage = ''' + str(avg) + '''\n
    standard deviation = ''' + str(std)

    print(new_sidebar)

    bot.subreddit('random_numb').mod.update(description=new_sidebar)

    print(bot.subreddit('random_numb').mod.settings())

def export_stats():

     bot = praw.Reddit(user_agent='random_numbers',
                      client_id='mHHqSUoc5khbfQ',
                      client_secret=secret,
                      username='random_numb',
                      password=pw)

    with open('numbs.csv', 'wb') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(numbs)


if __name__ == "__main__":
    get_numbs()
    update_side()