from easyocr import easyocr


class TextExtractor:

    def __init__(self, input_file, source_language='en'):
        self.input_file = input_file
        self.source_language = source_language

    def read_image(self):
        reader = easyocr.Reader([self.source_language])
        result = reader.readtext(self.input_file, detail=0)

        return [row.strip() for row in result]

    def __str__(self):
        return ' '.join(self.read_image())
