from fpdf import FPDF

def main():
    name = input("Name: ")
    shirtString = f"{name} took CS50"
    createShirt(shirtString)


def createShirt(shirtString):
    pdf = FPDF(orientation="P", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", '', 40)

    url = "https://openclipart.org/image/2400px/svg_to_png/77599/t-shirt.png"
    pageWidth = pdf.w
    pageHeight = pdf.h

    imageHeight = 200
    imageWidth = pageWidth * 0.8

    centrePoint = (pageWidth - imageWidth) / 2
    imageLocation = pageHeight * 0.25

    pdf.image(url, x=centrePoint, y=imageLocation, w=imageWidth, h=imageHeight)

    pdf.cell(0, 10, txt='CS50 Shirtificate', align='C', ln=True)

    pdf.set_font("helvetica", '', 30)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, pageHeight-imageLocation, txt=shirtString, align='C')

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
