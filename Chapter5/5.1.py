#-*-coding:utf-8 -*-
'''
第5章 分类和标注词汇
'''
import nltk
text = nltk.word_tokenize("And now for something completely different")
print(nltk.pos_tag(text))

text = nltk.word_tokenize("They refuse to permit us to obtain the refuse permit")
print(nltk.pos_tag(text))

text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
print(text.similar('woman'))
print(text.similar('over'))
print(text.similar('the'))

