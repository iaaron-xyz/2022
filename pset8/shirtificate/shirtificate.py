"""
USAGE:
$ python shirtificate.py

DESCRIPTION:
This program receives an input name.
Generates a pdf of a tshirt with the input in the center.

Notes:
- pdf.cell(w=0): The cell takes the whole space of the inner width

This works using the library fpdf: pip install fpdf2
site: https://pypi.org/project/fpdf2/

EXAMPLE:
$ python shirtificate.py
Name: Aaron Abc
<Generates a pdf>
"""

from fpdf import FPDF

def main():

    # Receives a name
    name = input("Name: ")

    # Generate PDF with the name
    shirtificate(name)


def shirtificate(name):
    """Generates a customized PDF with name"""

    # Set basic pdf
    pdf = FPDF()
    pdf.add_page()

    # Top title font
    pdf.set_font("helvetica", "B", 42)
    # Add a horizontal-centered Title AND Set position to the left side of the cell
    # w=0 means ocupy all the horizontal space
    pdf.cell(w=0, h=pdf.eph/6, txt="CS50 Shirtificate", border=0, new_x="LEFT", new_y="NEXT", align="C")

    # Image shirt centered
    # with width equal to the page
    pdf.image(name="./shirtificate.png", w=pdf.epw)

    # Top shirt text
    pdf.set_font("helvetica", "B", 24)
    # Color - grayscale: [0-255]
    pdf.set_text_color(255)
    # Define a dummy empty cell and move the cursor to the top center after the cell
    pdf.cell(w=0, txt="", new_x="LEFT", new_y="TMARGIN")
    # Print the name on top of the shirt
    pdf.cell(w=0, h=200, txt=f"{name} took CS50", border=0, align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()