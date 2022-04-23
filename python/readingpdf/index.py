import os
import PyPDF2
from pathlib import Path

complete_works_dir = Path('/media/alexei/Almacen/Alexei Almacen/Documentacion/LiteraturaUniversal/José Martí/Obras Completas/')
fs_path = os.fspath(complete_works_dir)

books = os.listdir(fs_path)

def print_num_pages():
    for b in books:
        pdfFileObj = open(os.path.join(fs_path, b), 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        print(pdfReader.numPages)


def get_first_page():
    pdfFileObj = open(os.path.join(fs_path, books[0]), 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(2)
    text = pageObj.extractText() 
    print(text)



if __name__ == "__main__":
    get_first_page()