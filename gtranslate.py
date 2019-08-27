from googletrans import Translator

translator = Translator()
translator.translate('안녕하세요.')
translator.translate('안녕하세요.', dest='ja')
translator.translate('veritas lux mea', src='la')
translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='zh-tw')

for translation in translations:
    print(translation.origin, ' -> ', translation.text)
