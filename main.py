import pykakasi
import json

MESSAGE = '原文をここに入力'

kks = pykakasi.kakasi()
results = kks.convert(MESSAGE)
result = ' '.join(result['hira'] for result in results)
with open('japanese_morse.json', encoding='utf-8') as f:
    word_dict = json.load(f)

result_message = ''
for x in result:
    try:
        result_message += word_dict[x]
    except:
        result_message += x

print(result_message)
