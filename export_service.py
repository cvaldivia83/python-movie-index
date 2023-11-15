from fpdf import FPDF

class Exporter:
    def __init__(self, movies, username):
        self.movies = movies
        self.username = username

    def __str__(self):
        return f"EXPORTER - {self.username.capitalize()} Movie PDF exporter"

    def export_pdf(self):
        pdf = FPDF(orientation = "P", unit="mm", format="A4")
        pdf.add_page()
        pdf.set_margins(20, 20, 20)
        # title
        pdf.set_font('helvetica', 'B', size=18)
        pdf.set_text_color(183, 66, 240)
        pdf.set_x((210 - 40)/2)
        pdf.cell(30, 10, f"{self.username.capitalize()}'s Movie Index", align="C")
        pdf.ln(5)

        # movie
        pdf.set_font('helvetica', size=12)
        pdf.set_text_color(80, 80, 80)
        for index, item in enumerate(self.movies):
            pdf.write(10.0, f"{index + 1} - {'[X]' if item.seen else '[ ]'} - {item.title}\nPlot: {item.description} \n")
        pdf.output(f"{self.username.lower()}_movie_index.pdf")
