import json
import feedparser

feed = feedparser.parse("https://globalnews.ca/world/feed/")

article_list = []

if feed.bozo == 0:
    for entry in feed.entries:
        description = entry.description

        article = {
            "title": entry.title,
            "description": description,
            "published": entry.published,
            "link": entry.link,
        }

        article_list.append(article)
else:
    print("Failed to parse the feed :(")

with open("../data/global_feed.json", "w") as outfile:
    json.dump(article_list, outfile, indent=4)
