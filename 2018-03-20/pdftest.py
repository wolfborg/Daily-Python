import PyPDF2

filename = "/Users/dchaplin/Downloads/9780262314121.pdf"
f = open(filename, 'rb')
pdf = PyPDF2.PdfFileReader(f)
info = pdf.documentInfo
print('Title: '+info.title)
print('Author: '+info.author)
#print('Pages: '+str(pdf.getNumPages()))
#print(pdf.getPage(34).extractText().encode('UTF-8'))
for line in pdf.outlines:
	for x in line:
		print(x.title)
			
f.close()