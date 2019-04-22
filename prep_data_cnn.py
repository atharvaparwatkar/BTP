from os import listdir
from os.path import isfile, join

DATA_PATH = "/home/atharva/cnn/training"
STORAGE_PATH = "sumdata/train"
TRAIN_DATA_SIZE = 1000
TEST_DATA_SIZE = 100
DATA_SIZE = TRAIN_DATA_SIZE + TEST_DATA_SIZE

files = []
article_files = []
summary_files = []
count = 0

print("Walking...")
for f in listdir(DATA_PATH):
    if count < DATA_SIZE:
        if isfile(join(DATA_PATH, f)):
            if f[-4:] == "sent":
                if isfile(join(DATA_PATH, f[:-4] + "summ")) and f not in article_files:
                    article_files.append(join(DATA_PATH, f))
                    summary_files.append(join(DATA_PATH, f[:-4] + "summ"))
                    count += 1
            elif f[-4:] == "summ":
                if isfile(join(DATA_PATH, f[:-4] + "sent")) and f not in summary_files:
                    summary_files.append(join(DATA_PATH, f))
                    article_files.append(join(DATA_PATH, f[:-4] + "sent"))
                    count += 1
    else:
        break

articles = []
summaries = []

for file in article_files:
    with open(file, "r", encoding="utf-8") as f:
        article = f.readlines()
        filtered_article = []
        for line in article:
            new_line = line.strip()
            if new_line != "" and new_line != "\n":
                filtered_article.append(new_line)
        articles.append(" ".join(filtered_article))
        f.close()

for file in summary_files:
    with open(file, "r", encoding="utf-8") as f:
        summary = f.readlines()
        filtered_summary = []
        for line in summary:
            new_line = line.strip()
            if new_line != "" and new_line != "\n":
                filtered_summary.append(new_line)
        summaries.append(" ".join(filtered_summary))
        f.close()

with open(join(STORAGE_PATH, "train.articles"), "w", encoding="utf-8") as f:
    for article in articles[:TRAIN_DATA_SIZE]:
        f.write(article.split("-- ", 1)[-1] + "\n")
    f.close()

with open(join(STORAGE_PATH, "train.summaries"), "w", encoding="utf-8") as f:
    for summary in summaries[:TRAIN_DATA_SIZE]:
        f.write(summary + "\n")
    f.close()

with open(join(STORAGE_PATH, "test.articles"), "w", encoding="utf-8") as f:
    for article in articles[TRAIN_DATA_SIZE:]:
        f.write(article.split("-- ", 1)[-1] + "\n")
    f.close()

with open(join(STORAGE_PATH, "test.summaries"), "w", encoding="utf-8") as f:
    for summary in summaries[TRAIN_DATA_SIZE:]:
        f.write(summary + "\n")
    f.close()
