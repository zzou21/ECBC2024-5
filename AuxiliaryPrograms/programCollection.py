# This file contains auxiliary programs that could help in many different stages of data cleaning and analysis. See each function's comment for descriptions of their usages.
import json, os, re

# This function combines multiple JSON files together.
def combineOCRedPerPageJSON(listOfJsonFiles):
    finalDictionary = {}
    pageCounter = 1
    for oneJson in listOfJsonFiles:
        with open(oneJson, "r", encoding="utf-8") as oneJsonContent:
            oneJsonDictionary = json.load(oneJsonContent)
            for pageNum, content in oneJsonDictionary.items():
                if content != "":
                    content = content.replace("\n", " ")
                    finalDictionary[pageCounter] = content
                    pageCounter += 1
    
    with open ("/Users/Jerry/Desktop/BassConnections2024-5/ECBC2024-5/OCRJSON/allFourVCLCombinedPerPage.json", "w", encoding="utf-8") as destinationJson:
        json.dump(finalDictionary, destinationJson, indent=4)
                

# This function cleans JSON files to avoid encoding errors.
def jsonCleaner(jsonPath):
    with open(jsonPath, "r", encoding="utf-8") as jsonContent:
        jsonDict = json.load(jsonContent)
    
    def cleanString(string):
        return re.sub(r'[\x00-\x1F\x7F]', '', string)
    def removeTab(string):
        return string.replace("\t", " ")

    for key, entry in jsonDict.items():
        if isinstance(entry, dict):  # If the value is a dictionary, clean nested text
            for sub_key in entry:
                if isinstance(entry[sub_key], str):  
                    entry[sub_key] = cleanString(entry[sub_key])
                    entry[sub_key] = removeTab(entry[sub_key])
        elif isinstance(entry, str):  # If the value is a string
            jsonDict[key] = cleanString(entry)
    with open(jsonPath, "w", encoding="utf-8") as jsonStorage:
        json.dump(jsonDict, jsonStorage, indent=8)

#Clean out new lines in a folder of TXT files
def cleanNewLines(folderPath):
    storageDict = {}
    for txtFile in os.listdir(folderPath):
        if txtFile.endswith(".txt"):
            filepath = os.path.join(folderPath, txtFile)

            with open(filepath, "r") as txtContent:
                content = txtContent.read()
                content = " ".join(content.splitlines())
                storageDict[txtFile] = content
    with open("/Users/Jerry/Desktop/BassConnections2024-5/ECBC2024-5/AuxiliaryPrograms/tempJSON2.json", "w", encoding="utf-8") as jsonFile:
        json.dump(storageDict, jsonFile, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    folderPath = "/Users/Jerry/Desktop/Superscript Corrected OCR Results"
    # cleanNewLines(folderPath)
    listOfJsonPathsToCombine = [
        "/Users/Jerry/Desktop/BassConnections2024-5/ECBC2024-5/OCRJSON/Vol1StoreOCRPerPage.json",
        "/Users/Jerry/Desktop/BassConnections2024-5/ECBC2024-5/OCRJSON/Vol2StoreOCRPerPage.json",
        "/Users/Jerry/Desktop/BassConnections2024-5/ECBC2024-5/OCRJSON/Vol3StoreOCRPerPage.json",
        "/Users/Jerry/Desktop/BassConnections2024-5/ECBC2024-5/OCRJSON/Vol4StoreOCRPerPage.json"
    ]
    # combineOCRedPerPageJSON(listOfJsonPathsToCombine)

    jsonCleanerPath = "/Users/Jerry/Desktop/BassConnections2024-5/ECBC2024-5/FomattedExamples.json"
    jsonCleaner(jsonCleanerPath)