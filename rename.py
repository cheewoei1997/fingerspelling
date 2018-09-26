import os

# Folder path
path = "original_images/Y"
# Letter
letter = "y"
# Student ID
stud_id = "1141128570"

# Get address of current working directory
folder =  os.path.join(os.getcwd(), path)
# Gets all contents of the address of folder
filenames = os.listdir(folder)
i = 0

for filename in filenames:
    # Replace everything in target directory with ordered namings
    os.rename(path + '/' + filename, path + '/' + filename.replace(filename, "%03d_orig_%s_%s.jpg" % (i, letter, stud_id)))    
    i += 1