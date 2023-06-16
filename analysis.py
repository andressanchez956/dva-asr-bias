import utils

file_names = utils.get_file_names("/Users/andressanchez/Dropbox/Mac/Desktop/ggl_transcripts_raw")
# file_names = ['ggl_l101_4.txt', 'ggl_s101_1.txt', 'ggl_s101_2h.txt', 'ggl_s101_2s.txt']

for name in file_names:
    utils.clean_text("/Users/andressanchez/Dropbox/Mac/Desktop/ggl_transcripts_raw/" + name[5:8] + "/" + name, name)

