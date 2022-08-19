# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 09:48:01 2022

@author: aysen
"""
import pandas as pd

df = pd.read_csv("22.20.07_US_videos.csv")

#tag count !! [none]
df["tag_count"] = df["tags"].apply(lambda x: len(x.split("|")) if x != "[none]" else 0)
df.drop(["tag_count"], axis=1)
#title length
df["title_length"] = df["title"].apply(len)
#title uppercase
df["title_uppercase"] = df["title"].str.count((r'[A-Z]'))



df.drop(["video_id","publishedAt","channelId","likes","dislikes","thumbnail_link","ratings_disabled"], axis=1, inplace=True)

df.to_csv("yttrendvids_cleaned_data.csv", index=False)
