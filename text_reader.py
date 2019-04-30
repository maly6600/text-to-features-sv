import re

# with open('rules.txt') as file:
#     file_contents = file.read()
#     print(file_contents)

# set up regular expressions
# use https://regexper.com to visualise these if required
rx_dict = {
    'word': re.compile(r'(?P<initial>\w+)\s\((?P<second>\w+)\|(?P<third>\w+)\)(?P<quantifier>[+*]+)'),
    #'single_token': re.compile(r'(?P<initial>[^#\s]+)'),
}

def _parse_line(line):
    """
    Do a regex search against all defined regexes and
    return the key and match result of the first matching regex

    """

    for key, rx in rx_dict.items():
        match = rx.search(line)
        if match:
            return key, match
    # if there are no matches
    return None, None



def translate(expr):
    print('printing item to be translated: ', expr)
    if expr == 'UPPERCASE_LETTER':
        result = r'[A-Ö]'
        return result
    elif expr == 'LETTER':
        return r'[a-ö]'
    elif expr == 'DASH_PUNCTUATION':
        return r'-'
    elif expr == '*':
        return r'*'
    elif expr == 'SPACE_SEPARATOR':
        return r'\s'
    elif expr == 'LEFT_PARENTHESES':
        return r'('
    elif expr == 'RIGHT_PARENTHESIS':
        return r')'
    elif expr == 'SYMBOL':
        return r'\S'


reg_expr = []
def create_reg_expr_word(initial, second, third, quantifier):
    expr =  []
    expr.append(r'\b')
    arg_list = []
    translated_items_list = []
    arg_list.append(initial)
    arg_list.append(second)
    arg_list.append(third)
    arg_list.append(quantifier)

    for item in arg_list:
        translated_item = translate(item)
        translated_items_list.append(translated_item)
    print(expr)
    expr.append(translated_items_list[0])
    expr.append(r'(?:')
    expr.append(translated_items_list[1])
    expr.append(r'|')
    expr.append(translated_items_list[2])
    expr.append(r')')
    expr.append(translated_items_list[3])
    expr.append(r'\b')
    result  = ''.join(expr)
    print(result)
    reg_expr.append(result)

def create_reg_expr_single(initial):
    result = translate(initial)
    print(result)
    reg_expr.append(result)




def parse_txt_file():

    with open('rules.txt', 'r') as file_object:
        line = file_object.readline()

        while line:
            # at each line check for a match with a regex
            # key, match = _parse_line(line)
            key, match = _parse_line(line)

            if key == 'word':
                initial = match.group('initial')
                second = match.group('second')
                third = match.group('third')
                quantifier = match.group('quantifier')
                print(initial)
                print(second)
                print(third)
                print(quantifier)
                print(match.group(0))
                create_reg_expr_word(initial, second, third, quantifier)
            if key == 'single_token':
                initial = match.group('initial')
                print(initial)
                print(match.group(0))
                create_reg_expr_single(initial)

            line = file_object.readline()

        print(reg_expr)
        return reg_expr





