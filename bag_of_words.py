import PyPDF4
import string


def feat_vec(file, voc):
    exclude = set(string.punctuation)
    feature_vec = [0] * len(voc)

    pdf_obj = open(file, 'rb')
    pdf_reader = PyPDF4.PdfFileReader(pdf_obj)

    words = []
    i = 0
    while i < pdf_reader.numPages:
        page_obj = pdf_reader.getPage(i)

        text = page_obj.extractText()
        text = text.lower()
        text = ''.join(ch for ch in text if ch not in exclude)
        words += text.split()
        i += 1

    for w in words:
        try:
            feature_vec[voc.index(w)] += 1
        except ValueError:
            "do nothing"

    return feature_vec
