#-*-coding:utf-8 -*-
'''
3.6 规范化文本
'''
import nltk
raw = """DENNIS:Listen,strange women lying in ponds distributing swords
...is no bisis for a system of government.Supreme executive power derives from
...a mandate from the masses,not from some farcical aquatic ceremony."""
tokens = nltk.word_tokenize(raw)

#词干提取器
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
print([porter.stem(t) for t in tokens])
print([lancaster.stem(t) for t in tokens])

#词形归并器
wnl = nltk.WordNetLemmatizer()
print(wnl.lemmatize(t) for t in tokens)

