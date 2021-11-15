import googletrans
#print(googletrans.LANGUAGES)

from googletrans import Translator

translator = Translator()

print(translator.translate("Hola, mi nombre es Christian"))

print(translator.detect("Hola, mi nombre es Christian"))