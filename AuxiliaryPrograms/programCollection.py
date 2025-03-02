import json, os

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
    cleanNewLines(folderPath)