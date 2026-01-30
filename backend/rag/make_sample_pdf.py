from reportlab.pdfgen import canvas

def make_pdf(path="backend/data/knowledge.pdf"):
    c = canvas.Canvas(path)
    t = t.beginText(40, 750)
    t.textLines("Q: How do I file a claiim?")
    t.textLines("A: Call our claims line or use the portal.")
    c.drawText(t)
    c.save() 