import os
lWithFiles = []
for path, currentDirectory, files in os.walk("/Users/maxhager/Projects2022"):
    for dir in currentDirectory:
        if dir.startswith("B"):
            lWithFiles.append(os.path.join(path, dir))
    for file, dir in files, currentDirectory:
        if file.startswith(typed) and file.endswith(".meta") == False and file.endswith(".mat") == False and file.endswith(".cs") == False:
            lWithFiles.append(os.path.join(path, file))

print(lWithFiles)