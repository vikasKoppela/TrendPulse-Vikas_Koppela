import pandas as pd
from pathlib import Path

directory = Path("data")
directory.mkdir(exist_ok=True)
file_path = directory/"trends_20260823.json"
file_path2 = directory/"trends_clean.csv"

#Loading json file in to a pandas dataframe
df = pd.read_json(file_path,convert_dates=["collected_at"])
print(f"Loaded {len(df)} stories from {file_path}")

#Removing rows where post_id column is duplicated
df = df.drop_duplicates(subset=["post_id"])
print("After removing duplicates:",len(df))

#Removing null value rows from post_id, title, score columns
df = df.dropna(subset=["post_id","title","score"])
print("After removing nulls:",len(df))

#Assigning score values greater than 5.
df = df[df["score"]>=5]
print("After removing low scores:", len(df))

# Stripping the title column values
df["title"] = df["title"].str.strip()

#Saving the dataframe in to csv file
df.to_csv(file_path2, index=False)

print(f"Saved {len(df)} rows to {file_path2}")

#Printing category summary
print(df["category"].value_counts())