import requests, json
# This file runs automated Google search on listed names or terms and store the top results (including title, meta description, and links) in a JSON for future reference.
# Each time when running the search, do not forget to update the API and CSE keys and IDs under the main Python block.
class googleSearchMachine:
    def __init__ (self, queryList, apiKeyString, cseIDString, numResultsInt, storingSearchResultJson):
        self.queryList = queryList
        self.apiKeyString = apiKeyString
        self.cseIDString = cseIDString
        self.numResultsInt = numResultsInt
        self.storingSearchResultJson = storingSearchResultJson
        self.storeAllSearchResultsDict = None #data format: {"searchName": {"Result 1": {"title": "", "meta_description": "", "resultLink": ""}, "searchName":{...}}}
    
    def processEachSearchName(self):
        allSearchResultStorage = {}
        for nameToSearch in self.queryList:
            allSearchResultStorage[nameToSearch] = {}
            print(f"\n\n\n\nCurrently searching: {nameToSearch}")
            oneNameSearchResult = self.googleSearch(nameToSearch)
            # print(f"return value from googleSearch: {oneNameSearchResult}")
            for numberOfSearchResult, oneItem in enumerate(oneNameSearchResult, start = 1):
                # print(f"One value in the oneNameSearchResult: {oneItem}")
                # titleValue = oneItem.get("title", "No title")
                # metaDescriptionValue = oneItem.get("meta_description", "No meta description")
                # # print(f"Title of one search: {titleValue}")
                # print(f"Meta description of one search: {metaDescriptionValue}\n\n\n")
                subDictionaryKeyForEachSearchResult = "Result " + str(numberOfSearchResult)
                allSearchResultStorage[nameToSearch][subDictionaryKeyForEachSearchResult] = {}
                for typeOfInfo, info in oneItem.items():
                    allSearchResultStorage[nameToSearch][subDictionaryKeyForEachSearchResult][typeOfInfo] = info
        
        # print(f"Final test: {allSearchResultStorage}")
        for name, result in allSearchResultStorage.items():
            print(f"Search name: {name}")
            for resultCounter, resultContent in result.items():
                print(resultCounter)
                for resultType, resultWords in resultContent.items():
                    print(f" {resultType}: {resultWords}")

        self.storeAllSearchResultsDict = allSearchResultStorage

    def googleSearch(self, query):
        url = f"https://www.googleapis.com/customsearch/v1"
        params = {
            "q": query,
            "key": self.apiKeyString,
            "cx": self.cseIDString,
            "num": self.numResultsInt
        }
        response = requests.get(url, params=params)
        searchResults = response.json() # type dictionary
        metaDescriptionResults = []
        print(f"These are the search result outputs: {searchResults}")
        if "items" in searchResults:
            for item in searchResults['items']:
                title = item.get("title", "No title")
                snippet = item.get("snippet", "No snippet")
                resultLink = item.get("link", "No link")

                metaDescriptionResults.append({"title": title, "meta_description": snippet, "resultLink": resultLink})
        
        print(f"this is the full meta description result: {metaDescriptionResults}")
        return metaDescriptionResults
    
    def addAllSearchResultsToJson(self):
        with open(self.storingSearchResultJson, "w") as jsonStorage:
            json.dump(self.storeAllSearchResultsDict, jsonStorage, indent = 4)
        
    def operations(self):
        self.processEachSearchName()
        self.addAllSearchResultsToJson()

if __name__ == "__main__":
    API_KEY = "AIzaSyBuNkIdtQC-y-1bNxoB4_7RV9SpwgIvUkU" # personal!!! This is for Google Python API access key
    CSE_ID = "704c915507a564a0c" #personal!!! CSE: Custom search engine
    searchNames = ["Albert Einstein", "Rodger Federer"] #store the names that need to be searched.
    numOfSearchResultsToStore = 10
    jsonSearchResultStorage = "/Users/Jerry/Desktop/BassConnections2024-5/ECBC2024-5/MassGoogleSearchTools/vol3Namepg80-90SearchResultStorage.json" # use when using personal computer
    # jsonSearchResultStorage = "C:\Users\zz341\Desktop\ECBC2024-5\MassGoogleSearchTools\vol3Namepg80-90SearchResultStorage.json" # use when using XR lab device 

    googleSearchTool = googleSearchMachine(searchNames, API_KEY, CSE_ID, numOfSearchResultsToStore, jsonSearchResultStorage)
    googleSearchTool.operations()