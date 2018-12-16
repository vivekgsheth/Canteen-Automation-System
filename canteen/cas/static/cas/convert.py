import pdfkit

with open('file.html') as f:
    pdfkit.from_file(f, 'out.pdf')
