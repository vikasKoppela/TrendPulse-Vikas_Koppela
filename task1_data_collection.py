import requests
from pathlib import Path
import json
from datetime import datetime

HEADERS = {"User-Agent": "TrendPulse/1.0"}

url_id = "https://hacker-news.firebaseio.com/v0/topstories.json"
session = requests.Session()
response = session.get(
    url_id,
    headers=HEADERS,
    timeout=3
    )
response.raise_for_status()
result = response.json()
Id = result[:500]
print(Id)

def get_story(Id):
    url = f"https://hacker-news.firebaseio.com/v0/item/{Id}.json"
    response2 = session.get(
    url,
    headers=HEADERS,
    timeout=3
    )
    response2.raise_for_status()
    output = response2.json()
    return output

#Creating file name in data path
directory = Path("data")
directory.mkdir(exist_ok=True)
file_path = directory/"trends_20260823.json"

#Categories 
CATEGORIES = {
    "technology": [
        "ai", "software", "tech", "code", "computer",
        "data", "cloud", "api", "gpu", "llm"
    ],
    "worldnews": [
        "war", "government", "country", "president",
        "election", "climate", "attack", "global"
    ],
    "sports": [
        "nfl", "nba", "fifa", "sport", "game",
        "team", "player", "league", "championship"
    ],
    "science": [
        "research", "study", "space", "physics",
        "biology", "discovery", "nasa", "genome"
    ],
    "entertainment": [
        "movie", "film", "music", "netflix",
        "game", "book", "show", "award", "streaming"
    ],
}

summary = []
for id in Id:
    result = get_story(id)
    #Assigning category name
    title = result["title"].lower()
    for category, keywords in CATEGORIES.items():
            if any(keyword in title for keyword in keywords):
                cat = category
    #Appending if the result contains category value
    if cat:
        res = {"post_id":result["id"],"title":result["title"], "category":cat, "score":result["score"], "num_comments":result.get("descendants"), "author":result["by"], "collected_at":datetime.now().isoformat()}
        summary.append(res)

#Writing in to the file
with open(file_path, "w") as f:
        json.dump(summary, f, indent=2)

#Printing number of stories collected.
print(f"Collected {len(summary)} stories. Saved to {file_path}")

#Printing the json output.
#with open(file_path,"r") as fr:
#     print(fr.read())
