import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_pickle("2022-07_tweet_data.pkl")

x = input("enter the search term ")

mask = df['tweet_text'].str.contains(x)

filter_df = df[mask]

count_df = filter_df.groupby("date")["date"].transform("count")

filter_df.to_pickle("2022-07_" + str(x)+".pkl")

count_df.to_pickle("2022-07_count" + str(x)+".pkl")
