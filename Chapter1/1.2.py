#NLTK入门
from nltk.book import *
#print(text1)
#print(text1.concordance("monstrous"))
#text4.dispersion_plot(["citizens","democracy","feedom","duties","America"])
#text3.generate()
#sorted(set(text3))
#print(len(set(text3)))
print(text5.count('lol'))
print(100 * text5.count('lol') / len(text5))

def lexical_diversity(text):
    return len(text) / len(set(text))

def percentage(count,total):
    return 100 * count / total

sent1 = ['Call','me','Ishmael','.']
print(sent1)