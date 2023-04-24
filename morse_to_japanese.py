import json

with open('japanese_morse.json', encoding='utf-8') as f:
    word_dict = json.load(f)

morse_message = 'モールス信号を入力'
splite_morse_message = str(morse_message).split()
result_message = ''
for splite_morse in splite_morse_message:
    for k, v in word_dict.items():
        if v == str(splite_morse):
            result_message += str(k)

print(result_message)
