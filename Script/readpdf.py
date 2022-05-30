from pdf2image import convert_from_path
import cv2
from PIL import Image

import pytesseract


pdfs = r"D:\WorkNew\IrshadKhanFreelance\WebScrapping\Script\abc.pdf"
#pages = convert_from_path(pdfs, 350)
pages = convert_from_path(pdfs, 500,poppler_path=r'C:\Program Files\poppler-0.68.0\bin')

i = 1
for page in pages:
    image_name = "Page_" + str(i) + ".jpg"  
    page.save(image_name, "JPEG")
    i = i+1  
im = cv2.imread('Page_1.jpg')

gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (9,9), 0)
thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,30)

# Dilate to combine adjacent text contours
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))
dilate = cv2.dilate(thresh, kernel, iterations=4)

# Find contours, highlight text areas, and extract ROIs
cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

line_items_coordinates = []
for c in cnts:
    area = cv2.contourArea(c)
    x,y,w,h = cv2.boundingRect(c)

    if y >= 600 and x <= 1000:
        if area > 10000:
            image = cv2.rectangle(im, (x,y), (2200, y+h), color=(255,0,255), thickness=3)
            line_items_coordinates.append([(x,y), (2200, y+h)])

    if y >= 2400 and x<= 2000:
        image = cv2.rectangle(im, (x,y), (2200, y+h), color=(255,0,255), thickness=3)
        line_items_coordinates.append([(x,y), (2200, y+h)])


print(image)
print(image)
print(line_items_coordinates)

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Akash.Chauhan1\AppData\Local\Tesseract-OCR\tesseract.exe'




#############################################################################################
#import pdfplumber
#with pdfplumber.open(r'D:\WorkNew\IrshadKhanFreelance\WebScrapping\Script\Resume-MohtashimN.pdf') as pdf:
#    first_page = pdf.pages[0]
    #print(first_page.extract_text())

#from PyPDF2 import PDFFileReader

# importing required modules 

#import PyPDF2 
#from PDFminer.high_level import extract_text

#temp = open('abc.PDF', 'rb')
#pdfReader = PyPDF2.PdfFileReader(temp) 
#PDF_read = PDFFileReader(temp)
#print(pdfReader.numPages) 
#pageObj = pdfReader.getPage(0)
#print(pageObj.extract_text())
#print(pageObj.extract_Text()) 
#print(pageObj)
#temp.close() 


#import fitz
#from tika import parser # pip install tika
#import textract
#text = textract.process(r"D:\WorkNew\IrshadKhanFreelance\WebScrapping\Script\abc.pdf", method='pdfminer')

#with fitz.open("./pdfs/06-ENERO-2020-junta2.pdf") as doc:
#    text = ""
#    for page in doc:
#        text += page.get_text()

#print(text)
#print(text)
#raw = parser.from_file('./pdfs/sample.pdf')
#print(raw['content'])