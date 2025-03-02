import json, os

# This function turns an OCRed text stored in a JSON into a TXT file:

class processOCRTXTJSON:
    def __init__(self, jsonFilePath, txtFilePath):
        self.jsonFilePath = jsonFilePath
        self.txtFilePath = txtFilePath
    
    #This turns one JSON into one combined TXT file:
    def jsonToTXT(self):
        with open(self.txtFilePath, "a") as txtFile:

            with open(self.jsonFilePath, "r", encoding="utf-8") as jsonFile:
                jsonOCRTextDict = json.load(jsonFile)
            for pageNum, pageContent in jsonOCRTextDict.items():
                txtFile.write(pageContent)

    #This turns one JSON into multiple TXT files, one for each key:value pair in JSON:
    def jsonToMultiTXT(self, txtIndividualOutputFolder):
        with open(self.jsonFilePath, "r") as jsonFile:
            jsonOCRTextDict = json.load(jsonFile)
        individualFileNameFormat = "image"
        for imageNum, pageContent in jsonOCRTextDict.items():
            txtOutputFileNameToCreate = individualFileNameFormat + str(imageNum) + ".txt"
            txtOutputFilePathToCreate = os.path.join(txtIndividualOutputFolder, txtOutputFileNameToCreate)
            with open(txtOutputFilePathToCreate, "w") as txtToWrite:
                txtToWrite.write(pageContent)
                print(f"Created file {txtOutputFileNameToCreate}.")
        

    # We do not yet have a TXT to JSON tool, as when converting from JPG to OCR-ed texts, we automatically stored the content in JSON format.
    
if __name__ == "__main__":
    # jsonFilePath = "C:/Users/zz341/Desktop/ECBC2024-5/OCRJSON/Vol3StoreOCRPerPage.json"
    # txtFilePath = "C:/Users/zz341/Desktop/ECBC2024-5/OCRTXT/v3FullOCR.txt"

    jsonFilePath = "/Users/Jerry/Desktop/BassConnections2024-5/ECBC2024-5/OCRJSON/OCR10imageTraining.json"
    txtFilePath = ""
    txtIndividualOutputFolder = "/Users/Jerry/Desktop/BassConnections2024-5/ECBC2024-5/OCRTXT/OCRTrainingIndividualTXT"
    processOCRMachine = processOCRTXTJSON(jsonFilePath, txtFilePath)
    # processOCRMachine.jsonToTXT()
    processOCRMachine.jsonToMultiTXT(txtIndividualOutputFolder)