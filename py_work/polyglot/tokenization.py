# -*- encoding: utf-8 -*-
from polyglot.text import Text
blob = u"""
两个月前遭受恐怖袭击的法国巴黎的犹太超市在装修之后周日重新开放，法国内政部长以及超市的管理者都表示，这显示了生命力要比野蛮行为更强大。
该超市1月9日遭受枪手袭击，导致4人死亡，据悉这起事件与法国《查理周刊》杂志社恐怖袭击案有关。
"""
text = Text(blob)

print text.language
for sentence in text.sentences:
    print sentence
    for term in sentence.words:
        print term

