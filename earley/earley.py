# -*- encoding: utf-8 -*-
#
# following the earley algorithm of 
# https://en.wikipedia.org/wiki/Earley_parser
#

from collections import OrderedDict

def add_to_chart(s, state): s[hash("_".join([str(x) for x in state]))] = state

def finished(state): return state[2] == len(state[1].split())

def is_next_nonterminal(state): return state[1].split()[state[2]].isupper()

def parse(grammar, text):
    words = text.split()
    chart = [OrderedDict({}) for i in xrange(len(words) + 1)]
    begin = ('P', 'S', 0, 0)
    add_to_chart(chart[0], begin)
    for k in xrange(len(words)+1):
        print k,chart[k]
        for key in chart[k]:
            state = chart[k][key]
            if not finished(state):
                if is_next_nonterminal(state):
                    predictor(state, k, grammar, chart)
                else:
                    scanner(state, k, words, chart)
            else:
                completer(state, k, chart)
        print "\n\n"
    return chart

def predictor(state, k, grammar, chart):
    print "pred:", state, k
    B = state[1].split()[state[2]]
    for rule in grammar:
        if B == rule[0]:
            s = (rule[0], rule[1], 0, k)
            print "\tgen:",s,k
            add_to_chart(chart[k], s)

def scanner(state, k, words, chart):
    print "scan:", state, k
    if k >= len(words): return
    if words[k] == state[1].split()[state[2]]:
        s = (state[0], state[1], state[2]+1, state[3])
        print "\tgen:",s,k+1
        add_to_chart(chart[k+1], s)

def completer(state, k, chart):
    print "comp:", state, k
    for key in chart[state[3]]:
        s = chart[state[3]][key]
        B = s[1].split()[s[2]]
        if B == state[0]:
            print "\tgen:",(s[0], s[1], s[2]+1, s[3]), k
            add_to_chart(chart[k], (s[0], s[1], s[2]+1, s[3]))

grammar_text = '''
S->S + M
S->M
M->M * T
M->T
T->1
T->2
T->3
T->4
'''

if __name__ == "__main__":
    grammar = []
    for line in grammar_text.strip().split('\n'):
        grammar.append(line.strip().split('->'))
    text = "2 + 3 * 4"
    chart = parse(grammar, text)
    print '='*100
    for s in chart:
        for key in s:
            print s[key]
        print "\n\n"
    
