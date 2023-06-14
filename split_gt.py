import utils
import re
import string
import os

def split_gt(file, filename):
    # read file to memory
    f = open(file, 'rt')
    text = f.read()
    f.close()

    # remove time markers
    text = re.sub(' ?/30-\d+/ ?', ' ', text)

    # fix double spaces
    text = text.replace('  ', ' ')

    # split text by line
    text_lines = text.splitlines()

    for i, x in enumerate(text_lines):
        # if there's a captial letter
        if x in list(string.ascii_uppercase):
            # save next item (lowercased) as gt_snippet
            gt_snippet = text_lines[i+1].lower()
            # open and write that snippet to a text file in the right folder
            snippet_file = open('/Users/andressanchez/Dropbox/Mac/Desktop/gt_transcripts_clean/' + filename[:3] + '/' + x.lower() + filename[:5] + '.txt','w')
            snippet_file.write(gt_snippet)
            snippet_file.close()
    

def main():
    file_names = utils.get_file_names("/Users/andressanchez/Dropbox/Mac/Desktop/gt_transcripts_raw")

    for file in file_names:
        split_gt("/Users/andressanchez/Dropbox/Mac/Desktop/gt_transcripts_raw/" + file, file)
        print('split', file)


if __name__ == '__main__':
     main()