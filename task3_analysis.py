import pandas as pd
import numpy as np
from pathlib import Path

directory = Path("data")
directory.mkdir(exist_ok=True)
processed_file_path = directory/"trends_clean.csv"
analysed_file = directory/"trends_analysed.csv"

df = pd.read_csv(processed_file_path)

print("Loaded data:",df.shape)

print("\nFirst 5 rowsa:\n",df.head(5))

print("\nAverage score:",df["score"].mean().round(2),"\nAverage number of comments:",df["num_comments"].mean().round(2))

score = np.array(df["score"].to_list())
print("\n--- NumPy Stats ---")
print("Mean score:", score.mean())
print("Median score:", np.median(score))
print("standard deviation:", score.std())
print("Max score:", score.max())
print("Min score:", score.min())

category = np.array(df["category"].to_list())

unique_cat,counts=np.unique(category, return_counts=True)

max_idx = np.argmax(counts)
print(f"\nMost stories in: {unique_cat[max_idx]} ({counts[max_idx]} stories)\n")

comments = np.array(df["num_comments"])
titles = np.array(df["title"])

idx_comm = np.argmax(comments)

print(f"Most commented story: {titles[idx_comm]}  — {comments[idx_comm]} comments\n")

df["engagement"] = df["num_comments"]/(df["score"]+1)

df["is_popular"] = df["score"]>score.mean()

df.to_csv(analysed_file, index=False)

print("Saved to",analysed_file)
