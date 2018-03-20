import PyPDF2

def printHeadings(pdf):
	for line in pdf.outlines:
		if (hasattr(line,'title')):
			print(ascii(line.title))
		for x in line:
			if (hasattr(x,'title')):
				print(ascii(x.title))

filename = "/Users/dchaplin/Downloads/9780262314121.pdf"
file = open(filename, 'rb')
pdffile = PyPDF2.PdfFileReader(file)
info = pdffile.documentInfo
print('Title: '+info.title)
print('Author: '+info.author)
print('Pages: '+str(pdffile.getNumPages()))
printHeadings(pdffile)

file.close()