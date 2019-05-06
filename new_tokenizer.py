import re
import Token as Token

example_tweet2 = "Deltog idag på bokmässan och svarade på många intressanta frågor och funderingar under årets kampanj #FrågaEnMuslim #svenskabokmässan #svpol #islam HEJ"

tokenizer_re = re.compile(r'''
@\w+ # mentions
|
\#(\w)+ # hashtags
|
\b[A-ZÅÄÖ](?:[A-ZÅÄÖ]|-)*\b|[A-ZÅÄÖa-zåäö](?:[A-ZÅÄÖa-zåäö]|-)* # words (all caps or other)
|
[0-9]+
|
[()] # left or right parenthesis
|
[".,;:?!-]+ # punctuation or quotation mark
|
\S# non-space character
''', re.VERBOSE)

word_list = []
left_parentheses_list = []
right_parentheses_list = []
quotation_mark_list = []
other_punctuation_list = []

def tokenize(data):
    for match in tokenizer_re.finditer(data):
        # för varje matchning/träff som vi får mot tweeten, lägg in denna token i token list och lägg sedan in annotations i en motsvarande annotation list/set.
        token = match.group(0)
        print(token)
        # annotate - match token against reg expr and create a token object for each token and set attr for the object depending on what reg expr it matched against
        if re.match(r'''\b[B-DF-HJ-NP-TVXZ](?:[B-DF-HJ-NP-TVXZ]|-)*\b''', token): # if token is ALL CAPS w/o vowel
            print('Matches against all caps w/o vowel')
            word_list.append(Token.Token(token, 'word', len(token), 'allCaps', False))
        elif re.match(r'''\b[A-ZÅÄÖ](?:[A-ZÅÄÖ]|-)*\b''', token): # if token is ALL CAPS with vowel
            print('Matches against caps with vowel')
            word_list.append(Token.Token(token, 'word', len(token), 'allCaps', True))
        elif re.match(r'''\b[B-DF-HJ-NP-TVXZb-df-hj-np-tvxz]([B-DF-HJ-NP-TVXZb-df-hj-np-tvxz]|-)*\b''', token):  # if token is a word w/o vowel
            print('Matches against \word w/o vowel')
            word_list.append(Token.Token(token, 'word', len(token), None, False))
        elif re.match(r'''\b[A-ZÅÄÖa-zåäö](?:[A-ZÅÄÖa-zåäö]|-)*\b''', token):  # if token is a word with vowel
            print('Matches against word with vowel')
            word_list.append(Token.Token(token, 'word', len(token), None, True))
        elif re.match(r'''^#[A-ZÅÄÖa-zåäö0-9_]+''', token):  # if token is a hashtag (åäö allowed)
            print('Matches against hashtag')
            new_token_object = Token.Token(token, 'Twitter', len(token), 'hashtag', None)
        elif re.match(r'''^@\w+''', token):  # if token is a mention (åäö not allowed for Twitter username)
            print('Matches against mention')
            new_token_object = Token.Token(token, 'Twitter', len(token), 'mention', None)
        elif re.match(r'''\(''', token):  # if token is a left parenthesis
            print('Matches against left parenthesis')
            left_parentheses_list.append(Token.Token(token, 'leftParenthesis', len(token), None, None))
        elif re.match(r'''\)''', token):  # if token is a right parenthesis
            print('Matches against right parenthesis')
            right_parentheses_list.append(Token.Token(token, 'rightParenthesis', len(token), None, None))
        elif re.match(r'''\"''', token):  # if token is a quotation mark
            print('Matches against quotation mark')
            quotation_mark_list.append(Token.Token(token, 'quotation', len(token), None, None))
        elif re.match(r'''[-_!?,.:;]+''', token):  # if token consists of puncutation
            print('Matches against punctuation')
            other_punctuation_list.append(Token.Token(token, 'punctuation', len(token), None, None))
        elif re.match(r'''[0-9]+''', token):  # if token is a combination of digits
            print('Matches against number')
            new_token_object = Token.Token(token, 'number', len(token), None, None)
        else:
            print('Matches against symbol')
            new_token_object = Token.Token(token, 'symbol', len(token), None, None)
        #print(new_token_object.getLength())
    return word_list, left_parentheses_list, right_parentheses_list, quotation_mark_list, other_punctuation_list


#list = tokenize(example_tweet2)



