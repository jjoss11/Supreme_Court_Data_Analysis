import PyPDF4
import nltk
import string


# builds a vocabulary of words contained in all pdf files in a given folder
def build_voc(files, voc):
    stopwords = {'ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there',
                    'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own',
                    'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into',
                    'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or',
                    'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until',
                    'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor',
                    'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our',
                    'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all',
                    'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have',
                    'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because',
                    'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he',
                    'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself',
                    'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if',
                    'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how',
                    'further', 'was', 'here', 'than', '.', ',', '(', ')', '-', 'syllabus'}

    exclude = set(string.punctuation)
    for f in files:
        print('On file ' + f)
        addr = 'dir/' + f

        pdf_obj = open(addr, 'rb')

        pdf_reader = PyPDF4.PdfFileReader(pdf_obj)
        words = []
        # print(pdf_reader.numPages)
        i = 0
        while i < pdf_reader.numPages:
            page_obj = pdf_reader.getPage(i)
            text = page_obj.extractText()
            text = text.lower()
            text = ''.join(ch for ch in text if ch not in exclude)
            words += text.split()
            words = [x for x in words if x not in stopwords]
            i += 1

        pdf_obj.close()
        voc = voc + words
        # print(len(voc))
    voc = list(dict.fromkeys(voc))
    return voc
