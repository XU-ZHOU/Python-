#-*-coding:utf-8 -*-
#分割
import nltk
print(len(nltk.corpus.brown.words()) / len(nltk.corpus.brown.sents()))

sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
text = nltk.corpus.gutenberg.raw('chesterton-thursday.txt')
sents = sent_tokenizer.tokenize(text)
print(sents[171:181])

#分词
text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
seg1 = "0000000000000001000000000010000000000000000100000000000"
seg2 = "0100100100100001001001000010100100010010000100010010000"
def segment(text,segs):
    words = []
    last = 0
    for i in range(len(segs)):
        if segs[i] == '1':
            words.append(text[last:i+1])
            last = i+1
    words.append(text[last:])
    return words
print(segment(text,seg1))

#例3-3 计算存储词典和重构源文本的成本
def evaluate(text,segs):
    words = segment(text,segs)
    text_size = len(words)
    lexicon_size = len(' '.join(list(set(words))))
    return text_size+lexicon_size

#例3-4 使用模拟退火算法的非确定性搜索
from random import randint
def flip(segs,pos):
    return segs[:pos] + str(1-int(segs[pos])) + segs[pos+1:]

def flip_n(segs,n):
    for i in range(n):
        segs = flip(segs,randint(0,len(segs)-1))
    return segs

def anneal(text,segs,iterations,cooling_rate):
    temperature = float(len(segs))
    while temperature > 0.5:
        best_segs,best = segs,evaluate(text,segs)
        for i in range(iterations):
            guess = flip_n(segs,int(round(temperature)))
            score = evaluate(text,guess)
            if score < best:
                best,best_segs = score,guess
        score,segs = best,best_segs
        temperature = temperature / cooling_rate
        print(evaluate(text,segs),segment(text,segs))
    print
    return segs
