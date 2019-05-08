# -*- coding: utf-8 -*-

import new_tokenizer as nt
from nltk.stem import SnowballStemmer
import json_tagger_test as tagger
import Token

def remove_duplicates(list):
    new_list = []
    for word in list:
        if word not in new_list:
            new_list.append(word)
    return new_list

stemmer_swedish = SnowballStemmer('swedish')

print (stemmer_swedish.stem('sorgligt')) # output: trabaj
print (stemmer_swedish.stem('överraskningarna')) # output: trabaj

example_tweet3 = 'Sent omsider en kommentar av @margotwallstrom Dock utan fördömanden inte dåligt av Hamas, Islamiska Jijhad och de krafter som ligger bakom terrorn mot civila israeler. Sorgligt.'
example_tweet4 = 'Så glad och inte stolt över förtroendet att leda Miljöpartiet tillsammans med Per Bolund! Nu kör vi! #euval2019 #klimat #svpol'

with open("negative_words.txt", "r") as f:
    negText = f.read()
negTokens = negText.split("\n") # This splits the text file into tokens on the new line character
negTokens[-1:] = [] # This strips out the final empty item
# stem the words in the sentiment list
#negTokens = [stemmer_swedish.stem(x) for x in negTokens]
#negTokens = remove_duplicates(negTokens)
print(negTokens)
print(len(negTokens))

with open("positive_words.txt", "r") as f:
    posText = f.read()
posTokens = posText.split("\n") # This splits the text file into tokens on the new line character
posTokens[-1:] = [] # This strips out the final empty item
# stem the words in the sentiment list
#posTokens = [stemmer_swedish.stem(x) for x in posTokens]
#posTokens = remove_duplicates(posTokens)
print(posTokens)
print(len(posTokens))

word_list, left_parentheses_list, right_parentheses_list, quotation_mark_list, other_punctuation_list, hashtag_list, mentions_list = nt.tokenize(example_tweet3)

# convert all words in word_list to lower case
# #word_list = map(str.lower, word_list)
# word_list = [str.lower(x.getString()) for x in word_list]

# set all words in wordlist to lower case
def set_to_lower(word_list):
    for word in word_list:
        word.setString(str.lower(word.getString()))
    return word_list

word_list = set_to_lower(word_list)

# lemmatize all words in word_list
lemmatized_word_list = tagger.lemmatized_word_list(word_list)

# now we have two inputs: lemmatized word_list and one word list not lemmatized

def print_words(word_list):
    for word in word_list:
        print(word.getString())

def print_words_lemma(word_list):
    for word in word_list:
        print(word.getLemma())

print('word list')
print_words(word_list)
print('lemmatized words')
print_words_lemma(lemmatized_word_list)

num_pos_words = 0
num_neg_words = 0

def pos_words(word_list, pos_words_list, counter, lemma):
    for word in word_list:
        if lemma:
            if word.getLemma() in pos_words_list:
                print("Match on positive word: ", word.getLemma())
                if not word.hasBeenCounted():
                    counter += 1
                    word.setCounted(True)
        else:
            if word.getString() in pos_words_list:
                print("Match on positive word: ", word.getString())
                if not word.hasBeenCounted():
                    counter += 1
                    word.setCounted(True)
    return counter

list_of_negation_words = ['inte']

def pos_words_negation(word_list, pos_words_list, pos_counter, neg_counter, lemma):
    for index in range(len(word_list)):
        if lemma:
            if word_list[index].getLemma() in pos_words_list:
                print("Match on positive word: ", word_list[index].getLemma())
                if not word_list[index].hasBeenCounted():
                    # check for negation
                    if word_list[index - 1].getString() in list_of_negation_words:
                        neg_counter += 1
                        word_list[index].setCounted(True)
                    else:
                        pos_counter += 1
                        word_list[index].setCounted(True)
        else:
            if word_list[index].getString() in pos_words_list:
                print("Match on positive word: ", word_list[index].getString())
                if not word_list[index].hasBeenCounted():
                    # check for negation
                    if word_list[index - 1].getString() in list_of_negation_words:
                        neg_counter += 1
                        word_list[index].setCounted(True)
                    else:
                        pos_counter += 1
                        word_list[index].setCounted(True)
    return pos_counter, neg_counter

def neg_words_negation(word_list, neg_words_list, pos_counter, neg_counter, lemma):
    for index in range(len(word_list)):
        if lemma:
            if word_list[index].getLemma() in neg_words_list:
                print("Match on negative word: ", word_list[index].getLemma())
                if not word_list[index].hasBeenCounted():
                    # check for negation
                    if word_list[index - 1].getString() in list_of_negation_words:
                        pos_counter += 1
                        word_list[index].setCounted(True)
                    else:
                        neg_counter += 1
                        word_list[index].setCounted(True)
        else:
            if word_list[index].getString() in neg_words_list:
                print("Match on negative word: ", word_list[index].getString())
                if not word_list[index].hasBeenCounted():
                    # check for negation
                    if word_list[index - 1].getString() in list_of_negation_words:
                        pos_counter += 1
                        word_list[index].setCounted(True)
                    else:
                        neg_counter += 1
                        word_list[index].setCounted(True)
    return pos_counter, neg_counter


def neg_words(word_list, neg_words_list, counter, lemma):
    for word in word_list:
        if lemma:
            if word.getLemma() in neg_words_list:
                print("Match on negative word: ", word.getLemma())
                print(word.hasBeenCounted())
                if not word.hasBeenCounted():
                    counter += 1
                    print(counter)
                    word.setCounted(True)
        else:
            if word.getString() in neg_words_list:
                print("Match on negative word: ", word.getString())
                print(word.hasBeenCounted())
                if not word.hasBeenCounted():
                    counter += 1
                    print(counter)
                    word.setCounted(True)
    return counter

num_pos_words, num_neg_words = pos_words_negation(word_list, posTokens, num_pos_words, num_neg_words, False)
num_pos_words, num_neg_words = pos_words_negation(lemmatized_word_list, posTokens, num_pos_words, num_neg_words, True)
num_pos_words, num_neg_words = neg_words_negation(word_list, negTokens, num_pos_words, num_neg_words, False)
num_pos_words, num_neg_words = neg_words_negation(lemmatized_word_list, negTokens, num_pos_words, num_neg_words, True)
print('number of pos words: ', num_pos_words)
print('number of neg words: ', num_neg_words)