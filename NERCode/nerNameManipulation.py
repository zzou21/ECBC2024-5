# This file uses spaCy to analyze names and proper nouns from VCL documents

import spacy, json, csv
from collections import defaultdict, Counter
from datetime import datetime
 
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
    cleanedDictionaryBefore1700Names = {}
    for tuple in dictAsListSorted:
        # print(tuple[0])
        # print(set(tuple[1]))
        # print("\n")
        if int(tuple[0][-4:]) < 1700:
            cleanedDictionaryBefore1700Names[tuple[0]] = tuple[1]
    
    # print(cleanedDictionaryBefore1700Names)
    return cleanedDictionaryBefore1700Names


def findTop20NamesAndOrganizeBySeason(nameDictionary):
    # Step 1: Count names
    name_counter = Counter()
    for names in nameDictionary.values():
        name_counter.update(names)

    # Step 2: Get top 20 names
    top_20_names = name_counter.most_common(20)
    top_20_set = set(name for name, _ in top_20_names)

    # Step 3: Initialize groupings
    year_grouped = defaultdict(lambda: {'Feb-Sept': {}, 'Nov-Jan': {}})
    name_lines = []  # For third output

    # Step 4: Build year groupings and name lines
    for date_str, names in nameDictionary.items():
        try:
            date = datetime.strptime(date_str.strip().title(), "%B %d, %Y")
        except ValueError:
            continue  # Skip invalid date formats

        year = str(date.year)
        month = date.month
        filtered_names = [name for name in names if name in top_20_set]

        if not filtered_names:
            continue

        if 2 <= month <= 9:
            group_label = 'Feb-Sept'
            year_grouped[year][group_label][date_str] = filtered_names
            for name in filtered_names:
                name_lines.append(f"{name}, feb-sept {year}")
        elif month in [1, 11, 12]:
            group_label = 'Nov-Jan'
            target_year = str(date.year - 1) if month == 1 else year
            year_grouped[target_year][group_label][date_str] = filtered_names
            for name in filtered_names:
                name_lines.append(f"{name}, nov-jan {target_year}")

    # # Step 5: Print summaries
    # print("Top 20 Names:")
    # for name, count in top_20_names:
    #     print(f"{name}: {count}")

    # print("\nSample grouped data (first 2 years):")
    # print(json.dumps(dict(list(year_grouped.items())[:2]), indent=2))

    # print("\nSample 'name, season year' lines:")
    # for line in name_lines[:10]:
    #     print(line)

    return year_grouped, top_20_names, name_lines


if __name__ == "__main__":
    cleanedVCLJson = "/Users/Jerry/Desktop/BassConnections2024-5/ECBC2024-5/NERCode/cleanedSection1NERNames.json"

    namesToIgnore = ["Lordships", "John Carter Brown Library", "the John Carter Brown Library", "The John Carter Brown Library", "John Carter Brown", "Roll A. 42", "Library", "Statutes", "LIBRARY", "Vol", "Debts", "Colony", "Plantations", "li", "Deputie", "VOLUME I.", "Virginia Miscellaneous Records", "Certain Orders", "Ibid", "Wrote", "Honourable Earle", "Miscellaneous Records", "Deputy", "Counsell"]
    processedNamesDict = processCleanedNERNames(cleanedVCLJson, namesToIgnore)
    year_grouped, top_20_names, nameLines = findTop20NamesAndOrganizeBySeason(processedNamesDict)
    for name in nameLines:
        print(name)
    
    with open("/Users/Jerry/Desktop/BassConnections2024-5/ECBC2024-5/NERCode/name_group_output.csv", "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["name", "season_year"])  # Header

        for line in nameLines:
            name, season_year = line.split(", ", 1)  # Split only on first comma
            writer.writerow([name, season_year])
