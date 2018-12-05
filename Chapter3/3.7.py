#-*-coding:utf-8 -*-
'''
3.7 用正则表达式为文本分词
'''

#分词的简单方法
import re
import nltk
raw = """'When I'M A Duchess,'she said to herself,(not in a very hopeful tone...though),'
'I won't have any pepper in my kitchen AT ALL.Soup does very... well without--Maybe it's always pepper that makes people hot-tempered,'..."""
print(re.split(r' ',raw))
print(re.split(r'[ \t\n]+',raw))
print(re.split(r'\s+',raw))
print(re.split(r'\W+',raw))

#NLTK的正则表达式分词器
text = 'That U.S.A. poster-print costs $12.40...'
pattern = r'''(?x)
              ([A-Z]\.)+
              | \w+(-\w+)*
              | \$?\d+(\.\d+)?%?
              | \.\.\.
              | [][.,;"'?():-_']'''
print(nltk.regexp_tokenize(text,pattern))

