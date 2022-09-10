#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bilibili_comment
import identify
import os
from flask import Flask,redirect, request,url_for,render_template,jsonify


app = Flask(__name__, static_folder=os.path.abspath("./templates/"), static_url_path="")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/show',methods=['POST'])
def show():
    url = request.form["Ourl"]
    bilibili_comment.main(url)
    # 引入 bilibili_comment.py 并用获取url对应的评论产生./comments.csv
    result = identify.main()
    # 循环预测list中每条评论的类别并产生如下形式的字典
    # {"positive":[],"negative":[],"neutral":[],"suggestion":[],"question":[]}
    #!使用ajax处理请求直接返回 result
    return jsonify(result)

if __name__ == '__main__':
   app.run(debug=True)
