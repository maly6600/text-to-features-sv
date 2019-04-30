import new_tokenizer as nt
import Token

example_tweet1 = 'Allt färre vill begränsa rätten till abort i Sverige - idag bara 8 %!!! De politiker som ifrågasätter "kvinnors rätt" till sin kropp "eu19" saknar folkligt stöd. #ståuppföraborträtten @hej (;-)) (GRR) brr'

example_tweet2 = "Deltog idag på bokmässan och svarade på många intressanta frågor och funderingar under årets kampanj #FrågaEnMuslim #svenskabokmässan #svpol #islam HEJ"

word_list, left_parentheses_list, right_parentheses_list, quotation_mark_list = nt.tokenize(example_tweet1)

for word in word_list:
    print('Printing the word: ', word.getString())

def average_word_length(word_list):
    sum = 0
    for word in word_list:
        print(word.getLength())
        sum += word.getLength()
    return sum/len(word_list)

print('averge word length: ', average_word_length(word_list))

# function to calculate the percentage of words without vowel
def percentage_without_vowel(word_list):
    no_of_vowel_words = 0
    for word in word_list:
        #print(word.getString(), word.hasVowel())
        if word.hasVowel():
            no_of_vowel_words += 1
            #print(no_of_vowel_words)
    return (no_of_vowel_words/len(word_list))*100

print('percentage word without vowel: ', percentage_without_vowel(word_list))

# function to calculate total number of balanced parentheses
def no_of_balanced_parantheses(no_of_left_parentheses, no_of_right_parentheses):
    difference = no_of_left_parentheses - no_of_right_parentheses
    if difference > 0:
        return no_of_right_parentheses
    elif difference < 0:
        return no_of_left_parentheses
    else:
        return no_of_left_parentheses


print(no_of_balanced_parantheses(len(left_parentheses_list), len(right_parentheses_list)))

# function to calculate total number of quotations
def no_of_quotations(no_of_quotation_marks):
    if no_of_quotation_marks % 2 == 0:
        return int(no_of_quotation_marks/2)
    else:
        return int((no_of_quotation_marks-1)/2)

print('number of quotes: ', no_of_quotations(len(quotation_mark_list)))