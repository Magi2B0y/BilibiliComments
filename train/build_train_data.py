# -*- coding=utf-8 -*-
# coding:unicode_escape
import codecs
import jieba

stopwords = [w.strip() for w in codecs.open("stopwords_comment.txt", "r+", "utf-8").readlines()]


# Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
def extract_corpus(data_file_path, label):
    corpus_all = []
    list = []
    with open(data_file_path, 'r+', encoding="utf8") as f:
        for line in f:
            list.append(line.replace('\n', ''))
    for corpus in list:
        corpus = ' '.join(w for w in jieba.cut(corpus) if w not in stopwords)
        corpus = "__label__" + label + " " + corpus
        corpus_all.append(corpus)
    return corpus_all


def writeData(sentences, fileName):
    print("writing data to fasttext format...")
    out = open(fileName, 'w', encoding='utf-8')
    for sentence in corpus_all:
        out.write(sentence + '\n')
    print("done")


label = 'negative'
data_file_path = "../comments/CMY_neg.txt"
corpus_neg = extract_corpus(data_file_path, label)

label = 'positive'
data_file_path = "../comments/CMY_pos.txt"
corpus_pos = extract_corpus(data_file_path, label)

label = 'neutral'
data_file_path = "../comments/CMY_neu.txt"
corpus_neu = extract_corpus(data_file_path, label)

label = 'suggestion'
data_file_path = "../comments/CMY_sug.txt"
corpus_sug = extract_corpus(data_file_path, label)

label = 'question'
data_file_path = "../comments/CMY_que.txt"
corpus_que = extract_corpus(data_file_path, label)

corpus_all = corpus_neg + corpus_pos + corpus_neu + corpus_sug + corpus_que

writeData(corpus_all, r'../temp/CMY_comments.txt')
