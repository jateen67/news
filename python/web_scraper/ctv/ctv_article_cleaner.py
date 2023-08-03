import json
import re

with open("../../data/ctv_article_content_raw.json") as json_data:
    article_list = json.load(json_data)

with_space = re.compile(r"(<br\s*/><br\s*/>)|(\-)|(\/)")
no_space = re.compile(r"[.;:!\'?,\"()\[\]]")

article_text_list = []
for article in article_list:
    article_text_list.append(article["text"])

for i in range(len(article_text_list)):
    article_text_list[i] = no_space.sub("", article_text_list[i].lower())
    article_text_list[i] = with_space.sub(" ", article_text_list[i])
    article_text_list[i] = article_text_list[i].replace("\r\n\t", " ")

articles = []
for article_text in article_text_list:
    articles.append({"text": article_text})

with open("../../data/ctv_article_content_cleaned.json", "w") as outfile:
    json.dump(articles, outfile, indent=4)
