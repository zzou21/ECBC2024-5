import requests, json
# Each time when running the search, do not forget to update the API and CSE keys and IDs under the main Python block.


# TO DO: Need to finish dump to JSON in processEachSearchName function
class googleSearchMachine:
    def __init__ (self, queryList, apiKeyString, cseIDString, numResultsInt, storingSearchResultJson):
        self.queryList = queryList
        self.apiKeyString = apiKeyString
        self.cseIDString = cseIDString
        self.numResultsInt = numResultsInt
        self.storingSearchResultJson = storingSearchResultJson
        self.storeSearchResults = None
    
    def processEachSearchName(self):
        allSearchResultStorage = {}
        for nameToSearch in self.queryList:
            allSearchResultStorage[nameToSearch] = {}

            print(f"\n\n\n\nCurrently searching: {nameToSearch}")

            oneNameSearchResult = self.googleSearch(nameToSearch)
            print(f"return value from googleSearch: {oneNameSearchResult}")
            for numberOfSearchResult, oneItem in enumerate(oneNameSearchResult, start = 1):
                print(f"One value in the oneNameSearchResult: {oneItem}")
                titleValue = oneItem.get("title", "No title")
                metaDescriptionValue = oneItem.get("meta_description", "No meta description")
                print(f"Title of one search: {titleValue}")
                print(f"Meta description of one search: {metaDescriptionValue}\n\n\n")
                subDictionaryKeyForEachSearchResult = "Result " + str(numberOfSearchResult)
                allSearchResultStorage[nameToSearch][subDictionaryKeyForEachSearchResult] = {}
                for typeOfInfo, info in oneItem.items():
                    allSearchResultStorage[nameToSearch][subDictionaryKeyForEachSearchResult][typeOfInfo] = info
        
        print(f"Final test: {allSearchResultStorage}")
        for name, result in allSearchResultStorage.items():
            print(f"Search name: {name}")
            for resultCounter, resultContent in result.items():
                print(resultCounter)
                for resultType, resultWords in resultContent.items():
                    print(f" {resultType}: {resultWords}")
    # left here, Oct 19, 2024


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
        if "items" in searchResults:
            print("Yes")
            for item in searchResults['items']:
                title = item.get("title", "No title")
                print(f"One title: {title}")
                snippet = item.get("snippet", "No snippet")
                print(f"One metadescription: {snippet}")

                metaDescriptionResults.append({'title': title, 'meta_description': snippet})
        
        print(f"this is the full meta description result: {metaDescriptionResults}")
        return metaDescriptionResults
    
    def operations(self):
        self.processEachSearchName()

if __name__ == "__main__":
    API_KEY = "" # personal!!!
    CSE_ID = "" #personal!!!
    searchNames = ['Albert Einstein'] #store the names that need to be searched.
    numOfSearchResultsToStore = 10
    jsonSearchResultStorage = "C:/Users/zz341/Desktop/ECBC2024-5/MassGoogleSearchTools/vol3Namepg80-90SearchResultStorage.json" # use when using XR lab computer
    # jsonSearchResultStorage = "C:\Users\zz341\Desktop\ECBC2024-5\MassGoogleSearchTools\vol3Namepg80-90SearchResultStorage.json" # use when using personal device 

    googleSearchTool = googleSearchMachine(searchNames, API_KEY, CSE_ID, numOfSearchResultsToStore, jsonSearchResultStorage)
    googleSearchTool.operations()