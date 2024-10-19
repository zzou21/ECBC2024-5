# This program cleans the names between pg 80-90 on Records of the Virginia Company of London, Vol III. This is "A complete List in Alphabetical Order of the 'Adventurers to Virginia,' with the Several Amounts of Their Holding."

# Task for the weekend of Oct 19: write a function that automatically searches up names in Google?
import json, re

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
        cleanedNameList = []
        for item in pagesCombinedListOriginalContent[:2]:
            splitAtNewLine = item.split("\n")

            for name in splitAtNewLine: # This function calls the people who have been separated using new lines are now reunited.
                cleaningRegexNewSingleNames = re.sub(r"[^a-zA-Z\s*']", "", name)
                cleaningSingleName = cleaningRegexNewSingleNames.strip()
                replaceNameTitle = {"S*": "Sir", "S'": "Sir", "St": "Saint ", "S ": "Sir ", "' ": "", "'": ""}
                for toBeReplaced, replacement in replaceNameTitle.items():
                    if cleaningSingleName.startswith(toBeReplaced):
                        cleaningSingleName = cleaningSingleName.replace(toBeReplaced, replacement)
                if cleaningSingleName:
                    filterKeywords = ["RECORDS OF THE VIRGINIA", "Adventurers to Virginia"]
                    if all(keyword not in cleaningSingleName for keyword in filterKeywords):
                        cleanedNameList.append(cleaningSingleName)
        self.storeCleanedTextNames = cleanedNameList
        print(cleanedNameList)

    def operations(self):
        self.openJson()
        self.cleanOCRText()

if __name__ == "__main__":
    # vol3OCRedJsonPath = "/Users/Jerry/Desktop/BassConnections2024-5/ECBC2024-5/OCRJSON/Vol3StoreOCRPerPage.json" #Use when using personal computer
    vol3OCRedJsonPath = "C:/Users/zz341/Desktop/ECBC2024-5/OCRJSON/Vol3StoreOCRPerPage.json" #Use when suign XR lab computer
    jsonOCRPageRange = (106, 116) # This is the page number in JSON that records the relevant pages (pg 80-90).
    nameListProcessingMachine = processVol3NameList(vol3OCRedJsonPath, jsonOCRPageRange)
    nameListProcessingMachine.operations()