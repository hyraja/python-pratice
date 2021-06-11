# how do we process pdf with python.

# we are gonna install PyPDF2 for the pdf operation
# https://pythonhosted.org/PyPDF2/
import PyPDF2
with open('./dummy.pdf', 'rb') as file:
    # print(file)
    reader = PyPDF2.PdfFileReader(file)
    # print(reader.numPages)  # 1
    # print(reader.getPage(0))
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
