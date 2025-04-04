# This file uses spaCy to analyze names and proper nouns from VCL documents

import spacy, json
 
# This function cleans the JSON containing Section 1 of cleaned OCR VCL documents to find names: name distribution, unique names, etc.
def processCleanedNERNames(VCLJson, namesToIgnore):
    with open(VCLJson, "r", encoding="utf-8") as VCLJsonProcess:
        VCLContentDict = json.load(VCLJsonProcess)
    dateName = {}
    for date, textDictList in VCLContentDict.items():
        if date not in dateName:
            dateName[date] = []
        for textPageDict in textDictList:
            for textEntitiesLabel, contentPageLabel in textPageDict.items():
                if textEntitiesLabel == "entities":
                    for NERResultDict in contentPageLabel:
                        for NERResultLabel, NERResultContent in NERResultDict.items():
                            if NERResultLabel == "label" and NERResultDict[NERResultLabel] == "PERSON":
                                # print(NERResultDict["entity"])
                                if NERResultDict["entity"] not in namesToIgnore:
                                    dateName[date].append(NERResultDict["entity"])
    uniqueNamesAccumulator = 0
    for k,v in dateName.items():
        uniqueNamesAccumulator += len(set(v))
    totalNames = set()
    for k, v in dateName.items():
        for name in v:
            totalNames.add(name)
    
    dictAsList = list(dateName.items())
    dictAsListSorted = sorted(dictAsList, key=lambda x: int(x[0][-4:]))
    # print(dictAsListSorted)
    for tuple in dictAsListSorted:
        print(tuple[0])
        print(set(tuple[1]))
        print("\n")

if __name__ == "__main__":
    cleanedVCLJson = "/Users/Jerry/Desktop/BassConnections2024-5/ECBC2024-5/NERCode/cleanedSection1NERNames.json"

    namesToIgnore = ["Lordships", "John Carter Brown Library", "the John Carter Brown Library", "The John Carter Brown Library", "John Carter Brown", "Roll A. 42", "Library", "Statutes", "LIBRARY", "Vol", "Debts", "Colony", "Plantations", "li", "Deputie", "VOLUME I.", "Virginia Miscellaneous Records", "Certain Orders", "Ibid", "Wrote", "Honourable Earle", "Miscellaneous Records"]
    processCleanedNERNames(cleanedVCLJson, namesToIgnore)