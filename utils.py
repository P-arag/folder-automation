import os
import shutil
from os.path import *


def move_file(src: str, where: str) -> None:
    print("Moving %s to %s" % (src, where))
    # print(os.listdir(os.path.expanduser(where)))
    if check_if_exists(src, where):
        print(f"Oops, {src} file already exists in {where}")
        new_file_name = newname_if_present(src, where)
        # new_file_name = basename(new_file_name)
        print("mvfile " + new_file_name)
        shutil.move(src, join(expanduser(where), new_file_name))
    else:
        shutil.move(src, join(expanduser(where), basename(src)))
    # os.system("mv "+os.path.expanduser(src) + " " + os.path.expanduser(where))


def check_if_exists(filename: str, where: str) -> bool:
    # filename = basename(filename)
    # is_present = exists(join(where, filename))
    # print(is_present)
    # print(filename)
    # print(os.listdir(expanduser(where)))
    if basename(filename) in os.listdir(expanduser(where)):
        return True
    return False


def newname_if_present(filename: str, where: str) -> str:
    new_filename = filename
    i = 1
    while True:
        if check_if_exists(new_filename, where):
            filename_without_extension = splitext(new_filename)[0]
            extension = ""
            for xtension in splitext(new_filename)[1:]:
                extension += xtension

            new_filename = "%s(%d)%s" % (filename_without_extension, i, extension)
        else:
            print(new_filename)
            return basename(new_filename)
        i += 1
