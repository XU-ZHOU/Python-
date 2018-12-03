'''
条件频率分布
'''
'''
import nltk
from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist(
    (genre,word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))

genre_word = [(genre,word)
              for genre in ['news','romance']
              for word in brown.words(categories=genre)]
print(len(genre_word))
print(genre_word[:4])
print(genre_word[-4:])

cfd = nltk.ConditionalFreqDist(genre_word)
print(cfd)
print(cfd.conditions())

print(cfd['news'])
print(cfd['romance'])
print(list(cfd['romance']))

import nltk
def generate_model(cfdist,word,num=15):
    for i in range(num):
        print(word,word = cfdist[word].max())
text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)
print(cfd['living'])

def plural(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh','ch']:
        return word + 'es'
    elif word.endswith('an'):
        return word[:-2] + 'en'
    else:
        return word+'s'
print(plural('fairy'))
print(plural('woman'))
'''





