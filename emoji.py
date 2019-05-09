import re
import smiley_dict as smiley
from emoji import UNICODE_EMOJI

# s = 'hej på dig 😊'
#
# print(s.replace('😊', ':-)'))

# get the codepoint number of a Unicode character

example_emoticon = 'Nu livetwittrar han igen! <3 <3 :-( :c :-b :( :-) :-( https://twitter.com/GayTenor/status/1080109863991152640 …'

example_emoji = 'Look at those itty-bitty steps 😍😭 ( woofwooftv)'

example_emoji2 = 'Bloomberg 2019 Healthiest Country Index: 1.🇪🇸Spain 2.🇮🇹Italy 3.🇮🇸Iceland 4.🇯🇵Japan 5.🇨🇭Switzerland 6.🇸🇪Sweden 7.🇦🇺Australia 8.🇸🇬Singapore 9.🇳🇴Norway 10.🇮🇱Israel 12.🇫🇷France 16.🇨🇦Canada 19.🇬🇧UK 23.🇩🇪Germany 35.🇺🇸US 37.🇶🇦Qatar 40.🇵🇱Poland 51.🇹🇷Turkey 52.🇨🇳China 53.🇲🇽Mexico'
example_emoji3 = 'Inför riksdagsvalet 2014 fick jag som näringsminister igenom en utredning om att ta bort den straffskatt som finns när familjeföretagare vill generationsskifta och sälja till sin familj. Idag röstade vi igenom det i riksdagen. 💪🏻🙌🏻 Ping: @foretagarna'
complex_example = 'Den 9 maj är det #Europadagen 🇪🇺 Jag kommer att prata om vår @Feministerna EU politik kl. 08.00 @Nyhetsmorgon ☀️ 📺 kl. 16.00 på Stockholm central 🚂 kl. 18.00 är det torgtal på Odenplan #EuropeNeedsFeminism #EUval2019'
complex_example2 = 'Om jag någon gång får chansen att gifta mig så ska jag fan i mig räknas som gift även på semestern och om jag flyttar utomlands. Så är det inte idag. Vi måste ställa krav på de andra EU-länderna! Utmärkt EU-valsförslag @socialdemokrat @strandhall 🌹🇪🇺♥️'
# string = '@Ygeman Gott Nytt År Anders!<f0><U+009F><U+008C><U+009F>'
#
# print(string)

# detect emoticons in tweet and return a list of positive and negative counts
def filter_emoticons(tweet):
    SMILEY = smiley.load_dict_smileys()
    words = tweet.split()
    print(words)
    list_of_emoticon_sentiment = [SMILEY[word] for word in words if word in SMILEY]
    print(list_of_emoticon_sentiment)
    num_pos_emoticons = 0
    num_neg_emoticons = 0
    for sentiment in list_of_emoticon_sentiment:
        if sentiment == 'positive':
            num_pos_emoticons += 1
        else:
            num_neg_emoticons += 1
    return num_pos_emoticons, num_neg_emoticons

# function to recognize emojis
def is_emoji(s):
    count = 0
    for emoji in UNICODE_EMOJI:
        count += s.count(emoji)
        if count > 1:
            return False
    return bool(count)



print(filter_emoticons(example_emoticon))

# list_of_words = example_emoji.split()
#
# print(list_of_words)
# for word in list_of_words:
#     letters = list(word)
#     print(letters)
#     for letter in letters:
#         #print(letter)
#         if is_emoji(letter):
#             print('found emoji')
#             print(letter)
# s = '😱'
# print(is_emoji(s))
# print('U+{:X}'.format(ord(s)))


# EMOJI TOKENIZER

# pattern match on emojis in string
#Emoji patterns
emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]", flags=re.UNICODE)

# -*- coding: UTF-8 -*-

def tokenize(data):
    list_of_emojis = []
    for match in emoji_pattern.finditer(data):
        # för varje matchning/träff som vi får mot tweeten, lägg in denna token i token list och lägg sedan in annotations i en motsvarande annotation list/set.
        token = match.group(0)
        print('printing token', token)
        list_of_emojis.append(token)
    return list_of_emojis

list_of_emojis = tokenize(example_emoji)

emoji_SentimentScores = {}

#happy, angry, love, sad, playful, confused
emoji_SentimentScores[b"\xF0\x9F\x98\x82"] = 0.221 #0.221*2
emoji_SentimentScores[b"\xF0\x9F\x98\xA1"] = -0.173 #-0.173
emoji_SentimentScores[b"\xe2\x9d\xa4"] = 0.746 #0.746*2
emoji_SentimentScores[b"\xF0\x9F\x98\xAD"] = -0.093 #-0.093*2
emoji_SentimentScores[b"\xF0\x9F\x98\x9C"] = 0.445 #0.445*2
emoji_SentimentScores[b"\xf0\x9f\x98\x95"] = -0.397 #0.397*2

print(emoji_SentimentScores)



def emoji_sentiment_score(emojis):
    sentiment_score = 0
    for emoji in emojis:
        print((emoji).encode('utf-8'))
        if (emoji).encode('utf-8') in emoji_SentimentScores.keys():
            print('found match')
            print('matched on: ', emoji)
            sentiment_score += emoji_SentimentScores[(emoji).encode('utf-8')]
    return sentiment_score

print(emoji_sentiment_score(list_of_emojis))
