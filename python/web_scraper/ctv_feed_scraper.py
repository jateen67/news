import feedparser
from time import sleep
from bs4 import BeautifulSoup
import requests
import re


def ctv_scrape():
    # BEGINNING OF FEED SCRAPER

    feed = feedparser.parse(
        "https://www.ctvnews.ca/rss/ctvnews-ca-world-public-rss-1.822289"
    )

    feed_list = []

    if feed.bozo == 0:
        for entry in feed.entries:
            article = {
                "title": entry.title,
                "description": entry.description,
                "published": entry.published,
                "link": entry.link,
            }

            feed_list.append(article)
    else:
        print("Failed to parse the feed :(")

    # END OF FEED SCRAPER

    # BEGINNING OF ARTICLE SCRAPER

    article_text_list = []

    for feed in feed_list:
        response = requests.get(feed["link"])

        soup = BeautifulSoup(response.content, "html.parser")

        c_text_div = soup.find("div", class_="c-text")

        if c_text_div:
            related_stories_div = c_text_div.find("div", class_="c-relatedStories")

            if related_stories_div:
                related_stories_div.extract()

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

    # END OF ARTICLE SCAPER

    # BEGINNING OF ARTICLE CLEANER

    with_space = re.compile(r"(<br\s*/><br\s*/>)|(\-)|(\/)")
    no_space = re.compile(r"[.;:!\'?,\"()\[\]]")

    article_text_list_cleaned = []
    for article in article_text_list:
        article_text_list_cleaned.append(article["text"])

    for i in range(len(article_text_list_cleaned)):
        article_text_list_cleaned[i] = no_space.sub(
            "", article_text_list_cleaned[i].lower()
        )
        article_text_list_cleaned[i] = with_space.sub(" ", article_text_list_cleaned[i])
        article_text_list_cleaned[i] = article_text_list_cleaned[i].replace(
            "\r\n\t", " "
        )
        article_text_list_cleaned[i] = article_text_list_cleaned[i].replace("\n", " ")

    articles = []
    for article_text in article_text_list_cleaned:
        articles.append({"text": article_text})

    # END OF ARTICLE CLEANER

    # BEGINNING OF ARTICLE + FEED MERGER

    merged_array = []
    for obj1, obj2 in zip(feed_list, articles):
        merged_obj = {**obj1, **obj2}
        merged_array.append(merged_obj)

    # END OF ARTICLE + FEED MERGER
    return merged_array
