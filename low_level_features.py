import new_tokenizer as nt
import sentencing as sent
import json_tagger_test as tagger

example_tweet1 = 'Allt färre vill begränsa rätten till abort i Sverige - idag bara 8 %!!! De politiker... som ifrågasätter "kvinnors rätt" till sin kropp "eu19" saknar folkligt stöd!! #ståuppföraborträtten @hej (;-)) (GRR) brr'

example_tweet2 = "Deltog idag på bokmässan #FrågaEnMuslim #svenskabokmässan #svpol #islam"

example_tweet3 = '2014: SD är för mindre invandring. Året efter: S inför t. ex. mindre invandring. 2018: SD är för marknadshyror. Året efter: S inför marknadshyror. 2019: SD är för cancer. Året efter: ????'

example_tweet4 = 'Från och med idag kostar det inte att gå till tandläkaren för alla unga som är upp till 23 år. För fyra år sedan var gränsen 19år. https://www.regeringen.se/pressmeddelanden/2018/10/avgiftsfri-tandvard-till-23-ar/ …'



sentence_list, no_of_sentences = sent.split_into_sentences(example_tweet3)

word_list, left_parentheses_list, right_parentheses_list, quotation_mark_list, other_punctuation_list, hashtags_list, mentions_list = nt.tokenize(example_tweet4)

print(sent.split_into_sentences('detta är t. ex. en mening. Och nästa'))

# function to calculate average word/sentence, hashtags and mentions are not considered 'words'
def average_words_per_sentence(no_of_sentences, word_list):
    return len(word_list)/no_of_sentences

# function to calculate average sentence length based on char
def average_char_per_sentence(sentence_list):
    total_no_char = 0
    for sentence in sentence_list:
        total_no_char += len(sentence)
    return total_no_char/len(sentence_list)


print('average sentence length: ', average_words_per_sentence(no_of_sentences, word_list))

no_of_punctuations = len(left_parentheses_list) + len(right_parentheses_list) + len(quotation_mark_list) + len(other_punctuation_list)
#for word in word_list:
    #print('Printing the word: ', word.getString())

# function for calculating average word length of text - hashtags and mentions filtered out, i.e. only conventional words counted
def average_word_length(word_list):
    sum = 0
    for word in word_list:
        #print(word.getLength())
        sum += word.getLength()
    return sum/len(word_list)

#print('averge word length: ', average_word_length(word_list))

# function for calculating average word length of text - hashtags and mentions included in "words"
def average_word_length_hashtags_mentions(word_list, hashtags_list, mentions_list):
    total_tokens_list = word_list + hashtags_list + mentions_list
    sum = 0
    for word in total_tokens_list:
        #print(word.getLength())
        sum += word.getLength()
    return sum/len(total_tokens_list)

print('averge word length, hashtags and mentions included: ', average_word_length_hashtags_mentions(word_list, hashtags_list, mentions_list))

# function to calculate the percentage of words without vowel
def percentage_without_vowel(word_list):
    no_of_vowel_words = 0
    for word in word_list:
        #print(word.getString(), word.hasVowel())
        if word.hasVowel():
            no_of_vowel_words += 1
            #print(no_of_vowel_words)
    return (no_of_vowel_words/len(word_list))*100

#print('percentage word without vowel: ', percentage_without_vowel(word_list))

# function to calculate total number of balanced parentheses
def no_of_balanced_parantheses(no_of_left_parentheses, no_of_right_parentheses):
    difference = no_of_left_parentheses - no_of_right_parentheses
    if difference > 0:
        return no_of_right_parentheses
    elif difference < 0:
        return no_of_left_parentheses
    else:
        return no_of_left_parentheses

# function to calculate average number of punctuations per sentence
def average_no_punctuations(no_of_punctuations, no_of_sentences):
    return no_of_punctuations/no_of_sentences

print('average no of punct: ', average_no_punctuations(no_of_punctuations, no_of_sentences))


#print(no_of_balanced_parantheses(len(left_parentheses_list), len(right_parentheses_list)))

# function to calculate total number of quotations
def no_of_quotations(no_of_quotation_marks):
    if no_of_quotation_marks % 2 == 0:
        return int(no_of_quotation_marks/2)
    else:
        return int((no_of_quotation_marks-1)/2)

#print('number of quotes: ', no_of_quotations(len(quotation_mark_list)))

# function to calculate percentage of words written in caps
def all_caps_words(word_list):
    no_of_all_caps = 0
    for word in word_list:
        if word.subkind == 'allCaps':
            no_of_all_caps += 1
    return (no_of_all_caps/len(word_list)) * 100

#print(all_caps_words(word_list))

# function to calculate percentage of two consecutive punctuation marks
def two_punctuation_marks(punctuation_list, no_of_punctuations):
    if no_of_punctuations != 0:
        quantity = 0
        for token in punctuation_list:
            if token.getLength() == 2:
                quantity += 1
        return (quantity/no_of_punctuations) * 100
    else:
        return 'no punctuations in tweet'

print('percentage of two punct marks: ', two_punctuation_marks(other_punctuation_list, no_of_punctuations))

# function to calculate percentage of three or more consecutive punctuation marks
def three_punctuation_marks(punctuation_list, no_of_punctuations):
    if no_of_punctuations != 0:
        quantity = 0
        for token in punctuation_list:
            if token.getLength() > 2:
                quantity += 1
        print(quantity)
        print(no_of_punctuations)
        return (quantity/no_of_punctuations) * 100
    else:
        return 'no punctuations in tweet'

print('percentage of three punct marks: ', three_punctuation_marks(other_punctuation_list, no_of_punctuations))


