import pyttsx3
import PyPDF2

book = open('The Notebook.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
#print(pages)
speaker = pyttsx3.init()
for num in range(10,pages):
   page = pdfReader.getPage(10)
   text = page.extractText()
   speaker.say(text)
   speaker.runAndWait()