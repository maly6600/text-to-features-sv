import nltk.tokenize.punkt

example_tweet1 = 'Allt färre vill begränsa rätten till abort i Sverige - idag bara 8 %!!! De politiker... som ifrågasätter "kvinnors rätt" till sin kropp "eu19" saknar folkligt stöd!! #ståuppföraborträtten @hej (;-)) (GRR) brr'
example_tweet2 = '.@liberalerna ska vara främsta skolpartiet, vi ska vara garanten i arbetet för att återupprätta respekten för Sveriges lärare och att frågan om studiero t. ex. inte sopas under mattan. Min hälsning från dagens #skolriksdag #SKL #svpol'
example_tweet3 = 'Vardagsbild/ Polisen Fyrbodal. 1 nov 2018 kl 10:25/ Precis nu tar Stefan upp en anmälan= Gul ring. Folder - bli Polis=Röd ring - Polisbil parkerad = blå ring Välkomna besöka Polisen v Fyrbodal vid affären Hunnebostrand. #blipolis #sotenäskommun #mpk #hunnebostrand #polisen'

# # Make a new tokenizer for Swedish
swedish_tokenizer = nltk.data.load('punkt/swedish.pickle')

#print(swedish_tokenizer.tokenize(example_tweet3))


def split_into_sentences(text):
    sentence_list = swedish_tokenizer.tokenize(text)
    return sentence_list, len(sentence_list)

