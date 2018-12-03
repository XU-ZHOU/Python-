'''
第2章 获得文本语料和词汇资源
2.1 获取文本语料库

'''

import nltk
print(nltk.corpus.gutenberg.fileids())
emma = nltk.corpus.gutenberg.words('austen-emma.txt')
print(len(emma))
emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
print(emma.concordance("surprize"))

from nltk.corpus import gutenberg
print(gutenberg.fileids())

for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
    print(int(num_chars/num_words),int(num_words/num_sents),int(num_words/num_vocab),fileid)

from nltk.corpus import webtext
for fileid in webtext.fileids():
    print(fileid,webtext.raw(fileid)[:65],'...')

from nltk.corpus import nps_chat
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
print(chatroom[123])

from nltk.corpus import brown
print(brown.categories())

import nltk
from nltk.corpus import brown
news_text = brown.words(categories='news')
fdist = nltk.FreqDist([w.lower() for w in news_text])
modals = ['can','could','may','might','must','will']
for m in modals:
    print(m+':',fdist[m])
    
import nltk
from nltk.corpus import brown
reviews_text = brown.words(categories='reviews')
fdist = nltk.FreqDist([w.lower() for w in reviews_text])
modals = ['what','when','where','who','why']
for m in modals:
    print(m+':',fdist[m])


import nltk
from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist((genre,word)
                               for genre in brown.categories()
                               for word in brown.words(categories=genre))
genres = ['news','religion','hobbies','science_fiction','romance','humor']
modals = ['can','could','may','might','must','will']
print(cfd.tabulate(conditions=genres,samples=modals))

from nltk.corpus import reuters
print(reuters.fileids())
print(reuters.categories())
print(reuters.categories('training/9865'))
print(reuters.categories(['training/9865','training/9880']))

from nltk.corpus import inaugural
print(inaugural.fileids())
print([fileid[:4] for fileid in inaugural.fileids()])

from nltk.corpus import inaugural
import nltk
cfd = nltk.ConditionalFreqDist((target,fileid[:4])
                               for fileid in inaugural.fileids()
                               for w in inaugural.words(fileid)
                               for target in ['america','citizen']
                               if w.lower().startswith(target))
cfd.plot()

import nltk
print(nltk.corpus.cess_esp.words())

import nltk
from nltk.corpus import udhr
languages = ['Chicksaw','English','German_Deutsch','Greenlandic_Inuktikut','Hungarian_Magyar','Ibibio_Efik']
cfd = nltk.ConditionalFreqDist(
    (lang,len(word))
    for lang in languages
    for word in udhr.words(lang+'-Latin1'))
cfd.plot(cumulative=True)






