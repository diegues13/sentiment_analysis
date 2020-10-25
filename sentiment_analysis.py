import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

# Takes away puntuation chars
def strip_punctuation(word):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@', '-']
    x = word.strip()
    for mark in punctuation_chars:
        x = x.replace(mark, "")
    return x

# Count number of positive words
def get_pos(text_lines):
    text = text_lines.lower()
    text = strip_punctuation(text)
    lst_words = text.split()
    accum = 0
    for word in lst_words:
        if word in positive_words:
            accum += 1
    return accum

# Count number of negative words
def get_neg(text_lines):
    text = text_lines.lower()
    text = strip_punctuation(text)
    lst_words = text.split()
    accum = 0
    for word in lst_words:
        if word in negative_words:
            accum += 1
    return accum

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

# read file with tweeter data
with open('project_twitter_data.csv', 'r') as data:
    text = data.readlines()
    data_collected = []
    for line in text:
        line_data = line.split(',')
        tweet = strip_punctuation(line_data[0])
        num_retweets = line_data[1].strip()
        num_replies = line_data[2].strip()
        num_pos = get_pos(strip_punctuation(line_data[0]))
        num_neg = get_neg(strip_punctuation(line_data[0]))
        data_collected.append((num_retweets, num_replies, num_pos, num_neg, num_pos - num_neg))

del data_collected[0]

with open('resulting_data.csv', 'w') as data:
    data.write('Number of Retweets,Number of Replies,Positive Score,Negative Score,Net Score\n')
    for tweet in data_collected:
        text = '{},{},{},{},{}\n'.format(tweet[0], tweet[1], tweet[2], tweet[3], tweet[4])
        data.write(text)

y_data = [data[0] for data in data_collected]
x_data = [data[4] for data in data_collected]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_data, y_data, alpha=0.7, color='r', edgecolors='none')
ax.set_xlabel('Net Score')
ax.set_ylabel('Number of Retweets')
ax.set_title('Sentiment Analysis')
plt.show()