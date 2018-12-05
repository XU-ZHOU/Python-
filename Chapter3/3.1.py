# -*- coding: utf-8 -*-
'''
from __future__ import division
import nltk,re,pprint

from urllib import urlopen
url = "http://www.gutenberg.org/files/2554/2554.txt"
proxies = {'http':'http://www.someproxy.com:3128'}
raw = urlopen(url,proxies=proxies).read()
print(type(raw))
print(len(raw))
print(raw[:75])

#处理HTML
import BeautifulSoup
import nltk
from urllib import urlopen
url = "https://zhuanlan.zhihu.com/p/31977759"
html = urlopen(url).read()
print(html[:60])

raw = BeautifulSoup(html).get_text()
tokens = nltk.word_tokenize(raw)
print(tokens)

import feedparser
llog = feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")
print(llog['feed']['title'])
print(len(llog.entries))

import nltk
s = raw_input("Enter some text: ")
print("You typed",len(nltk.word_tokenize(s)),"words.")

import nltk
from nltk.corpus import gutenberg
raw = gutenberg.raw('melville-moby_dick.txt')
fdist = nltk.FreqDist(ch.lower() for ch in raw if ch.isalpha())
print(fdist.keys())
fdist.plot()

import nltk
path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
import codecs
f = codecs.open(path,encoding='latin2')
for line in f:
    line = line.strip()
    print(line.encode('unicode_escape'))

import unicodedata
lines = codecs.open(path,encoding='latin2').readlines()
line = lines[2]
print(line.encode('unicode_escape'))

'''
import nltk
path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
import codecs
f = codecs.open(path,encoding='latin2')
for line in f:
    line = line.strip()
    print(line.encode('unicode_escape'))
import unicodedata
lines = codecs.open(path,encoding='latin2').readlines()
line = lines[2]
print(line.encode('unicode_escape'))
print(line.find(u'zosta\u0142y'))

import re
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
print([w for w in wordlist if re.search('ed$',w)])

print([w for w in wordlist if re.search('^[ghi][mno][jlk][def]$',w)])

chat_words = sorted(set(w for w in nltk.corpus.nps_chat.words()))
print([w for w in chat_words if re.search('^m+i+n+e+$',w)])

wsj = sorted(set(nltk.corpus.treebank.words()))
print([w for w in wsj if re.search('^[0-9]+\.[0-9]+$',w)])

