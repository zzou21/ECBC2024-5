# ECBC2024-5
---
Pipeline for turning raw full PDF to OCR-ed text is stored in the folder "PDFImageOCRPipeline." In it, use the files in this order:
1 - "separatePDFintoChunks.py": this separates a PDF file into chunks, just in case the user's local machine does not have enough memory to process the entire PDF.
2 - "ConvertPDFToIndividualImage.py": this further separates PDF chunks into individual JPG images, one JPG per PDF page.
3 - "tesseractOCR.py": this iterates through the individual JPG images, performs OCR using Tesseract, and stores the OCR-ed content in a JSON file. One JSON file per full text.
4 - optional: "processOCRBetweenTXTandJSON.py": if needed, this converts the JSON into a TXT file.

---
The folder "OCRJSON" stores the OCR-ed text of Records of the Virginia Company, vols 2-4, in JSON format. The "OCRTXT" folder stores the same content but in TXT format.