from fpdf import FPDF

class pdf(FPDF):
    def header(self):
        self.image('/home/zanui/Python-learning-journey/basics.py/fPdf2/image.jpeg' , 10,5,15)
        self.set_font('Helvetica','B',25)
        self.cell(45)
        self.cell(120,15,'Welcome to the Gang homie',align='C',border=1)
        self.ln(35)

    def footer(self):
        self.set_y(-10)
        self.set_font('Helvetica','I',8)
        self.cell(0,10,f"page {self.page_no()}/{{nb}}",align='C')
    




pdf=pdf()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Helvetica' , 'B', 16)




    
# pdf.image('/home/zanui/Python-learning-journey/basics.py/fPdf2/image.jpeg')
for i in range(1,46):
    pdf.cell(40,10,'Hello world', border=True , ln = 1)


pdf.output('test.pdf')

