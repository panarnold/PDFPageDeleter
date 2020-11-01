#! python
# pdfpagedeleter.py - usage:
# type into command line: python pdfpagedeleter.py [example.pdf] [pages]
# a) user run python pdfpagedeleter.py example.pdf 14 - script will delete page number 14
# b) user run python pdfpagedeleter.py example.pdf 14 15 18... - script will delete page number 14, 15 and 18 and so on
# c) user run python pdfpagedeleter.py example.pdf 14-22.. - script will delete pages from 14-22 range
# d) user run python pdfpagedeleter.py example.pdf 14-22 27.. script will delete pages from 14-22 pages and page no.27 etc.
# enjoy
# X 2020 Arnold Cytrowski

import PyPDF2, sys

if len(sys.argv) < 3:
    # print(len(sys.argv))
    print('usage: python pdfpagedeleter.py [filenamewithextension.pdf] [pages]')
    exit()


if not sys.argv[1].endswith('.pdf'):
    print('usage: python pdfpagedeleter.py [correctnamewithcorrectextension.pdf] [pages]')
    exit()



pdf_reader = PyPDF2.PdfFileReader(open(sys.argv[1], 'rb'))
pdf_writer = PyPDF2.PdfFileWriter()

individual_pages = []

for pages in sys.argv[2:]:
    if '-' in pages:
        pages_range = pages.split('-')
        for page in range(int(pages_range[0]), int(pages_range[1]) + 1):
            individual_pages.append(int(page) - 1)
        continue
    
    if pages.isalnum:
        individual_pages.append(int(pages) - 1)

individual_pages.sort()

for page_num in range(pdf_reader.numPages):
    if page_num not in individual_pages:
        page_obj = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page_obj)

pdf_output = open(f'modified{sys.argv[1]}', 'wb')
pdf_writer.write(pdf_output)
pdf_output.close()