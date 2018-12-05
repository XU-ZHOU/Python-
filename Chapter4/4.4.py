#-*-coding:utf-8 -*-
'''
4.4 函数：结构化编程的基础
import re
def get_text(file):
    text = open(file).read()
    text = re.sub('\s+',' ',text)
    text = re.sub(r'<.*?>',' ',text)
    return text

def insert(trie,key,value):
    if key:
        first,rest = key[0],key[1:]
        if first not in trie:
            trie[first] = {}
        insert(trie[first],rest,value)
    else:
        trie['value'] = value
'''
import re
def raw(file):
    contents = open(file).read()
    contents = re.sub(r'<.*?>',' ',contents)
    contents = re.sub('\s+',' ',contents)
    return contents

#NetworkX
import networkx as nx
import matplotlib
from nltk.corpus import wordnet as wn
def traverse(graph,start,node):
    graph.depth[node.name] = node.shortest_path_distance(start)
    for child in node.hyponyms():
        graph.add_edge(node.name,child.name)
        traverse(graph,start,node)
def hyponym_graph(start):
    G = nx.Graph()
    G.depth = {}
    traverse(G,start,start)
    return G
def graph_draw(graph):
    nx.draw_graphviz(graph,
                     node_size = [16*graph.degree(n) for n in graph],
                     node_color = [graph.depth[n] for n in graph],
                     with_labels = False)
    matplotlib.pyplot.show()
dog = wn.synset('dog.n.01')
graph = hyponym_graph(dog)
graph_draw(graph)
