import utils
import os

def unique_words(path):
    unique_words = []

    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            if "DS" not in name:
                transcript = os.path.join(root, name)
                f = open(transcript, 'rt')
                text = f.read()
                f.close()

                unique_words_in_line = text.split()
                unique_words += unique_words_in_line

    return set(unique_words)

def all_words(path):
    all_words = []

    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            if "DS" not in name:
                transcript = os.path.join(root, name)
                f = open(transcript, 'rt')
                text = f.read()
                f.close()

                words_in_line = text.split()
                all_words += words_in_line

    return all_words

def main():
    machine_unique = unique_words("/Users/andressanchez/Dropbox/Mac/Desktop/machine_transcripts_clean")
    print(len(machine_unique))

    gt_words = all_words("/Users/andressanchez/Dropbox/Mac/Desktop/gt_transcripts_clean")
    print('gt', len(gt_words))

    words_in_vocab = 0
    for word in gt_words:
        if word in machine_unique:
            words_in_vocab += 1

    print(words_in_vocab)
    vocab_proportion = words_in_vocab / len(gt_words)

    print(vocab_proportion)

    print(len(set(gt_words)))

        
if __name__ == '__main__':
    main()