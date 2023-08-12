import json

import ctv_feed_scraper
import global_feed_scraper

array1 = ctv_feed_scraper.ctv_scrape()  # Your first array with JSON objects
array2 = global_feed_scraper.global_scrape()  # Your second array with JSON objects

merged_array = array1 + array2

with open("../data/news_done.json", "w") as outfile:
    json.dump(merged_array, outfile, indent=4)
