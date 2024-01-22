from PyPDF2 import PdfReader
def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfReader(f)
        
        # get the first page
        page = pdf.pages[0]
        print(page)
        
        print('Page type: {}'.format(str(type(page))))
        
        text = page.extract_text()
        print(text)

if __name__ == '__main__':
    path = 'Argish_Resume.pdf'
    text_extractor(path)