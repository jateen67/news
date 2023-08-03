#!/bin/sh

python ../web_scraper/ctv/ctv_feed_scraper.py
python ../web_scraper/ctv/ctv_article_scraper.py
python ../web_scraper/ctv/ctv_article_cleaner.py
python ../web_scraper/ctv/ctv_merger.py

python ../web_scraper/global/global_feed_scraper.py
python ../web_scraper/global/global_article_scraper.py
python ../web_scraper/global/global_article_cleaner.py
python ../web_scraper/global/global_merger.py