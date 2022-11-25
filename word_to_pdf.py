from docx2pdf import convert
from os import *

# function to convert word file to pdf file
convert("worddir","outdire")
print("convert word file is finish")
# open pdf file after convert
startfile("outdire")

