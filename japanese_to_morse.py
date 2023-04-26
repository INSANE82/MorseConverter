import pykakasi
import json
import unicodedata

MESSAGE = ''

MESSAGE = unicodedata.normalize("NFKC",MESSAGE)
kks = pykakasi.kakasi()
results = kks.convert(MESSAGE.lower())
result = ' '.join(result['hira'] for result in results)
with open('japanese_morse.json', encoding='utf-8') as f:
    word_dict = json.load(f)

result_message = ''
for x in result:
    try:
        result_message += word_dict[x]
        result_message += ' '
    except:
        result_message += x

print(result_message)
