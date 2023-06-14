import utils
import string
import re
from num2words import num2words

my_punctuation = string.punctuation.replace("'", "")

def clean_text(filename):
    # read file to memory
    file = open(filename, 'rt')
    text = file.read()
    file.close()
    print(filename, '\n\n\n')
    print(text, '\n\n\n')

    # find all numbers in text
    numbers = re.findall('\d+', text)
    # replace each number with words
    for num in numbers:
        text = re.sub(num, num2words(num), text)
    print(text, '\n\n\n')

    # lowercase
    text = text.lower()
    print(text, '\n\n\n')

    # remove all punctuation except apostrophe
    translating = str.maketrans('','', my_punctuation)
    text = text.translate(translating)
    print(text, '\n\n\n')

    

    # clean_file = open('/Users/andressanchez/Dropbox/Mac/Desktop/ama_transcripts_clean/' + name[5:8] + '/c_' + name,'w')

clean_text('/Users/andressanchez/Dropbox/Mac/Desktop/ama_transcripts_raw/101/ama_a101_3.txt')