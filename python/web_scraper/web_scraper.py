import json

import ctv_feed_scraper
import global_feed_scraper

array1 = ctv_feed_scraper.ctv_scrape()
array2 = global_feed_scraper.global_scrape()

merged_array = array1 + array2

with open("../data/news_done.json", "w") as outfile:
    json.dump(merged_array, outfile, indent=4)
