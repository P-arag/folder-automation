import os
import json
import time
from pprint import pprint
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from utils import *


class OnMyWatch:
    def __init__(self, watch_directory):
        self.observer = Observer()
        self.watch_directory = os.path.expanduser(watch_directory)
        print(f"WatchDog Watching {self.watch_directory}")

    def run(self):
        event_handler = Handler()
        self.observer.schedule(
            event_handler, self.watch_directory, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("  Observer Stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        print(event.event_type+" "+event.src_path)

        if event.is_directory:
            return None
        elif event.event_type == 'created':
            print("*created "+event.src_path)
            for folder_iterable in data["move_folders"]:
                extensions = ["." + extension for extension in folder_iterable["Xtensions"]]
                if event.src_path.endswith(tuple(extensions)):
                    print(folder_iterable["print_text"])
                    if folder_iterable["move_this_file?"]:
                        time.sleep(folder_iterable["sleep"])
                        move_file(event.src_path, folder_iterable["location"])
                        print("moved")
                        print(os.listdir(os.path.expanduser(folder_iterable["location"])))
                        break
                    else:
                        print(folder_iterable["print_text"])
                        break



if __name__ == '__main__':
    data = json.load(open("./config.json"))
    watch = OnMyWatch(data["watch_directory"])
    watch.run()
