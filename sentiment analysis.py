# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import re
from collections import Counter

NEGWORDS = ["not", "no", "none", "neither", "never", "nobody", "n't", 'nor']
# STOPWORDS = ["an", "a", "the"] + NEGWORDS
STOPWORDS = ["an", "a", "the", "or", "and", "thou", "must", "that", "this", "self", "unless", "behind", "for", "which",
             "whose", "can", "else", "some", "will", "so", "from", "to", "by", "within", "of", "upon", "th", "with",
             "it"]


def _remove_stopwords(txt):
    """Delete from txt all words contained in STOPWORDS."""
    words = txt.split()

    for i, word in enumerate(words):
        if word in STOPWORDS:
            words[i] = " "
    return (" ".join(words))


with open('digitalcoins.txt', 'r', encoding='utf-8') as digitalcoins_read:
    digitalcoins_string = digitalcoins_read.read()

digitalcoins_split = str.split(digitalcoins_string, sep=',')
print(digitalcoins_split)
len(digitalcoins_split)

ndct = ''
with open('bl_negative.csv', 'r', encoding='utf-8', errors='ignore') as infile:
    for line in infile:
        ndct = ndct + line
# create a list of negative words
ndct = ndct.split('\n')
ndct = [entry for entry in ndct]
len(ndct)

pdct = ''
with open('bl_positive.csv', 'r', encoding='utf-8', errors='ignore') as infile:
    for line in infile:
        pdct = pdct + line
pdct = pdct.split('\n')
pdct = [entry for entry in pdct]
len(pdct)

def decompose_word(doc):
    txt = []
    for word in doc:
        txt.extend(word.split())
    return txt


def wordcount(words, dct):
    counting = Counter(words)
    count = []
    for key, value in counting.items():
        if key in dct:
            count.append([key, value])
    return count


nwords = len(tokens)

nwc = wordcount(tokens, ndct)

pwc = wordcount(tokens, pdct)

ntot, ptot = 0, 0
for i in range(len(nwc)):
    ntot += nwc[i][1]

for i in range(len(pwc)):
    ptot += pwc[i][1]


print('Positive words:')
for i in range(len(pwc)):
    print(str(pwc[i][0]) + ': ' + str(pwc[i][1]))
print('Total number of positive words: ' + str(ptot))
print('\n')
print('Percentage of positive words: ' + str(round(ptot / nwords, 4)))
print('\n')
print('Negative words:')
for i in range(len(nwc)):
    print(str(nwc[i][0]) + ': ' + str(nwc[i][1]))
print('Total number of negative words: ' + str(ntot))
print('\n')
print('Percentage of negative words: ' + str(round(ntot / nwords, 4)))