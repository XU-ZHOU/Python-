#命名体识别

import nltk
sent = nltk.corpus.treebank.tagged_sents()
print(nltk.ne_chunk(sent,binary=True))
