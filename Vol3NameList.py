# This program cleans the names between pg 80-90 on Records of the Virginia Company of London, Vol III. This is "A complete List in Alphabetical Order of the 'Adventurers to Virginia,' with the Several Amounts of Their Holding."

# Task for the weekend of Oct 19: write a function that automatically searches up names in Google?
import json

class processVol3NameList:
    def __init__(self, vol3OCRedJsonPath, jsonOCRPageRange):
        self.vol3OCRedJsonPath = vol3OCRedJsonPath
        self.jsonOCRPageRange =jsonOCRPageRange
        self.jsonOriginalContentStorage = None
        self.storeCleanedTextNames = []
    
    def openJson(self):
        with open(self.vol3OCRedJsonPath, "r") as jsonContent:
            self.jsonOriginalContentStorage = json.load(jsonContent)
    
    def cleanOCRText(self):
        # print(self.jsonOriginalContentStorage)
        # print((self.jsonOCRPageRange[0], self.jsonOCRPageRange[1] + 1))
        pagesCombinedListOriginalContent = [value for key, value in self.jsonOriginalContentStorage.items() if int(key) in range(self.jsonOCRPageRange[0], self.jsonOCRPageRange[1] + 1)]
        for item in pagesCombinedListOriginalContent:
            print(item)
    
    def operations(self):
        self.openJson()
        self.cleanOCRText()

if __name__ == "__main__":
    vol3OCRedJsonPath = "/Users/Jerry/Desktop/BassConnections2024-5/ECBC2024-5/OCRJSON/Vol3StoreOCRPerPage.json"
    jsonOCRPageRange = (106, 116) # This is the page number in JSON that records the relevant pages (pg 80-90).
    nameListProcessingMachine = processVol3NameList(vol3OCRedJsonPath, jsonOCRPageRange)
    nameListProcessingMachine.operations()