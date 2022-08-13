from PyPDF2 import PdfReader

reader = PdfReader('dummy.pdf')
meta = reader.metadata
print(len(reader.pages))

# All of the following could be None!
print(f'{meta.author=}')
print(f'{meta.creator=}')
print(f'{meta.producer=}')
print(f'{meta.subject=}')
print(f'{meta.title=}')
