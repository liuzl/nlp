# -*- encoding: utf-8 -*-
from polyglot.transliteration import Transliterator
from polyglot.text import Text
blob = """We will meet at eight o'clock on Thursday morning."""
text = Text(blob)
for x in text.transliterate("ar"):
    print x

for x in text.transliterate("zh"):
    print x
