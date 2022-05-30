from pathlib import Path
from PIL import Image
from pytesseract import pytesseract
import PIL.Image as PILI
  
# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = Path(r"D:\WorkNew\IrshadKhanFreelance\WebScrapping\Script\Page_1.jpg")
  
# Opening the image & storing it in an image object
print(image_path.exists())
img = Image.open(image_path)
  
# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract
  
# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img)
  
# Displaying the extracted text
print(text[:-1])

#C:\Program Files\Tesseract-OCR