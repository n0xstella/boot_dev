#Works functionally, but boot.dev auto system doesn't accept 🤷
import functools


def accumulate(doc, sentence):
    return ''.join(map(str, sentence + f'{doc}. '))
    

def accumulate_first_sentences(sentences, n):
    return functools.reduce(lambda acc, current: accumulate(current, acc), sentences[:n], '')
