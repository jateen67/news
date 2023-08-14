import csv
import ctv_feed_scraper
import global_feed_scraper


ctv_news = ctv_feed_scraper.ctv_scrape()
global_news = global_feed_scraper.global_scrape()

merged_news = ctv_news + global_news
csv_rows = []

for news in merged_news:
    row = [
        news["title"],
        news["description"],
        news["published"],
        news["link"],
        news["text"],
    ]
    csv_rows.append(row)

with open("../data/news.csv", "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["title", "description", "published", "link", "text"])
    csv_writer.writerows(csv_rows)
