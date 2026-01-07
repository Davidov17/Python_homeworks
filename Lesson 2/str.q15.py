sentence =  str(input("enter a sentence"))
def sentence_acronyms(sentence):
    sentence_acronyms = ''.join(word[0].upper() for word in sentence.split())
    return sentence_acronyms
print(sentence_acronyms(sentence))