'''
The tool should sort the files on Desktop on the basis of file extension and move them in
separate folders in Documents folder.

Example: If there are 10 MP3 files, 3 word documents, 4 PDFs then in Documents Folder three
folders should be created with name MP3, DOC and PDF and all the files on the Desktop should
be moved into these directories based on their file type or extension. Desktop should be cleaned
but dont remove shortcuts of My Computer, Chrome or even Counter strike.
'''


import os
import shutil

# Give the path for the desktop
filePath = r"C:\Users\MANISH\Desktop"


# List to store all the file names
filenames = os.listdir(filePath)

# Dictionary to store different file types
fileTypes = {}

for file in filenames:
    filename, file_extension = os.path.splitext(file)
    if (file_extension[1:len(file_extension)].lower()!='lnk') & (file_extension[1:len(file_extension)].lower()!='url'):
        if(file_extension[1:].lower()=='mp4') | (file_extension[1:].lower()=='mkv') | (file_extension[1:].lower()=='3gp') | (file_extension[1:].lower()=='flv') | (file_extension[1:].lower()=='wmv') | (file_extension[1:].lower()=='mov'):
            fileTypes[file_extension.lower()] = 'Videos'
            
        if(file_extension[1:].lower()=='mp3') | (file_extension[1:].lower()=='m3u') | (file_extension[1:].lower()=='m4a') | (file_extension[1:].lower()=='mpa') | (file_extension[1:].lower()=='wav'):
            fileTypes[file_extension.lower()] = 'Audios'
            
        if(file_extension[1:].lower()=='pdf') | (file_extension[1:].lower()=='pct') | (file_extension[1:].lower()=='indd') | (file_extension[1:].lower()=='qxd') | (file_extension[1:].lower()=='qxp') | (file_extension[1:].lower()=='rels'):
            fileTypes[file_extension.lower()] = 'PDF FILES'
            
        if(file_extension[1:].lower()=='docx') | (file_extension[1:].lower()=='doc') | (file_extension[1:].lower()=='msg') | (file_extension[1:].lower()=='txt') | (file_extension[1:].lower()=='wps'):
            fileTypes[file_extension.lower()] = 'DOCX FILES'
            
        if(file_extension[1:].lower()=='pptx'):
            fileTypes[file_extension.lower()] = 'PPTs'
            
        if(file_extension[1:].lower()=='jpg') | (file_extension[1:].lower()=='bmp') | (file_extension[1:].lower()=='png') | (file_extension[1:].lower()=='gif') | (file_extension[1:].lower()=='thm') | (file_extension[1:].lower()=='tif'):
            fileTypes[file_extension.lower()] = 'Images'
            
    

# Make folders for different extensions

for keys, values in fileTypes.items():
    file_path = filePath + str('/') + fileTypes[keys]
    directory = os.path.dirname(file_path)
    
    if not os.path.exists(file_path):
        os.mkdir(file_path)


# Move the files into folders

for file in filenames:
    filename, file_extension = os.path.splitext(file)
    if (file_extension[1:len(file_extension)].lower()!='lnk') & (file_extension[1:len(file_extension)].lower()!='url') & (file_extension[1:len(file_extension)].lower()!=''):
        file_extension = file_extension.lower()
        src_path = filePath + str('/') + file
        dest_path = filePath + str('/') + fileTypes[file_extension] + str('/') + file
        
        if not os.path.isfile(dest_path):
            os.rename(src_path, dest_path)
        
    