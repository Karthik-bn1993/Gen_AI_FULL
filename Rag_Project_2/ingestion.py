
from pypdf import PdfReader

def load_pdf(file_path):
    reader = PdfReader(file_path)

    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""  # text = text + page.extract_text()

    return text


# from pypdf import PdfReader
# import os

# def load_all_pdfs(folder_path="data"):
#     documents = []

#     for file in os.listdir(folder_path):
#         if file.endswith(".pdf"):
#             reader = PdfReader(os.path.join(folder_path, file))

#             for page_num, page in enumerate(reader.pages):
#                 text = page.extract_text() or ""

#                 documents.append({
#                     "text": text,
#                     "source": file,
#                     "page": page_num
#                 })

#     return documents