# -*- coding =utf-8 -*-
# @time:2022/1/7

import shutil
import pandas as pd

frame=pd.read_csv('comments.csv')
print(frame.to_string())
data = frame.drop_duplicates(subset=None,keep='first')
data.to_csv('comments.csv', encoding='utf8',header=None, index=None)
