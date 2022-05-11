# -*- coding =utf-8 -*-
import fasttext
import jieba
import codecs  # codecs专门用作编码转换
# from gensim.models.wrappers import FastText
import numpy as np

stopwords = [w.strip() for w in codecs.open("stopwords_comment.txt", "r", "utf-8").readlines()]
classifier = fasttext.train_supervised('train_data.txt', label_prefix="__label__", min_count=1)

texts = "这衣服质"
print("评论：%s" % texts)
texts = texts.replace('\n', ' ').replace('\r', '')
texts = ' '.join(w for w in jieba.cut(texts) if w not in stopwords)
texts = [texts]
label_test = classifier.predict(texts)

print('result:', str(label_test))

# model=fasttext.skipgram('train_data.txt','vector')
# vector_m=np.array(model['电脑 十分满意'])
# https://www.bilibili.com/video/BV1JE411e7Ye?from=search&seid=17856862625331099998&spm_id_from=333.337.0.0
