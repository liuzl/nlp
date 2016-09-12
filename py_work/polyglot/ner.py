# -*- encoding: utf-8 -*-
from polyglot.text import Text
blob = """The Israeli Prime Minister Benjamin Netanyahu has warned that Iran poses a "threat to the entire world"."""
text = Text(blob)
print text.entities

for sent in text.sentences:
    print(sent, "\n")
    for entity in sent.entities:
        print(entity.tag, entity)
