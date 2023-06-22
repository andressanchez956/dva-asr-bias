import utils
import audioread

path = "/Users/andressanchez/Dropbox/Mac/Desktop/participant_files/snippets"
file_names = utils.get_file_names(path)

times = []
for name in file_names:
    if name[0] != "s":
        audio = path + '/s' + name[1:4] + '/s' + name[1:6] + '/' + name
    else:
        audio = path + '/' + name[:4] + '/' + name

    with audioread.audio_open(audio) as f:
        totalsec = f.duration
        times.append(totalsec)

print(max(times))
print(min(times))
print(sum(times))