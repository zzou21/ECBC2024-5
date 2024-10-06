import json

# This function turns an OCRed text stored in a JSON into a TXT file:

class processOCRTXTJSON:
    def __init__(self, jsonFilePath, txtFilePath):
        self.jsonFilePath = jsonFilePath
        self.txtFilePath = txtFilePath
    
    def jsonToTXT(self):
        with open(self.txtFilePath, "a") as txtFile:

            with open(self.jsonFilePath, "r", encoding="utf-8") as jsonFile:
                jsonOCRTextDict = json.load(jsonFile)
            for pageNum, pageContent in jsonOCRTextDict.items():
                txtFile.write(pageContent)

if __name__ == "__main__":
    # jsonFilePath = "C:/Users/zz341/Desktop/ECBC2024-5/OCRJSON/Vol3StoreOCRPerPage.json"
    # txtFilePath = "C:/Users/zz341/Desktop/ECBC2024-5/OCRTXT/v3FullOCR.txt"

    jsonV4 = "C:/Users/zz341/Desktop/ECBC2024-5/OCRJSON/Vol4StoreOCRPerPage.json"
    txtV4 = "C:/Users/zz341/Desktop/ECBC2024-5/OCRTXT/v4FullOCR.txt"

    jsonV3 = "/Users/Jerry/Desktop/BassConnections2024-5/ECBC2024-5/OCRJSON/Vol3StoreOCRPerPage.json"
    txtV3 = "/Users/Jerry/Desktop/BassConnections2024-5/ECBC2024-5/OCRTXT/v3FullOCR.txt"

    jsonV2 = "/Users/Jerry/Desktop/BassConnections2024-5/ECBC2024-5/OCRJSON/Vol2StoreOCRPerPage.json"
    txtV2 = "/Users/Jerry/Desktop/BassConnections2024-5/ECBC2024-5/OCRTXT/v2FullOCR.txt"
    processOCRMachine = processOCRTXTJSON(jsonV2, txtV2)
    processOCRMachine.jsonToTXT()