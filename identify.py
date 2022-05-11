#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fasttext
import csv
import jieba
import codecs  # codecs专门用作编码转换

def main(data_file="./comments.csv"):
    stopwords = [w.strip() for w in codecs.open("./train/stopwords_comment.txt", "r", "utf-8").readlines()]
    classifier = fasttext.train_supervised('./train/train_data.txt', label_prefix="__label__", min_count=1)
    f = open(data_file,"r+",encoding="utf-8")
    fr = csv.reader(f)
    r=[]
    result = {"positive": 0, "negative": 0, "neutral": 0, "suggestion": [], "question": [], "high_praise": [],"more_reply": []}

    for i in fr:
        temp = {}
        temp["name"]=i[1]
        temp["comment"]=i[2]
        # temp["praise_num"] = i[4]
        # temp["reply_num"] = i[3]
        # print(temp)
        r.append(temp)
    # print(r)


    for i in r:
        texts = ' '.join(w for w in jieba.cut(i["comment"]) if w not in stopwords)
        label_test = classifier.predict(texts,k=2)[0]
        # print(label_test)
        if label_test[0]=="__label__positive":
            result["positive"]=result["positive"]+1
        elif label_test[0]=="__label__negative":
            result["negative"]=result["negative"]+1
        else:
            result["neutral"]=result["neutral"]+1

        if "__label__suggestion" in label_test:
            result["suggestion"].append(i)
        if "__label__question" in label_test:
            result["question"].append(i)

    data = csv.reader(open('comments.csv', encoding='utf-8'))

    # for i in data:
    #     print(i)

    reply_sortedlist = sorted(data, key=lambda x: int(x[3]), reverse=True)
    flag1=0
    for i in reply_sortedlist:
        if flag1<10:
            flag1 = flag1+1
            temp={}
            temp["name"]=i[1]
            temp["comment"] = i[2]
            temp["reply_num"]=i[3]
            result["more_reply"].append(temp)
        else:
            break
    open('comments.csv', encoding='utf-8').close()

    data = csv.reader(open('comments.csv', encoding='utf-8'))
    praise_sortedlist = sorted(data, key=lambda x: int(x[4]), reverse=True)
    # print(praise_sortedlist)
    flag2 = 0
    for i in praise_sortedlist:
        if flag2 < 10:
            flag2 = flag2 + 1
            temp = {}
            temp["name"] = i[1]
            temp["comment"] = i[2]
            temp["praise_num"] = i[4]
            result["high_praise"].append(temp)
        else:
            break
    open('comments.csv', encoding='utf-8').close()

    print(result)
    return result
    
if __name__=="__main__":
    main()