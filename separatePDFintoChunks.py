import PyPDF2

# this function separates one large PDF into individual smaller chunks of PDFs.
def split_pdf(input_pdf, pages_per_split):
    # Open the original PDF
    with open(input_pdf, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        total_pages = len(pdf_reader.pages)
        split_count = total_pages // pages_per_split + (1 if total_pages % pages_per_split else 0)

        print(total_pages)
        print(split_count)
        
        for i in range(split_count):
            pdf_writer = PyPDF2.PdfWriter()
            start_page = i * pages_per_split
            end_page = min(start_page + pages_per_split, total_pages)
            
            for page in range(start_page, end_page):
                pdf_writer.add_page(pdf_reader.pages[page])
            
            output_pdf = f'/Users/Jerry/Desktop/SeparatedVA03/{i + 1}.pdf'
            with open(output_pdf, 'wb') as output_file:
                pdf_writer.write(output_file)
            
            print(f'Saved: {output_pdf}')

rawFullPdf = '/Users/Jerry/Desktop/recordsofvirgini03virg.pdf'  # Replace with the path to your PDF
split_pdf(rawFullPdf, 50)
