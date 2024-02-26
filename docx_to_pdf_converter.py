

import pathlib as p
import docx2pdf

#set a sourcefile with the docx inside it
src = r".\test_target"
#set a destination folder for the pdfs
destination = r".\test_destination"

#doc conversion function
def convert_file(filenameInput, filenameOutput):
    docx2pdf.convert(filenameInput, filenameOutput)

#obtain list of all OSCE checklist paths and names in dict
targets = {}
for docfile in p.Path(src).glob("**/*"):
    print(docfile)
    if str(docfile)[-4:] =="docx":
        path_to_file = p.Path(docfile)
        targets[path_to_file.name[:-5]] = path_to_file
    else:
        continue

#do the conversion
for name in targets:
    old_path = targets[name]
    course_name = old_path.parent.name
    new_path = destination + '\\' +course_name +'_' + name + ".pdf"
    convert_file(old_path, new_path)