def get_file_names():
    path ="/Users/andressanchez/Dropbox/Mac/Desktop/participant_files/snippets"
    #we shall store all the file names in this list
    filelist = []

    for root, dirs, files in os.walk(path):
        for file in files:
            #append the file name to the list
            if "DS" not in file:
                filelist.append(file)

    return sorted(filelist)