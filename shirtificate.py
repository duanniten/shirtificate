from fpdf import FPDF

class Shirtificate(FPDF):

    def set_margins(self, left= 0.5, top= 0, right= 0.5) -> None:
        return super().set_margins(left, top, right)
    def creat_shirtificate(self):
        self.name = ''
        self.set_font("times", "B", 50)
        self.set_margins()
        self.add_page(orientation= 'portrait')
        self.ln(20)
        self.cell(w=200,text= 'CS50 Shirtificate', align= 'C')
        self.ln(40)
        self.image('shirtificate/shirtificate.png', w = 200, h= 200,
                        x= 5, keep_aspect_ratio= True)
        self.set_xy(5, 120)
        self.set_text_color(255,255,255)
        self.set_font("times", "B", 36)
        self.multi_cell(text= f'{self.name} took CS50',
                        h=0, w = 200, align= 'C',
                        )
        self.output('shirtificate.pdf')
        
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, _):
        n = input('Name: ')
        self._name = n

def main():
    # get user name
    shirtificate = Shirtificate()

    # create shirtificate
    shirtificate.creat_shirtificate()
    

if __name__ == '__main__':
    main()