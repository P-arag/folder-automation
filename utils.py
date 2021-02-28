import os
import shutil


def move_file(src: str, where: str) -> None:
    print("Moving %s to %s" % (src, where))
    print(os.listdir(os.path.expanduser(where)))
    if check_if_exists(src, where):
        print(f"Oops, {src} file already exists in {where}")
        new_file_name = rename_if_present(src, where)
        os.rename(src, new_file_name)
        shutil.move(new_file_name, os.path.expanduser(where))
        os.remove(os.path.expanduser(new_file_name))
    else:
        shutil.move(src, os.path.expanduser(where))
        os.system(f"rm {os.path.expanduser(src)}")


def check_if_exists(filename: str, where: str) -> bool:
    filename = os.path.splitext(filename)[-1]
    is_present = os.path.exists(os.path.join(where, filename))
    print(is_present)
    print(os.listdir(os.path.expanduser(where)))
    return is_present


def rename_if_present(filename: str, where: str) -> str:
    new_filename = filename
    i = 0
    while True:
        if check_if_exists(new_filename, where):
            filename_without_extension = os.path.splitext(new_filename)[0]
            extension = ""
            for xtension in os.path.splitext(new_filename)[1:]:
                extension += xtension

            new_filename = "%s(%d)%s" % (filename_without_extension, i, extension)
        else:
            print(new_filename)
            return new_filename
        i += 1
