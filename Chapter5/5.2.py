#-*-coding:utf-8 -*-


#标注语料库
import nltk
tagged_token = nltk.tag.str2tuple('fly/NN')
print(tagged_token)
print(tagged_token[0])

print(nltk.corpus.brown.tagged_words())

from nltk.corpus import brown
brown_news_tagged = brown.tagged_words(categories='news')
tag_fd = nltk.FreqDist(tag for (word,tag) in brown_news_tagged)
print(tag_fd.keys())

word_tag_pairs = nltk.bigrams(brown_news_tagged)
print(list(nltk.FreqDist(a[1] for (a,b) in word_tag_pairs if b[1] == 'NN')))

#动词
import nltk
wsj = nltk.corpus.treebank.tagged_words()
word_tag_fd = nltk.FreqDist(wsj)
print([word+"/"+tag for (word,tag) in word_tag_fd if tag.startswith('V')])

cfd1 = nltk.ConditionalFreqDist(wsj)
print(cfd1['yield'].keys())
print(cfd1['cut'].keys())

cfd2 = nltk.ConditionalFreqDist((tag,word) for (word,tag) in wsj)
print(cfd2['VB'].keys())
print(w for w in cfd1.conditions() if 'VBD' in cfd1[w] and 'VBN' in cfd1[w])

#形容词和副词
import nltk
from nltk.corpus import brown
def findtags(tag_prefix,tagged_text):
    cfd = nltk.ConditionalFreqDist((tag,word) for (word,tag) in tagged_text if tag.startswith(tag_prefix))
    return dict((tag,cfd[tag].keys()[:5]) for tag in cfd.conditions())
tagdict = findtags('NN',nltk.corpus.brown.tagged_words(categories='news'))
for tag in sorted(tagdict):
    print(tag,tagdict[tag])

brown_learned_text = brown.words(categories='learned')
print(sorted(set(b for (a,b) in nltk.bigrams(brown_learned_text) if a == 'often')))
brown_lrnd_tagged = brown.tagged_words(categories='learned')
tags = [b[1] for (a,b) in nltk.bigrams(brown_lrnd_tagged) if a[0]=='often']
fd = nltk.FreqDist(tags)
print(fd.tabulate())

from nltk.corpus import brown
def process(sentence):
    for (w1,t1),(w2,t2),(w3,t3) in nltk.trigrams(sentence):
        if (t1.startswith('V') and t2 == 'TO' and t3.startswith('V')):
            print(w1,w2,w3)
for tagged_sent in brown.tagged_sents():
    process(tagged_sent)

brown_news_tagged = brown.tagged_words(categories='news')
data = nltk.ConditionalFreqDist((word.lower(),tag) for (word,tag) in brown_news_tagged)
for word in data.conditions():
    if len(data[word]) > 3:
        tags = data[word].keys()
        print(word,' '.join(tags))

import nltk
alice = nltk.corpus.gutenberg.words('carroll-alice.txt')
vocab = nltk.FreqDist(alice)
v1000 = list(vocab)[:1000]
mapping = nltk.defaultdict(lambda : 'UNK')
for v in v1000:
    mapping[v] = v
alice2 = [mapping[v] for v in alice]
print(alice2[:100])

counts = nltk.defaultdict(int)
from nltk.corpus import brown
for (word,tag) in brown.tagged_words(categories='news'):
    counts[tag] += 1
print(counts['NN'])
print(list(counts))

from operator import itemgetter
print(sorted(counts.items(),key=itemgetter(1),reverse=True))


#颠倒字典
pos = {'colorless':'ADJ','ideas':'N','sleep':'V','furiously':'ADV'}
pos2 = dict((value,key) for (key,value) in pos.items())
print(pos2['N'])

