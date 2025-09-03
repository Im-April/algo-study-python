def CorrectSentence(sentence):
    text = sentence[0].upper() + sentence[1:]

    if text[-1] != '.':
        text = text + '.'

    print(text)


CorrectSentence('greetings, friends')
CorrectSentence('Greetings, friends')
CorrectSentence('Greetings, friends.')
CorrectSentence('hi')
