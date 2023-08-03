import json
import feedparser

feed = feedparser.parse(
    "https://www.ctvnews.ca/rss/ctvnews-ca-world-public-rss-1.822289"
)

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

with open("../data/ctv_feed.json", "w") as outfile:
    json.dump(article_list, outfile, indent=4)
