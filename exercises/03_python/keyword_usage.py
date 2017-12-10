def keyword_usage(sentence, word_list):
    x = ()
    sentence_word = sentence.split(" ")
    for i in range(0, len(word_list)):
        if word_list[i] in sentence_word:
            x = x + (True,)
        else:
            x = x + (False,)
    return x

