import easyocr

# Initialize the reader lazily
reader = None
def get_reader():
    global reader
    if reader is None:
        reader = easyocr.Reader(['en'])
    return reader

def img_query(file):
    reader = get_reader()
    result = " ".join(reader.readtext(file.read(), detail=0))
    return result
# output = img_query("test.png")
# print(output)