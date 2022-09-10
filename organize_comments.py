# -*- coding =utf-8 -*-

import re
import json
import csv
import os
import pandas as pd


# 用户id 用户名 评论 评论回复数 点赞数
def orgnize():
    c = open("comments.csv", "w+", encoding="utf-8", newline="")
    c1 = csv.writer(c)
    files = os.listdir("./comments")
    # print(len(files))
    for k in range(len(files)):
        file_name = "./comments/comment" + str(k) + ".json"
        file = open(file_name, "r+", encoding="utf-8")
        s = file.read()
        begin = re.findall("jQuery[\d_]+[(]", s)
        begin_len = len(begin[0])
        a = json.loads(s[begin_len:-1])
        # print(a)
        # re1 = "(?<=message\":\")[^\"]*"
        # re2 = "(?<=replies\":)[^\"top\"]"
        # r = re.compile(re2)
        # print(re.findall(r,s))

        replies = a["data"]["replies"]
        if replies:
            for i in range(0, len(replies)):
                replies[i]["content"]["message"] = replies[i]["content"]["message"].replace("\n", '')
                # print(replies[i]["reply_control"]["sub_reply_entry_text"])
                if replies[i]["reply_control"].setdefault("sub_reply_entry_text"):
                    a = re.findall("\d+", replies[i]["reply_control"]["sub_reply_entry_text"])
                    l = [replies[i]["member"]["mid"], replies[i]["member"]["uname"], replies[i]["content"]["message"],
                         a[0], replies[i]["like"]]
                else:
                    l = [replies[i]["member"]["mid"], replies[i]["member"]["uname"], replies[i]["content"]["message"],
                         0, replies[i]["like"]]
                # if (replies[i]["replies"]):
                #     for j in range(0, len(replies[i]["replies"])):
                #         l.append(replies[i]["replies"][j]["member"]["mid"])
                #         l.append(replies[i]["replies"][j]["member"]["uname"])
                #         replies[i]["replies"][j]["content"]["message"]=replies[i]["replies"][j]["content"]["message"].replace("\n",'')
                #         l.append(replies[i]["replies"][j]["content"]["message"])
                # print(l)
                c1.writerow(l)
                l = []
    c.close()
    frame = pd.read_csv('./comments.csv')
    # print(frame.to_string())
    data = frame.drop_duplicates(subset=None, keep='first')
    data.to_csv('./comments.csv', encoding='utf8', header=None, index=None)
