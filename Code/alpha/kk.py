# coding   : utf-8 
# @Time    : 21/06/14 22:52
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : kk.py
# @Software: PyCharm


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

pd.options.display.float_format = '{:.4f}'.format
df = pd.read_csv("dau.csv")

df_window = df.rolling(window=3, min_periods=1, center=True).mean()

df_diff = df_window.diff(7).dropna()
df_diff

data = df_window.diff(1).dropna()
df_diff1 = df_window.diff(1).dropna()
df_diff3 = df_window.diff(3).dropna()
df_diff7 = df_window.diff(7).dropna()
df_diff15 = df_window.diff(15).dropna()
df_diff30 = df_window.diff(30).dropna()

