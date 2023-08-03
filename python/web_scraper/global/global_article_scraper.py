import json
from time import sleep
from bs4 import BeautifulSoup

import requests

with open("../../data/global_feed.json") as json_data:
    feed_list = json.load(json_data)

article_text_list = []

for feed in feed_list:
    response = requests.get(feed["link"])

    soup = BeautifulSoup(response.content, "html.parser")

    c_text_div = soup.find("article", class_="l-article__text")

    if c_text_div:
        p_tags = c_text_div.find_all("p")
        article = ""

        for p_tag in p_tags:
            article += p_tag.get_text()

        article_text = {"text": article}

    else:
        article_text = {"text": ""}

        article_text_list.append(article_text)

    article_text_list.append(article_text)

    sleep(1)


with open("../../data/global_article_content_raw.json", "w") as outfile:
    json.dump(article_text_list, outfile, indent=4)