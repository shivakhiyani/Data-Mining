# -*- coding: utf-8 -*-
"""HW6.4 Knowledge graph.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YfGQfhxsxJlCHNSBnjyyxLLVkSlaHtNE
"""

# !curl -O https://www.ccs.neu.edu/home/vip/teach/DMcourse/6_graph_analysis/HW6/graph.txt
# !curl -O https://www.ccs.neu.edu/home/vip/teach/DMcourse/6_graph_analysis/HW6/annotations.txt
!curl -O http://www.ccs.neu.edu/home/vip/teach/DMcourse/6_graph_analysis/HW6/word2vec_train_dev.dat

import nltk
nltk.download('punkt')

import gensim
from nltk import word_tokenize
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict


# Function to get the cosine similarity between a relation and query
# Note: Be sure to prepend the relation with ns:
word2vec_model = gensim.models.Word2Vec.load('word2vec_train_dev.dat')
def get_rel_score_word2vecbase(rel, query):
    if rel not in word2vec_model.wv:
        return 0.0
    words = word_tokenize(query.lower())
    w_embs = []
    for w in words:
        if w in word2vec_model.wv:
            w_embs.append(word2vec_model.wv[w])
    return np.mean(cosine_similarity(w_embs, [word2vec_model.wv[rel]]))


# Function to load the graph from file
def load_graph():
    # Preparing the graph
    graph = defaultdict(list)
    for line in open('graph.txt'):
        line = eval(line[:-1])
        graph[line[0]].append([line[1], line[2]])
    return graph


# Function to load the queries from file
# Preparing the queries
def load_queries():
    queries = []
    for line in open('annotations.txt'):
        line = eval(line[:-1])
        queries.append(line)
    return queries

class depth_first:
    def __init__(self):
        self.visited = [] 
        self.similar= set()  
    def dfs(self, graph,ver,query):
        if ver not in self.visited:
            self.dfs_visit(graph, ver,query)
        return self.similar
    
    def dfs_visit(self, graph, vertex,query):
        for i in g[vertex]:
            k=i[1]
            nb=i[0]
            rel=['ns:'+nb for nb in i]
            if get_rel_score_word2vecbase(rel[0], query)>0.30:
                if i not in self.visited:
                  self.visited.append(i)              
                  self.dfs_visit(g, k,query)
                self.similar.add(k)

precision=0
recall=0
b=0
for edge in load_queries():
  topic_code = edge[2]
  d= depth_first()
  g=load_graph()
  query = edge[1]
  predicted=d.dfs(g,topic_code,query)
  total = len(predicted)
  true=set()
  for k in range(len(edge[5])):
    truth= edge[5][k]['AnswerArgument']
    true.add(truth)
  
  truepositives=true.intersection(predicted)
  if total!=0:
    precision+=(len(truepositives)/total)
    recall+=(len(truepositives)/len(true))
    b+=1

final_precision=(precision/b)
final_recall=(recall/b)
f1score=2*(final_precision*final_recall/(final_precision+final_recall))
print(final_precision,final_recall,f1score)

# print(g['m.059g4'])
# # m.06yxd
# # m.0fv_t
# # m.02hcv8
# # m.0mmyl
# # m.09c7w0
# # m.03q1lwl
# # m.01lp8
# # m.03_gx
# for i in g['m.059g4']:
#   k=i
#   print(k)

# d.dfs_visit(g, topic_code)

# for i in g['m.09c7w0']:
#   nb=i[0]
#   k=['ns:'+nb for nb in i]
# print(k)

# q=load_queries()
# an=[]
# answer = []
# positives=defaultdict(list)
# k=0
# for i in q:
#   for k in range(len(i[5])):
#     query= i[5][k]['AnswerArgument']
#     answer.append(query)

# print(positives)

# print(k)
# print(query)
# get_rel_score_word2vecbase(k[0], query)