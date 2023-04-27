from os import listdir
from os.path import isdir, join


def walk_directory(d, indent):
    # Implement recursive directory walk here
    for f in listdir(d):
        print(indent, f)
        f_path = join(d, f)
        if isdir(f_path):
            walk_directory(f_path, 2 * indent)


# '.' means current directory
walk_directory('Desktop', ' ')
