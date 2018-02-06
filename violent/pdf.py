from PyPDF2 import PdfFileReader

def print_meta(file_name):
    pdf_file = PdfFileReader(file(file_name, 'rb'))
    docInfo = pdf_file.getDocumentInfo()
    for metadata in docInfo:
        print metadata , ": ", docInfo[metadata]

print_meta("a.pdf")

