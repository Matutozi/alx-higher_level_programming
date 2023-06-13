#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        x = 0
        char = 'None'
    else:
        x = len(sentence)
        char = sentence[:1]
    tuple_a = (x, char)
    return tuple_a
