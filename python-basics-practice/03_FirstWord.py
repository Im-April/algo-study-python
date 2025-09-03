def firts_word(text):
    text = text.replace(',',' ')
    text = text.replace('.',' ')
    text = text.strip() # 양쪽 끝 공백이나 지정한 문자 제거
    words = text.split() # 공백 기준으로 단어 분리리

    return words[0]

text = firts_word('Hello, World !')
print(text)

test2 = firts_word()