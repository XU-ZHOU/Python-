#-*-coding:<utf-8>-*-

import re
import nltk
word = 'supercalifragilisticexpialidocious'
print(re.findall(r'[aeiou]',word))
print(len(re.findall(r'[aeiou]',word)))

wsj = sorted(set(nltk.corpus.treebank.words()))
fd = nltk.FreqDist(vs for word in wsj
                   for vs in re.findall(r'[aeiou]{2,}',word))
print(fd.items())

import re
import nltk

regexp = r'^[AEIOUaeiou]+ | [AEIOUaeiou] + $ | [^AEIOUaeiou]'
def compress(word):
    pieces = re.findall(regexp,word)
    return ''.join(pieces)
english_udhr = nltk.corpus.udhr.words('English-Latin1')
print(nltk.tokenwrap(compress(w) for w in english_udhr[:75]))

rotokas_words = nltk.corpus.toolbox.words('rotokas.dic')
cvs = [cv for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]',w)]
cfd = nltk.ConditionalFreqDist(cvs)
print(cfd.tabulate())

cv_word_pairs = [(cv,w) for w in rotokas_words
                        for cv in re.findall(r'[ptksvr][aeiou]',w)]
cv_index = nltk.Index(cv_word_pairs)
print(cv_index['su'])
print(cv_index['po'])

import re
import nltk
def stem(word):
    for suffix in ['ing','ly','ed','ious','ies','ive','es','s','ment']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word
print(re.findall(r'^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$','processing'))

def stem(word):
    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
    stem,suffix = re.findall(regexp,word)[0]
    return stem


from nltk.corpus import gutenberg,nps_chat
import nltk
moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
print(moby.findall(r"<a> (<.*>) <man>"))
chat = nltk.Text(nps_chat.words())
print(chat.findall(r"<.*><.*><bro>"))
print(chat.findall(r"<1.*>{3,}"))

