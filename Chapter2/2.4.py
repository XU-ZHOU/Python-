'''
2.4 词典资源
'''

'''
#过滤文本
import nltk
def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab.difference(english_vocab)
    return sorted(unusual)
print(unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt')))

#停用词
import nltk
from nltk.corpus import stopwords
print(stopwords.words('english'))

def content_fraction(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return len(content)/len(text)

print(content_fraction(nltk.corpus.reuters.words()))

#词谜
import nltk
puzzle_letters = nltk.FreqDist('egivrvonl')
obligatory = 'r'
wordlist = nltk.corpus.words.words()
print([w for w in wordlist if len(w) >= 6
       and obligatory in w
       and nltk.FreqDist(w) <= puzzle_letters])

       
import nltk
names = nltk.corpus.names
print(names.fileids())
male_names = names.words('male.txt')
female_name = names.words('female.txt')
print([w for w in male_names if w in female_name])

cfd = nltk.ConditionalFreqDist(
    (fileid,name[-1])
    for fileid in names.fileids()
    for name in names.words(fileid))
cfd.plot()

import nltk
entries = nltk.corpus.cmudict.entries()
print(len(entries))

for entry in entries[39943:39951]:
    print(entry)

for word,pron in entries:
    if len(pron) == 3:
        ph1,ph2,ph3 = pron
        if ph1 == 'P' and ph3 == 'T':
            print(word,ph2)

print([w for w,pron in entries if pron[-1] == 'M' and w[-1] == 'n'])

def stress(pron):
    return [char for phone in pron for char in phone if char.isdigit()]
print([w for w,pron in entries if stress(pron) == ['0','1','0','2','0']])

import nltk
entries = nltk.corpus.cmudict.entries()
p3 = [(pron[0]+'-'+pron[2],word)
      for (word,pron) in entries
      if pron[0] == 'P' and len(pron) == 3]
cfd = nltk.ConditionalFreqDist(p3)
for template in cfd.conditions():
    if len(cfd[template]) > 10:
        words = cfd[template].keys()
        wordlist = ' '.join(words)
        print(template,wordlist[:70]+"....")

prondict = nltk.corpus.cmudict.dict()
print(prondict['fire'])

text = ['natural','language','processing']
print([ph for w in text for ph in prondict[w][0]])

from nltk.corpus import swadesh
print(swadesh.fileids())

fr2en = swadesh.entries(['fr','en'])
print(fr2en)

translate = dict(fr2en)
print(translate['chien'])

de2en = swadesh.entries(['de','en'])
es2en = swadesh.entries(['es','en'])
translate.update(dict(de2en))
translate.update(dict(es2en))
print(translate['Hund'])
print(translate['perro'])

languages = ['en','de','nl','es','fr','pt','la']
for i in [139,140,141,142]:
    print(swadesh.entries(languages)[i])

'''
#词汇工具：ToolBox和Shoebox
from nltk.corpus import toolbox
print(toolbox.entries('rotokas.dic'))







