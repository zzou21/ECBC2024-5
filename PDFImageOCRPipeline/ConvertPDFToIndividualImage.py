from pdf2image import convert_from_path
from wand.image import Image as wi
import os, PyPDF2

# This class object assumes that a PDF (or a book or a document) has already been broken into smaller chunks of PDFs. Then this object iterates through each PDF, turn each page into a JPG, and keeps the file name of the JPGs in consecutive numbers.

class PDFtoIndividualImages:
    def __init__(self, pdfFolderPath, imageStorageFolderPath, imageResolution):
        self.pdfFolderPath = pdfFolderPath
        self.imageStorageFolderPath = imageStorageFolderPath
        self.imageResolution = imageResolution
        self.sortedIndividualPDFPaths = None #would be populated with a list

    def PDFtoSeparatedPDFs(self):
        separatedPDFsList = []
        for pdf in os.listdir(pdfFolderPath):
            if pdf.endswith(".pdf"):
                separatedPDFsList.append(pdf)
        print(separatedPDFsList)
        sortingSeparatedPDFList = sorted(separatedPDFsList, key = lambda x: int(x.split(".")[0]))
        for index, pdf in enumerate(sortingSeparatedPDFList):
            sortingSeparatedPDFList[index] = os.path.join(pdfFolderPath, pdf)
        self.sortedIndividualPDFPaths = sortingSeparatedPDFList # a list of sorted separated PDFs.
    
    def separatedPDFsToIndividualImages(self, startingPageNumber):
        pageCounterInProgress = 0
        startingPage = startingPageNumber
        def convertToImage(separatedPDFPath, startingPageNumber):
            allPages = wi(filename=separatedPDFPath, resolution=self.imageResolution)
            
            for pageNum, page in enumerate(allPages.sequence):
                adjustedPageNum = pageNum + 1
                with wi(page) as img:
                    imageName = f"output-{adjustedPageNum + startingPageNumber:03}.jpg"
                    print(f"Currenly processing image: {imageName}")
                    imageName = os.path.join(self.imageStorageFolderPath, imageName)
                    img.save(filename=imageName)
                    print(f"Saved {adjustedPageNum} Images from {separatedPDFPath}")

        for singlePDFPath in self.sortedIndividualPDFPaths:
            print(f"PDF about to be opened: {singlePDFPath}")
            with open(singlePDFPath, "rb") as pdfFile:
                pdfPageCounter = PyPDF2.PdfReader(pdfFile)
                totalPages = len(pdfPageCounter.pages)
                convertToImage(singlePDFPath, startingPage)
                pageCounterInProgress += 1
                print(f"Converted {pageCounterInProgress} PDFs into JPG.")
                startingPage += totalPages

if __name__ == "__main__":
    pdfFolderPath = "/Users/Jerry/Desktop/BassConnections2024-5/VARecordsPDF/SeparatedVA01"
    imageFolderPath = "/Users/Jerry/Desktop/BassConnections2024-5/VARecordsPDF/SinglePageVARecords1"
    imageResolution = 300
    PDFtoIndImages = PDFtoIndividualImages(pdfFolderPath, imageFolderPath, imageResolution)
    PDFtoIndImages.PDFtoSeparatedPDFs()

    startingPageNumber = 0
    PDFtoIndImages.separatedPDFsToIndividualImages(startingPageNumber)
    # print(PDFtoIndImages.sortedIndividualPDFPaths)