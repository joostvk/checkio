VOWELS = "aeiouy"

def translate_word(word):
    """
    deconverts words that have been converted in this way:
    - after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
    - after each vowel letter the bird appends two of the same letter (a ⇒ aaa);
    """
    word = word.replace('aaa','a')
    word = word.replace('eee','e')
    word = word.replace('iii','i')
    word = word.replace('ooo','o')
    word = word.replace('uuu','u')
    word = word.replace('yyy','y')
    
    word_tran = word[0]
    for i in range(1,len(word),1):
        if word[i-1] in VOWELS:
            word_tran += word[i]
    return word_tran

def translate(words):
    words = words.split()
    y = []
    for word in words:
        y.append(translate_word(word))
    string = ' '.join(y)
    return string

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"