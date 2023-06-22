import pandas as pd
import utils
from jiwer import wer
import audioread

# file_names = utils.get_file_names("/Users/andressanchez/Dropbox/Mac/Desktop/ama_transcripts_raw")
# for name in file_names:
#     utils.clean_text("/Users/andressanchez/Dropbox/Mac/Desktop/ama_transcripts_raw/" + name[5:8] + "/" + name, name)
#     print('finished', name)

def calc_wer(gt_file, filename, machine_file, task):
    f = open(gt_file, 'rt')
    ground_truth = f.read()
    f.close()

    f = open(machine_file, 'rt')
    machine_gen = f.read()
    f.close()

    return wer(ground_truth, machine_gen)

def make_row_list(gt_file, filename):
    row_list = [filename]

    participant = filename[1:4]
    row_list.append(participant)

    task = filename[5]
    if task == "2":
        task = filename[5:7]
    row_list.append(task)

    for company in ["ama", "ggl"]:
        machine_file = "/Users/andressanchez/Dropbox/Mac/Desktop/machine_transcripts_clean/" + company + "/" + participant + "/c_" + company + "_" + filename 
        error = calc_wer(gt_file, filename, machine_file, task)
        row_list.append(error)

    return row_list

def main():
    file_names = utils.get_file_names("/Users/andressanchez/Dropbox/Mac/Desktop/gt_transcripts_clean")
    # file_names = ['s101_2h.txt', 'l101_4.txt', 's101_1.txt', 's101_2s.txt']

    rows = []
    for filename in file_names:
        participant = filename[1:4]
        row = make_row_list("/Users/andressanchez/Dropbox/Mac/Desktop/gt_transcripts_clean/" + participant + "/" + filename, filename)
        rows.append(row)
    
    df = pd.DataFrame(rows, columns=['file', 'participant', 'task', 'amazon_wer', 'google_wer'])
    df.to_csv('/Users/andressanchez/Dropbox/Mac/Desktop/machine_wer.csv', index=False)
        
if __name__ == '__main__':
    main()

