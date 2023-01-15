# Image-finder
This python3 tool allows you to check if images in folder A is present in folder B.
It's not based on image file hash like md5 or sha1 but on image real content as sometime you get the same image but the hashs are not equals.

## Tests
It has been tested on python 3.11.1

## Usage
`pip install imagehash`  
`pip install Pillow` (may be needed on some installations)

Then change the parameters `imagesFolder` & `imagesToCompareFolder` with the 2 folders you would like to test (don't use trailing `/` and use only `/` and not `\` as on some systems it seems to not work)
Once it's done, run the program and you should get an output similar to :
```
====================================
Hash calc ended, start comparing...
====================================
Same hash found for C:/Users/testUser/Downloads/TestFolder\Test\duplicatedfile.png (C:/Users/anotherUser/OneDrive\Pictures\Screenshots\File1.png)

press a key to exit
```
If there is no file matching, you will get a message specifiying it to you

### Test environment
Python 3.11.1 packages :
```
Package                   Version
------------------------- ---------
altgraph                  0.17.3
future                    0.18.3
ImageHash                 4.3.1
numpy                     1.24.1
pefile                    2022.5.30
Pillow                    9.4.0
pip                       22.3.1
pyinstaller               5.7.0
pyinstaller-hooks-contrib 2022.15
PyWavelets                1.4.1
pywin32-ctypes            0.2.0
scipy                     1.10.0
setuptools                65.5.0
```
