import os
import cv2

# Folder to convert images
path = "cropped_images"
# Folder to save converted images
save = "greyscale_images"
# student_id = "1141128675"

# Get address of current working directory
folder =  os.path.join(os.getcwd(), path)
# Gets all contents of the address of folder
filenames = os.listdir(folder)
# Folder to be saved into
save_folder = os.path.join(os.getcwd(), save)

# Iterates through imagetest
for filename in filenames:
    directories = os.path.join(folder, filename)
    directory = os.listdir(directories)
    
    # Iterates through the subdirectories in imagetest
    for image in directory:
        if image == 'desktop.ini':
            continue
            
        letter = image[9]
        save_foldernew = os.path.join(save_folder, letter)
        print("Currently at: ", image)

        # Reads the images in the subdirectories
        array_img = cv2.imread(os.path.join(directories, image))

        # Converts selected image to greyscale
        grey_img = cv2.cvtColor(array_img, cv2.COLOR_BGR2GRAY)

        cv2.imwrite(os.path.join(save_foldernew, image[:3] + '_grey_%s_%s.jpg' % (letter, image[11:21])), grey_img)

    