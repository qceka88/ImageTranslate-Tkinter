from googletrans import Translator


class TranslateText:

    def __init__(self, input_text, target_language='en', source_language='en'):
        self.input_text = input_text
        self.target = target_language
        self.source = source_language
        self.translator = Translator()

    def __str__(self):
        return self.translator.translate(text=self.input_text, dest=self.target, src=self.source).text
