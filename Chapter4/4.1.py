#-*-coding:utf-8 -*-
'''
第4章 编写结构化程序
import nltk
words = ['I','turned','off','the','spectroroute']
tags = ['noun','verb','prep','det','noun']
print(zip(words,tags))
print(list(enumerate(words)))

text = nltk.corpus.nps_chat.words()
cut = int(0.9*len(text))
training_data,test_data = text[:cut],text[cut:]
print(text == training_data + test_data)
print(len(training_data)/len(test_data))

words = 'I turned off the spectroroute'.split()
wordlens = [(len(word),word) for word in words]
wordlens.sort()
print(' '.join(w for (_,w) in wordlens))

#产生器表达式
import nltk
text =
"it means just what I choose it to mean - neither more nor less.
print([w.lower() for w in nltk.word_tokenize(text)])

tokens = nltk.corpus.brown.words(categories='news')
total = sum(len(t) for t in tokens)
print(total/len(tokens))

fd = nltk.FreqDist(nltk.corpus.brown.words())
cumulative = 0.0
for rank,word in enumerate(fd):
    cumulative += fd[word] * 100 / fd.N()
    print("%3d %6.2f%% %s" % (rank+1,cumulative,word))
    if cumulative > 25:
        break
'''
import nltk
text = nltk.corpus.gutenberg.words('milton-paradise.txt')
longest = ''
for word in text:
    if len(word) > len(longest):
        longest = word
print(longest)

maxlen = max(len(word) for word in text)
print([word for word in text if len(word) == maxlen])

sent = ['The','dog','gave','John','the','newspaper']
n = 3
print([sent[i:i+n] for i in range(len(sent)-n+1)])

m,n = 3,7
array = [[set() for i in range(n)] for j in range(m)]
array[2][5].add('Alice')
print(array)
