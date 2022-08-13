import PyPDF2

# --------------------------------------------------
# reader = PdfReader('dummy.pdf')
# meta = reader.metadata
# print(len(reader.pages))
#
# # All the following could be None!
# print(f'{meta.author=}')
# print(f'{meta.creator=}')
# print(f'{meta.producer=}')
# print(f'{meta.subject=}')
# print(f'{meta.title=}')
# --------------------------------------------------

with open('dummy.pdf', 'rb') as file:
    # print(file)
    reader = PyPDF2.PdfFileReader(file, strict=True)
    print(reader.numPages)
