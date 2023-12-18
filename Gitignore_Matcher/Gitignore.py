import os


gitignore_Paths = []
all_Paths = []
all_Files = []
matches = []


root = "C:/Users/Anil/OneDrive/Desktop/Gitignore_Test"  # Root directory
f = open(root + "/.gitignore", "r")  # Gitignore file

count = sum(1 for line in f)

i = 0  # Count for lines
f = open(root + "/.gitignore", "r")
for x in f:
    i = i + 1
    if i == count:
        gitignore_Paths.append(x)  # Adds the last file name to the list
    else:
        gitignore_Paths.append(
            x[:-1]
        )  # Removes the newline and adds the file name to the list


# Grabs every file path and name from the directory
for path, subdirs, files in os.walk(
    root
):
    for name in files:
        all_Paths.append(path + "/" + name)
        all_Files.append(name)

for i in range(
    len(all_Paths)
):
    all_Paths[i] = all_Paths[i].replace("\\", "/")


for i in range(len(all_Files)):  # Finds the matches
    if all_Files[i] in gitignore_Paths:
        matches.append(all_Paths[i])


matches
