import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

DIR = "/home/pallav/Downloads/"


class OnMyWatch:
    watchDirectory = DIR

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(
            event_handler, self.watchDirectory, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("  Observer Stopped")

        self.observer.join()


def check_if_already_there(file_path, dest_dir):
    dest_dir = "/home/pallav/"+dest_dir
    fileNum = 1
    fileName = file_path.split("/")[-1]
    print(dest_dir+"/"+fileName)
    if os.path.exists(dest_dir+"/"+fileName):

        while True:
            if os.path.exists(f"{dest_dir}/{fileName}({fileNum})"):
                fileNum += 1
                print("Exists")
            else:
                fileNameArr = fileName.split(".")
                fileNameWithoutExten = fileNameArr[0]
                fileExten = fileNameArr[1]
                return f"{fileNameWithoutExten}{fileNum}.{fileExten}"
    else:
        return fileName


def commands(file_path, where):
    command_copy = "cp " + file_path + " " + "/home/pallav/" + where
    command_delete = "rm " + file_path
    return [command_copy, command_delete]


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            print("Watchdog received created event - % s." % event.src_path)

            if event.src_path.endswith(("jpg", "jpeg", "png", "gif")):
                print("Image Detected")
                time.sleep(2)
                fileName = check_if_already_there(event.src_path, "Pictures")
                print(fileName)
                os.rename(event.src_path, DIR+fileName)
                myCommands = commands(DIR+fileName, "Pictures")
                os.system(myCommands[0])
                os.system(myCommands[1])

            elif event.src_path.endswith(("docx", "txt", "pdf")):
                print("Document Detected")
                time.sleep(2)
                fileName = check_if_already_there(event.src_path, "Documents")
                print(fileName)
                os.rename(event.src_path, DIR+fileName)
                myCommands = commands(DIR+fileName, "Documents")
                os.system(myCommands[0])
                os.system(myCommands[1])

            elif event.src_path.endswith(("mp3", "wav")):
                print("Audio Detected")
                time.sleep(2)
                fileName = check_if_already_there(event.src_path, "Music")
                print(fileName)
                os.rename(event.src_path, DIR+fileName)
                myCommands = commands(DIR+fileName, "Music")
                os.system(myCommands[0])
                os.system(myCommands[1])

            elif event.src_path.endswith(("mp4", "avi", "mpv", "ogg")):
                print("Video Detected")
                time.sleep(2)
                fileName = check_if_already_there(event.src_path, "Videos")
                print(fileName)
                os.rename(event.src_path, DIR+fileName)
                myCommands = commands(DIR+fileName, "Videos")
                os.system(myCommands[0])
                os.system(myCommands[1])

            elif event.src_path.endswith(("py", "json", "js", "c", "cs", "cpp", "java", "go")):
                print("Code Detected")
                time.sleep(2)
                fileName = check_if_already_there(event.src_path, "Code")
                print(fileName)
                os.rename(event.src_path, DIR+fileName)
                myCommands = commands(DIR+fileName, "Code")
                os.system(myCommands[0])
                os.system(myCommands[1])

            elif event.src_path.endswith(("zip")):
                print("Folders Detected")
                time.sleep(100)
                fileName = check_if_already_there(event.src_path, "Public")
                print(fileName)
                os.rename(event.src_path, DIR+fileName)
                myCommands = commands(DIR+fileName, "Public")
                os.system(myCommands[0])
                os.system(myCommands[1])
            elif event.src_path.endswith(("tar", "gz", "tar.gz", "deb")):
                print("Large Files Detected, Not Doing anything")

            else:
                print("Unknown Files Detected")
                print(fileName)
                os.rename(event.src_path, DIR+fileName)
                time.sleep(20)
                fileName = check_if_already_there(event.src_path, "Etc")
                myCommands = commands(DIR+fileName, "Etc")
                os.system(myCommands[0])
                os.system(myCommands[1])


if __name__ == '__main__':
    watch = OnMyWatch()
    print(f"Watchdog watching {DIR}")
    watch.run()
