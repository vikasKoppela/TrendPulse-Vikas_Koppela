import matplotlib.pyplot as plt
from pathlib import Path 
import pandas as pd

directory = Path("data")
directory.mkdir(exist_ok=True)
analysed_file = directory/"trends_analysed.csv"
directory2 = Path("data/outputs")
directory2.mkdir(exist_ok=True)
chart1_path = directory2/"chart1_top_stories.png"
chart2_path = directory2/"chart2_categories.png"
chart3_path = directory2/"chart3_scatter.png"

df = pd.read_csv(analysed_file)

#Horizontal Bar chart...
def barh_fig(f):
    top_scores = df.nlargest(10, "score")
    title_short = []
    for title in top_scores["title"]:
        if len(title)>50:
            title_short.append(title[:50])
        else:
            title_short.append(title)
    
    f.barh(title_short, top_scores["score"])
    f.set_title("TrendPulse story scores")
    f.set_xlabel("Score")
    f.set_ylabel("Story")
fig1,f1 = plt.subplots(figsize=(12,6))
barh_fig(f1)
fig1.tight_layout()
fig1.savefig(chart1_path)
plt.close(fig1)

#Bar chart....
def bar_fig(fv):
    category_count = df["category"].value_counts()
    colors = plt.cm.tab10(range(len(category_count)))
    fv.bar(category_count.index, category_count.values, color=colors)
    fv.set_title("Stories per Category")
    fv.set_xlabel("Category")
    fv.set_ylabel("No of Sttories")

fig2, f2 = plt.subplots(figsize=(10,4))
bar_fig(f2)
fig2.tight_layout()
fig2.savefig(chart2_path)
plt.close(fig2)

#Scatter plot
def scatter_plot(fs):
    popular_df = df[df["is_popular"] == True]
    non_popular_df = df[df["is_popular"] == False]
    fs.scatter(popular_df["score"], popular_df["num_comments"], color="red", label="Popular")
    fs.scatter(non_popular_df["score"], non_popular_df["num_comments"], color="blue", label="Non-Popular")
    fs.set_title("Score Popularity")
    fs.set_xlabel("Score")
    fs.set_ylabel("Num of Comments")

fig3,f3 = plt.subplots(figsize=(10,4))
scatter_plot(f3)
fig3.tight_layout()
fig3.savefig(chart3_path)
plt.close(fig3)

fig,axes = plt.subplots(1,3,figsize=(20,8))
barh_fig(axes[0])
bar_fig(axes[1])
scatter_plot(axes[2])

fig.suptitle("TrendPulse Dashboard", fontsize=18)

fig.tight_layout()
fig.subplots_adjust(top=0.88)

fig.savefig("data/outputs/dashboard.png", dpi=300)
plt.close(fig)

