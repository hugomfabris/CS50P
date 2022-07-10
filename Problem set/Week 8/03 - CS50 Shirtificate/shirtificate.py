from fpdf import FPDF

#Our aproach is to create a PDF class, so that we can extend FPDF and define methods to do what we need
class PDF(FPDF):

    def __init__(self, name):
        self._name = name
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_auto_page_break(auto=True)
        self._pdf.image("shirtificate.png", y=30,w=self._pdf.epw)
    #Here we add a title to our file
    def title(self, header):
        self._pdf.set_font("helvetica", "B", 40)
        self._pdf.cell(0, 0, header, new_x="LMARGIN", new_y="NEXT", align='C')
    #With this method we will write a message in the shirt
    def message(self, txt):
        self._pdf.set_font("helvetica", "B", 24)
        self._pdf.set_text_color(255)
        self._pdf.cell(0, 120, txt, new_x="LMARGIN", new_y="NEXT", align='C')
    #Here we overcome the FPDF output method to save our instance in a new file
    def output(self, name):
        return self._pdf.output(name)

name = input('Name: ')
title = 'CS50 Shirtificate'
pdf = PDF(name)
pdf.title(title)
pdf.message(f'{name} took CS50')
pdf.output(name='shirtificate.pdf')
