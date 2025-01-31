'''This file's intention is to test run JSON files that store the different OCRed VCR company records to perform different types of analysis.

Add different functionalities as necessary.'''

import json

def viewPageContent(JSONStoragePath):
    with open(JSONStoragePath, "r", encoding="utf-8") as jsonContent:
        content = json.load(jsonContent)
    return content

if __name__ == "__main__":
    jsonPath = "/Users/Jerry/Desktop/BassConnections2024-5/ECBC2024-5/OCRJSON/testocr.json"
    print(viewPageContent(jsonPath))