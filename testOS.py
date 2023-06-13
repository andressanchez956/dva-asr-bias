import os

path = "/Users/andressanchez/Dropbox/Mac/Desktop/participant_files/snippets/"

path += ""

filelist = []

for root, dirs, files in os.walk(path):
    for file in files:
        #append the file name to the list
        filelist.append(file)

sorted(filelist)

sorted(os.listdir(path))

