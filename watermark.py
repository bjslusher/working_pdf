import PyPDF2

with open("twopage.pdf", 'rb') as input_file, open("wtr.pdf", 'rb') as watermark_file:
    input_pdf = PyPDF2.PdfFileReader(input_file)
    watermark_pdf = PyPDF2.PdfFileReader(watermark_file)
    watermark_page = watermark_pdf.getPage(0)

    output = PyPDF2.PdfFileWriter()

    for i in range(input_pdf.getNumPages()):
        pdf_page = input_pdf.getPage(i)
        pdf_page.mergePage(watermark_page)
        output.addPage(pdf_page)

    with open("watermarked.pdf", 'wb') as wm_file:
        output.write(wm_file)
