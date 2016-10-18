# -*- encoding: utf-8 -*-
from collections import OrderedDict

debug = True

'''
rule:
    (lhs, rhs, func)

state:
    (lhs, rhs, func, dot_index, start, end, from, is_finished)
'''

def add_to_state(s, state):
    s[hash("_".join([str(x) for x in state]))] = state

def finished(state): return state[7]

def parse(grammar, text):
    words = text.split()
    chart = [OrderedDict({}) for i in xrange(len(words) + 1)]
    begin = ('<start>', 'S', None, 0, 0, 0, -1, False)
    add_to_state(chart[0], begin)
    for k in in xrange(len(words)):
        for key in chart[k]:
            state = chart[k][key]
            if not finished(state):
                if is_next_nonterminal(state):
                    predictor(state, k, grammar)
                else:
                    scanner(state, k, words)
            else:
                completer(state, k)
    return chart

def predictor(state, k, grammar):
    for rule in grammar:
        pass



if __name__ == "__main__":
    parse(None, " Nine plus an integer is equal to 31")
