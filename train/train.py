#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fasttext
model = fasttext.train_supervised(input = "data.train")
model.save_model("model_comment_train.bin")
