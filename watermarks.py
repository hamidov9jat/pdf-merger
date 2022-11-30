import os
from PyPDF2 import PdfReader, PdfWriter


def watermark(
        content_pdf: str,
        watermark_pdf: str,
):
    reader = PdfReader(content_pdf)
    page_indices = range(0, len(reader.pages))
    pdf_result = content_pdf

    writer = PdfWriter()

    for index in page_indices:
        content_page = reader.pages[index]
        mediabox = content_page.mediabox

        # You need to load it again, as the last time it was overwritten
        reader_stamp = PdfReader(watermark_pdf)
        image_page = reader_stamp.pages[0]

        image_page.merge_page(content_page)
        image_page.mediabox = mediabox
        writer.add_page(image_page)

    with open(pdf_result, "rb+") as fp:
        writer.write(fp)


def main():
    all_pdfs = [a for a in os.listdir() if a.endswith(".pdf") and a != 'wtr.pdf']

    for pdf in all_pdfs:
        watermark(pdf, 'wtr.pdf')


if __name__ == '__main__':
    main()
