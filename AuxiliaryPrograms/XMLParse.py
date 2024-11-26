import xml.etree.ElementTree as ET, untangle

class xmlParse:
    def __init__(self, xmlFilePath, contentStoragePath):
        self.xmlFilePath = xmlFilePath
        self.contentStoragePath = contentStoragePath

    # Method 1: using '.findall()'
    def traverseXMLDataTree(self, xmlTagsToSearchList):
        tree = ET.parse(self.xmlFilePath)
        root = tree.getroot()
        storeContentDictionary = {xmlTagToSearch: [] for xmlTagToSearch in xmlTagsToSearchList}
        for xmlTagToSearch in xmlTagsToSearchList:
            for element in root.findall(f".//{xmlTagToSearch}"):
                print(element.text)
                storeContentDictionary[xmlTagToSearch].append(element.text)
        print(storeContentDictionary)


    # Method 2: recursive tree traversal
    def recursiveTreeTraversal(self, element, xmlTag, tagHolderList, treeLevel = 0):
        xmlTagContent = element.text.strip() if element.text and element.text.strip() else "No content"
        print(f"{' ' * treeLevel}{element.tag}: {element.attrib} -- {xmlTagContent}")
        if element.tag == xmlTag:
            tagHolderList.append(element.text)
        for child in element:
            self.recursiveTreeTraversal(child, xmlTag, tagHolderList, treeLevel + 1)

    def recursiveTraverseRoot(self, xmlTagsToSearchList):
        tree = ET.parse(self.xmlFilePath)
        root = tree.getroot()
        storeContentDictionary = {xmlTag: [] for xmlTag in xmlTagsToSearchList}
        for xmlTag in xmlTagsToSearchList:
            temporaryXmlTagHolderList = []
            self.recursiveTreeTraversal(root, xmlTag, temporaryXmlTagHolderList)
            storeContentDictionary[xmlTag] = temporaryXmlTagHolderList
        print(storeContentDictionary)


if __name__ == "__main__":
    xmlFilePath = "/Users/Jerry/Desktop/BassConnections2024-5/ECBC2024-5/AuxiliaryPrograms/testTraversal(A00002.P4).xml"
    contentStoragePath = ""
    xmlTagsToSearchList = ["NOTE", "PUBLISHER"]
    xmlTraverseMachine = xmlParse(xmlFilePath, contentStoragePath)
    # xmlTraverseMachine.traverseXMLDataTree(xmlTagsToSearchList)
    # xmlTraverseMachine.recursiveTraverseRoot(xmlTagsToSearchList)