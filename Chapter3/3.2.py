# -*- coding: utf-8 -*-
#字符串：最底层的文本处理
import nltk
monty = 'Monty Python'
print(monty)

a = "asndsdf"
print(a)

b = """asdfa gsdfk jdklfj gksdjgfkljklsdgjfkl gjsdkjfd"""
print(b)

c = 'very'+'very'+'very'
print(c)

print('very'*3)

a = [1,2,3,4,5,6,5,4,3,2,1]
b = [' ' * 2 * (7 - i) + 'very' * i for i in a]
for line in b:
    print(b)

print monty

from nltk.corpus import gutenberg
raw = gutenberg.raw('melville-moby_dick.txt')
fdist = nltk.FreqDist(ch.lower() for ch in raw if ch.isalpha())
print(fdist.keys())


