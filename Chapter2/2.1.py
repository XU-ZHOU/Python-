'''
第2章 获得文本语料和词汇资源
  2.1 获取文本语料库
  1、古腾堡语料库

'''

import nltk
'''
#古腾堡语料库
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

macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
print(macbeth_sentences)
longest_len = max([len(s) for s in macbeth_sentences])
print(longest_len)

#网络和聊天文本
from nltk.corpus import webtext
for fileid in webtext.fileids():
    print(fileid,webtext.raw(fileid)[:65])

from nltk.corpus import nps_chat
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
print(chatroom[123])

#布朗语料库
from nltk.corpus import brown
print(brown.categories())
print(brown.words(categories='news'))
print(brown.words(fileids=['cg22']))
print(brown.sents(categories=['news','editorial','reviews']))

from nltk.corpus import brown
news_text = brown.words(categories='news')
fdist = nltk.FreqDist([w.lower() for w in news_text])
modals = ['can','could','may','might','must','will']
for m in modals:
    print(m + ':',fdist[m])

cfd = nltk.ConditionalFreqDist(
    (genre,word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))

genres = ['news','religion','hobbies','science_fiction','romance','humor']
modals = ['can','could','may','might','must','will']
cfd.tabulate(conditions=genres,samples=modals)
print(cfd)


#路透社语料库
from nltk.corpus import reuters
print(reuters.fileids())
print(reuters.categories())
print(reuters.categories('training/9865'))
print(reuters.categories(['training/9865','training/9880']))
print(reuters.fileids('barley'))
print(reuters.fileids(['barley','corn']))

#就职演说语料库
from nltk.corpus import inaugural
print(inaugural.fileids())

cfd = nltk.ConditionalFreqDist(
    (target,fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america','citizen']
    if w.lower().startswith(target))
cfd.plot()


#标注文本语料库
from nltk.corpus import udhr
languages = ['Chickasaw','English','German_Deutsch','Greenlandic_Inuktikut',
             'Hungarian_Magyar','Ibibio_Efik']
cfd = nltk.ConditionalFreqDist(
    (lang,len(word))
    for lang in languages
    for word in udhr.words(lang + '-Latinl'))
cfd.plot(cumulative = True)

#使用双连词生成随机文本
sent = ['In','the','beginning','God','created','the','heaven','and','the','earth']
nltk.bigrams(sent)
'''

def generate_model(cfdist,word,num=15):
    for i in range(num):
        print(word)
        word = cfdist[word].max()
text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)
print(cfd['living'])

#例2-3
def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab.difference(english_vocab)
    return sorted(unusual)

print(unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt')))
print(unusual_words(nltk.corpus.nps_chat.words()))

from nltk.corpus import stopwords
print(stopwords.words('english'))

def content_fraction(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return len(content)/len(text)

print(content_fraction(nltk.corpus.reuters.words()))

#2-6
puzzle_letters = nltk.FreqDist('egivrvonl')
obligatory = 'r'
wordlist = nltk.corpus.words.words()
obj = [w for w in wordlist if len(w) >= 6
                    and obligatory in  w
                    and nltk.FreqDist(w) <= puzzle_letters]
print(obj)

names = nltk.corpus.names
male_names = names.words('male.txt')
female_names = names.words('female.txt')
sexname = [w for w in male_names if w in female_names]
print(sexname)

cfd = nltk.ConditionalFreqDist(
    (fileid,name[-1])
    for fileid in names.fileids()
    for name in names.words(fileid))
cfd.plot()

#发音的词典
entries = nltk.corpus.cmudict.entries()
print(len(entries))

for entry in entries[39943:39951]:
    print(entry)

for word,pron in entries:
    if len(pron) == 3:
        ph1,ph2,ph3 = pron
        if ph1 == 'P' and ph3 == 'T':
            print(word,ph2)

syllable = ['N','IHO','K','S']
words = [word for word,pron in entries if pron[-4:] == syllable]
print(words)

from nltk.corpus import swadesh
print(swadesh.fileids())

fr2en = swadesh.entries(['fr','en'])
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

from nltk.corpus import toolbox
print(toolbox.entries('rotokas.dic'))
