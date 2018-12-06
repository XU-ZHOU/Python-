
#分块：用于实体识别的基本技术是分块。

#例7-1 一个简单的基于正则表达式的NP分块器例子
import nltk
sentence = [("the","DT"),("little","JJ"),("yellow","JJ"),("dog","NN"),("barked","VBD"),("at","IN"),("the","DT"),("cat","NN")]
grammar = "NP:{<DT>?<JJ>?<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print(result)

#用正则表达式分块
#例7-2 简单的名词短语分块器
grammar = r"""
    NP:{<DT|PP\$>?<JJ>*<NN>}
       {<NNP>+}
"""
import nltk
cp = nltk.RegexpParser(grammar)
sentence = [("Rapunzel","NNP"),("let","VBD"),("down","RP"),("her","PP$"),("long","JJ"),("golden","JJ"),("hair","NN")]
print(cp.parse(sentence))

nouns = [("money","NN"),("market","NN"),("fund","NN")]
grammar = "NP:{<NN><NN>}"
cp = nltk.RegexpParser(grammar)
print(cp.parse(nouns))

#探索文本语料库
import nltk
cp = nltk.RegexpParser('CHUNK:{<V.*><TO><V.*>}')
brown = nltk.corpus.brown
for sent in brown.tagged_sents():
    tree = cp.parse(sent)
    for subtree in tree.subtrees():
        if subtree.node == 'CHUNK':
            print(subtree)





#缝隙
#例7-3 简单的加缝隙
import nltk
grammar = r"""
    NP:
    {<.*>+}
    {<VBD|NN>+}
"""
sentence = [('the',"DT"),("little","JJ"),("yellow","JJ"),("dog","NN"),("barked","VBD"),("at","IN"),("the","DT")]
cp = nltk.RegexpParser(grammar)
print(cp.parse(sentence))

