import string
import re
from num2words import num2words
from jiwer import wer
import os


def get_file_names(path):
    #we shall store all the file names in this list
    filelist = []

    for root, dirs, files in os.walk(path):
        for file in files:
            #append the file name to the list if it's not a .DS_Store file
            if "DS" not in file:
                filelist.append(file)

    return sorted(filelist)


def clean_text(filename):
    # read file to memory
    file = open(filename, 'rt')
    text = file.read()
    file.close()

    # find all numbers in text
    numbers = re.findall('\d+', text)
    # replace each number with words
    for num in numbers:
        text = re.sub(num, num2words(num), text)

    # lowercase
    text = text.lower()

    # remove all punctuation except apostrophe
    my_punctuation = string.punctuation.replace("'", "")
    translating = str.maketrans('','', my_punctuation)
    text = text.translate(translating)

    # remove ums and uhs
    text = re.sub('( um )|( uh )', ' ', text)

    return text
    
    # clean_file = open('/Users/andressanchez/Dropbox/Mac/Desktop/ama_transcripts_clean/' + filename[5:8] + '/c_' + filename,'w')
    # clean_file.write(text)
    # clean_file.close()

def calc_wer(gt, mt):
    return wer(gt, mt)