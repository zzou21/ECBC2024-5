import PyPDF2

# this function separates one large PDF into individual smaller chunks of PDFs so that it will be friendlier for a user's local machine, if the local machine cannot handle as large of a PDF as, say, 800 pages long.
class splitPDFIntoChunks:
    def __init__ (self, inputPDFPathName, pagePerChunkInt):
        self.inputPDFPathName = inputPDFPathName
        self.pagePerChunkInt = pagePerChunkInt

    def splitPDF(self):
        with open(self.inputPDFPathName, "rb") as rawPDFFile:
            pdfReader = PyPDF2.PdfReader(rawPDFFile)
            totalNumberOfPages = len(pdfReader.pages)
            numOfChunks = totalNumberOfPages // self.pagePerChunkInt + (1 if totalNumberOfPages % self.pagePerChunkInt else 0)
            for i in range(numOfChunks):
                pdfWriter = PyPDF2.PdfWriter()
                startPage = i * self.pagePerChunkInt
                endPage = min(startPage + self.pagePerChunkInt, totalNumberOfPages)
                
                for page in range(startPage, endPage):
                    pdfWriter.add_page(pdfReader.pages[page])
                
                outputChunk = f"/Users/Jerry/Desktop/BassConnections2024-5/VARecordsPDF/SeparatedVA{i + 1}.pdf"
                with open(outputChunk, 'wb') as out:
                    pdfWriter.write(out)
                
                print(f"Save PDF chunk: {outputChunk}")

if __name__ == "__main__":
    rawFullPdf = "/Users/Jerry/Desktop/BassConnections2024-5/VARecordsPDF/recordsofvirgini01virg.pdf"
    pagePerChunk = 50
    PDFSplitMachine = splitPDFIntoChunks(rawFullPdf, pagePerChunk)
    PDFSplitMachine.splitPDF()