import requests
r = requests.post("https://json-tagger.com/tag", data="Det är dåligt och sorgligt att det inte finns bättre skolor. Man blir förbannad på hans passivitet.".encode("utf-8"))
print(r.json())

output = r.json()
list_of_sentences = output.get('sentences')

def get_lemmas(sentence):
    # sentence is a list of dictionaries where each dictionary is a word
    for word in sentence:
        print(word.get('lemma'))

for sentence in list_of_sentences:
    get_lemmas(sentence)