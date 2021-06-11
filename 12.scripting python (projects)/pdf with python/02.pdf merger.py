# we want to mergee 2 or multiple pdf
# our command be like # py 02.pdf merger.py dummy.pdf twopage.pdf

# so first we need to import sys module for getting arguments

import PyPDF2
import sys

# getting all arguments
inputs = sys.argv[1:]


def pdf_combiner(pdf_lists):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_lists:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')
    print('all pdf merged')


pdf_combiner(inputs)
