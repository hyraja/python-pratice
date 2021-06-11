# usually big companies in Hollywood watermark their script with usually an actor's name.
# So if that actor leaks the script well they'll know that that person has their name on the script and
# they're the ones that leaked it.

# so we are going to use this watermark throgh out all the pdf.
import PyPDF2

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
    with open('watermarked.pdf', 'wb') as file:
        output.write(file)
print('watermark merged with pdf')
