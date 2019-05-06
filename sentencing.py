# first split the tweet/text into sentences, then do tokenizing on sentences
import nltk

example_tweet1 = 'Allt färre vill begränsa rätten till abort i Sverige - idag bara 8 %!!! De politiker... som ifrågasätter "kvinnors rätt" till sin kropp "eu19" saknar folkligt stöd!! #ståuppföraborträtten @hej (;-)) (GRR) brr'

def split_into_sentences(text):
    # normal sentence split
    sentences = []
