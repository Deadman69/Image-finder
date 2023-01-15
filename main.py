from PIL import Image
import imagehash
import os  
import glob

imagesFolder = "C:/myfolder/folder A"
imagesToCompareFolder = "C:/Users/test/folderB"

listHashsImages = []
listHashsImagesCompare = []

def getRealHash(path):
    hashCalc = imagehash.average_hash(Image.open(path))
    return str(hashCalc)

for filename in glob.iglob(imagesFolder + '**/**', recursive=True):
    if(not os.path.isdir(filename) and ('.png' in filename or '.PNG' in filename or '.jpg' in filename or '.JPG' in filename)):
        objCreated = {'hashCalc': getRealHash(filename), 'filename': filename}
        listHashsImages.append(objCreated)

for filename in glob.iglob(imagesToCompareFolder + '**/**', recursive=True):
    if(not os.path.isdir(filename) and ('.png' in filename or '.PNG' in filename or '.jpg' in filename or '.JPG' in filename)):
        objCreated = {'hashCalc': getRealHash(filename), 'filename': filename}
        listHashsImagesCompare.append(objCreated)

print("====================================")
print("Hash calc ended, start comparing...")
print("====================================")

matchFiles = 0
for file in listHashsImagesCompare:
    for file2 in listHashsImages:
        if(file['hashCalc'] == file2['hashCalc']):
            matchFiles = matchFiles + 1
            print("Same hash found for " + file['filename'] + " (" + file2["filename"] + ")")

if(matchFiles == 0):
    print("We haven't found any files in folder '" + imagesToCompareFolder + "' matching elements in '" + imagesFolder + "'")

input("\npress a key to exit")
