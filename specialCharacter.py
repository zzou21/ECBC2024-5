import json, PyPDF2

jsonContent = None
decodeLibrary = {}

with open("/Users/Jerry/Desktop/Bass Connections 2024-5/Code/StoreOCRPerPage.json", "r", encoding="utf-8") as file:
    jsonContent = json.load(file)
    print(jsonContent)

for page, content in jsonContent.items():
    decodeLibrary[page] = content.encode("utf-8").decode("unicode_escape")

# print(decodeLibrary)