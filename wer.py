import pandas as pd
import utils
from jiwer import wer
import audioread

# file_names = utils.get_file_names("/Users/andressanchez/Dropbox/Mac/Desktop/ama_transcripts_raw")
# for name in file_names:
#     utils.clean_text("/Users/andressanchez/Dropbox/Mac/Desktop/ama_transcripts_raw/" + name[5:8] + "/" + name, name)
#     print('finished', name)

def calc_wer(file, filename, task):
    f = open(file, 'rt')
    machine_gen = f.read()
    f.close()

    if task == '1' or task == '2':
        gt_file = "/Users/andressanchez/Dropbox/Mac/Desktop/gt_transcripts_clean/task_" + task + ".txt"
    else:
        gt_file = "/Users/andressanchez/Dropbox/Mac/Desktop/gt_transcripts_clean/" + filename[7:10] + "/" + filename[6:]

    f = open(gt_file, 'rt')
    ground_truth = f.read()
    f.close()

    return wer(ground_truth, machine_gen)

def make_row_list(file, filename):
    row_list = [filename]

    participant = filename[7:10]
    row_list.append(participant)

    task = filename[11]
    if task == 2:
        task = filename[11:13]
    row_list.append(task)

    error = calc_wer(file, filename, task)
    row_list.append(error)

    return row_list

def main():
    file_names = utils.get_file_names("/Users/andressanchez/Dropbox/Mac/Desktop/machine_transcripts_clean")
    # file_names = ['c_ama_l101_4.txt', 'c_ama_s101_1.txt', 'c_ama_s101_2h.txt', 'c_ama_s101_2s.txt']

    rows = []
    for name in file_names:
        company = name[2:5]
        row = make_row_list("/Users/andressanchez/Dropbox/Mac/Desktop/ggl_transcripts_clean/" + name[7:10] + "/" + name, name)
        rows.append(row)
    
    df = pd.DataFrame(rows, columns=['file', 'participant', 'task', 'WER'])
    df.to_csv('/Users/andressanchez/Dropbox/Mac/Desktop/ggl_wer.csv', index=False)
        
if __name__ == '__main__':
    main()

