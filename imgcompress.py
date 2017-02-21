#!/usr/bin/python3

import tinify, argparse, os, settings
# change this to your tinypng api key
tinify.key = settings.TINIFY_API_KEY

# input arguments
input = argparse.ArgumentParser()
input.add_argument("-d", "--directory", type=str, help="\
        Specify the directory you want to save the images in, if not the current one.", required=False)
input.add_argument("-s", "--scale", type=int, help="\
        Scale proportionally to the specified width/height", required=False)
input.add_argument("file", help="The file/s you want to compress, separated by spaces.\
        Wildcards accepted.", nargs="+")
arguments = input.parse_args()

if arguments.directory != None:
    save_dir = arguments.directory
else:
    save_dir = "./"

if arguments.scale != None:
    scale_size = arguments.scale

# file type checking
'''
for file in arguments.file:
    ext = os.path.splitext(file)[1][1:].strip().lower()
    print(ext)  
    if ext != "jpg" or ext != "jpeg" or ext != "png":
        print(file + " is not a JPG or PNG. It has been removed.")
        arguments.file.remove(file)
'''
if len(arguments.file) == 0:
    raise ValueError("There are no images to process!")

for file in arguments.file:
    orig = tinify.from_file(file)
    if scale_size != None:
        resized = orig.resize(
                method="scale",
                width = scale_size
                )
        resized.to_file(save_dir + file)
        print(file + " has been compressed.")
    else:
        orig.to_file(save_dir + file)
        print(file + " has been compressed.")


