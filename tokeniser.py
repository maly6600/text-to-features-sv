import nltk
import Token
import re
import text_reader as tr

example_tweet = "Allt färre vill begränsa rätten till abort i Sverige - idag bara 8 %! De politiker som ifrågasätter kvinnors rätt till sin kropp saknar folkligt stöd. #ståuppföraborträtten @hej"

def create_string(reg_expr_list):
    string = []
    for index, expr in enumerate(reg_expr_list):
        string.append(expr)
        if index != len(reg_expr_list)-1:
            string.append(r'|')
    result = ''.join(string)

    print('final re expr: ', result)
    return result

#uppercase = [A-Z]
#checking for word tokens
word_rules = r'''\b[a-ö](?:[a-ö]|-)*\b'''

# if using () then you create a group - if you do not want to capture this group specifically, use ?:

#using custom tokenizer in order to create objects/annotate at the same time as tokenizing is performed
regex_word = re.compile(word_rules)
print(regex_word)

reg_expr_list = tr.parse_txt_file()

# Set up the tokenizer using rules parsed from the text file
print(reg_expr_list)
reg_expr_string = create_string(reg_expr_list)

tokenizer_re = re.compile(r'''#(\w)+''')


print(tokenizer_re)
for match in tokenizer_re.finditer(example_tweet):
    # för varje matchning/träff som vi får mot tweeten, lägg in denna token i token list och lägg sedan in annotations i en motsvarande annotation list/set.
    print(match.group(0))

#checking for punctuation tokens
punctuation_rules = r'''\b[a-ö](?:[a-ö]|-)*\b'''


#using tokenizer provided by nltk
# token_list = nltk.regexp_tokenize(example_tweet, pattern)
# print (token_list)








