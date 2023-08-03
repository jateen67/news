import json

with open("../../data/ctv_feed.json") as file1_data:
    file1_content = json.load(file1_data)

with open("../../data/ctv_article_content_cleaned.json") as file2_data:
    file2_content = json.load(file2_data)

if len(file1_content) != len(file2_content):
    raise ValueError("Both JSON files should have the same number of objects >:(")

merged_data = []
for i in range(len(file1_content)):
    merged_object = {**file1_content[i], **file2_content[i]}
    merged_data.append(merged_object)

with open("../../data/ctv_merged.json", "w") as outfile:
    json.dump(merged_data, outfile, indent=4)
