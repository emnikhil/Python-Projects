from zipfile import ZipFile

file_path = 'zip_file_path'
with ZipFile(file_path,"r") as zip_:
    #print the zip content
    zip_.printdir()

    #Extract the content
    zip_.extractall()