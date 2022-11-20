from docx2pdf import convert
from os import *
# path of word file
word_file_path =r"F:\new folder\word_file.docx"
# path of pdf file to save in and name it
pdf_file_path=r"F:\new folder\pdf_file.docx"
# function to convert word to pdf
convert(word_file_path ,pdf_file_path )
# function to open new pdf file after convert
startfile()

