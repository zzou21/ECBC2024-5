import pytesseract, os, re, json
from PIL import Image

# This class object takes in a directory of single JPGs, each JPG representing one page from a PDF. Then, the object iterates through each JPG, performs OCR through Tesseract, and store the resulting text (String data type) in a JSON, with the key of the JSON being the page number and value being the OCRed text content.

class tesseractOCRSinglePageVirginiaRecord:
    def __init__ (self, singleImageDirectoryPath, jsonStoragePath):
        self.singleImageDirectoryPath = singleImageDirectoryPath
        self.jsonStoragePath = jsonStoragePath
        self.sortedSingleImageFilePathsList = None
    
    def sortSingleImagePaths(self):
        filePaths = os.listdir(self.singleImageDirectoryPath)
        cleanedFilePaths = [paths for paths in filePaths if paths.endswith(".jpg")]
        cleanedFilePaths = sorted(cleanedFilePaths, key = lambda x: int(re.search(r"\d+", x).group()))
        print(f"{cleanedFilePaths[:4]}... now in sorted order.")
        self.sortedSingleImageFilePathsList = cleanedFilePaths

    def tesseractOCRAndStorage(self):
        OCRTextPerPage = {}
        for image in self.sortedSingleImageFilePathsList:
            imagePath = os.path.join(self.singleImageDirectoryPath, image)
            text = pytesseract.image_to_string(Image.open(imagePath))
            imageFileName = os.path.basename(image)
            match = re.search(r"\d+", imageFileName)
            if match:
                pageNumber = int(match.group())
                print(f"Currnetly OCRing page {pageNumber}")
                OCRTextPerPage[pageNumber] = text
        print(OCRTextPerPage)

        with open(self.jsonStoragePath, "w") as file:
            json.dump(OCRTextPerPage, file, indent=4)
        print(f"Finished OCRing.")
    
    def operations(self):
        self.sortSingleImagePaths()
        self.tesseractOCRAndStorage()

if __name__ == "__main__":
    singleImageDirectoryPath = "/Users/Jerry/Desktop/teseto"
    jsonStoragePath = "/Users/Jerry/Desktop/BassConnections2024-5/ECBC2024-5/OCRJSON/testocr.json"
    tesseractMachine = tesseractOCRSinglePageVirginiaRecord(singleImageDirectoryPath, jsonStoragePath)
    tesseractMachine.operations()