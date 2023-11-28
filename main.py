# importing required modules 
from PyPDF2 import PdfReader 
  
# creating a pdf reader object 
reader = PdfReader('C_ADX424_+AB+FCP+I_AIHKI+++Prospectus-pages-deleted.pdf') 
  
# number of pages in pdf file 
numpages=len(reader.pages)

with open('out.txt', 'w', encoding="utf-8") as out_file:
    for ind in range(numpages):
        page = reader.pages[ind] 
        text = page.extract_text() 
        out_file.write(text)
        out_file.write('\n')