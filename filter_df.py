import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_pickle("2022-07_tweet_data.pkl")

x = input("enter the search term ")

mask = df['tweet_text'].str.contains(x)

filter_df = df[mask]

filter_df.to_pickle("2022-07_" + str(x)+".pkl")
