'''
2.5 WordNet
  WordNet是面向语义的英语词典，与传统词典类似，但是结构更丰富。
'''


#意义与同义词
from nltk.corpus import wordnet as wn
print(wn.synsets('motorcar'))
print(wn.synset('car.n.01').lemma_names)
print(wn.synset('car.n.01').definition)
print(wn.synset('car.n.01').lemmas)

print(wn.synsets('car'))
for synset in wn.synsets('car'):
    print(synset.lemma_names)

from nltk.corpus import wordnet as wn
motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hyponyms()
print(types_of_motorcar[26])

paths = motorcar.hypernym_paths()
print(len(paths))

print(wn.synset('tree.n.01').part_meronyms())
print(wn.synset('tree.n.01').substance_meronyms())
print(wn.synset('tree.n.01').member_holonyms())

from nltk.corpus import wordnet as wn
right = wn.synset('right_whale.n.01')
orca = wn.synset('orca.n.01')
minke = wn.synset('minke_whale.n.01')
tortoise = wn.synset('tortoise.n.01')
novel = wn.synset('novel.n.01')
print(right.lowest_common_hypernyms(orca))





