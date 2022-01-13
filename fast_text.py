# -*- coding =utf-8 -*-

import os
import codecs#codecs专门用作编码转换
import fasttext
import jieba
# from gensim.models.wrappers import FastText
import numpy as np


stopwords = [w.strip() for w in codecs.open("stopwords_comment.txt","r","utf-8").readlines()]
#Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
def extract_corpus(data_dir, label):
    corpus_all=[]
    filelist=os.listdir(data_dir)
    for one in  filelist:
        corpus=codecs.open(os.path.join(data_dir,one),'r','gbk').read()
        #   os.path.join()函数：连接两个或更多的路径名组件
        # 1.如果各组件名首字母不包含’ / ’，则函数会自动加上
        # 2.如果有一个组件是一个绝对路径，则在它之前的所有组件均会被舍弃
        # 3.如果最后一个组件为空，则生成的路径以一个’ / ’分隔符结尾

        corpus=corpus.replace('\n',' ').replace('\r','')
        #疑惑1
        corpus=' '.join(w for w in jieba.cut(corpus) if w not in stopwords)#Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
        # jieba.cut方法接受两个输入参数: 1) 第一个参数为需要分词的字符串,2)参数用来控制是否采用全模式
        # jieba.cut_for_search方法接受一个参数：需要分词的字符串, 该方法适合用于搜索引擎构建倒排索引的分词，粒度比较细,注意：待分词的字符串可以是gbk字符串、utf - 8字符串或者unicode
        # jieba.cut以及jieba.cut_for_search返回的结构都是一个可迭代的generator，可以使用for循环来获得分词后得到的每一个词语(unicode)，也可以用list(jieba.cut(...))转化为list
        corpus="__label__"+label+" "+corpus
        corpus_all.append(corpus)#append() 方法向列表末尾追加元素。
    return corpus_all

label='negative'
data_dir="neg"
corpus_neg=extract_corpus(data_dir,label)

label='positive'
data_dir="pos"
corpus_pos=extract_corpus(data_dir,label)

corpus_all=corpus_neg+corpus_pos

def writeData(sentences,fileName):
    print("writing data to fasttext format...")
    out=open(fileName,'w',encoding='utf-8')
    for sentence in corpus_all:
        out.write(sentence+'\n')
    print("done")

writeData(corpus_all,r'train_data.txt')

classifier=fasttext.train_supervised('train_data.txt', label_prefix="__label__",min_count=1)

texts="这衣服质"
print("评论：%s"%texts)
texts=texts.replace('\n',' ').replace('\r','')
texts=' '.join(w for w in jieba.cut(texts) if w not in stopwords)
texts=[texts]
label_test=classifier.predict(texts)

print('result:',str(label_test))

# model=fasttext.skipgram('train_data.txt','vector')
# vector_m=np.array(model['电脑 十分满意'])
#https://www.bilibili.com/video/BV1JE411e7Ye?from=search&seid=17856862625331099998&spm_id_from=333.337.0.0



