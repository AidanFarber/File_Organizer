'''
    - Create a script that monitors the desktop
    - Any time there is an update while the script is running, move files accordingly
        ex. if it's a .txt file, send it to the "text" subfolder
    - Script must run in the background
    - We want to leave apps and shortcuts as is
    - Write the path to monitor and the base file path to write to in a file
'''
# import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# import sys
# import platform

path_to_monitor = ''
base_file_path = ''

# file_path_separator = ''
class DirectoryWatcher: 
    def __init__(self, monitorPath, basePath):
        self.path_to_monitor = monitorPath
        self.base_file_path = base_file_path
        self.event_observer = Observer()
        self.event_handler = FileSystemEventHandler()

    def main(self):
        # if 'Linux' in platform.platform() or 'Mac' in platform.platform():
        #     file_path_separator = '/'
        # elif 'Windows' in platform.platform():
        #     file_path_separator = '\\'
        # else:
        #     print('ERROR, UNKNOWN OS')
        with open('./settings.txt', 'w+') as file:
            for line in file:
                if 'Monitored Path:' in line:
                    path_to_monitor = line.strip('Monitored Path')
                if 'Output Path:' in line:
                    base_file_path = line.strip('Output Path:')

    def start(self):
        self.__schedule()
        self.event_observer.start()

    def stop(self):
        self.event_observer.stop()
        self.event_observer.join()

    def _check_extension(self):
        pass

    def __schedule(self):
        self.event_observer.schedule(self.event_handler, self.path_to_monitor, recursive=False)
    

            

    fileLookup = {
        # Programming languages extensions
        ".py": f"{base_file_path}",
        ".c": f"{base_file_path}",
        ".cpp": f"{base_file_path}",
        ".class": f"{base_file_path}",
        ".cs": f"{base_file_path}",
        ".h": f"{base_file_path}",
        ".java": f"{base_file_path}",
        ".pl": f"{base_file_path}",
        ".sh": f"{base_file_path}",
        ".swift": f"{base_file_path}",
        ".vb": f"{base_file_path}",
        '.xhtml':f"{base_file_path}",
        '.php': f"{base_file_path}",
        '.css': f"{base_file_path}",
        '.htm': f"{base_file_path}",
        '.html': f"{base_file_path}",
        '.js': f"{base_file_path}",
        '.jsp': f"{base_file_path}",

        # Audio file extensions
        ".aif": f"{base_file_path}",
        ".cda": f"{base_file_path}",
        ".mid": f"{base_file_path}",
        ".midi": f"{base_file_path}",
        ".mp3": f"{base_file_path}",
        ".mpa": f"{base_file_path}",
        ".ogg": f"{base_file_path}",
        ".wav": f"{base_file_path}",
        ".wma": f"{base_file_path}",
        ".wpl": f"{base_file_path}",

        # Image file extensions
        '.ai': f"{base_file_path}",
        '.bmp': f"{base_file_path}",
        '.gif': f"{base_file_path}",
        '.ico': f"{base_file_path}",
        '.jpeg': f"{base_file_path}",
        '.jpg': f"{base_file_path}",
        '.png': f"{base_file_path}",
        '.ps': f"{base_file_path}",
        '.psd': f"{base_file_path}",
        '.svg': f"{base_file_path}",
        '.tif': f"{base_file_path}",
        '.tiff': f"{base_file_path}",

        # Video file extensions 
        '.3g2': f"{base_file_path}",
        '.3gp': f"{base_file_path}",
        '.avi': f"{base_file_path}",
        '.flv': f"{base_file_path}",
        '.h264': f"{base_file_path}",
        '.m4v': f"{base_file_path}",
        '.mkv': f"{base_file_path}",
        '.mov': f"{base_file_path}",
        '.mp4': f"{base_file_path}",
        '.mpg': f"{base_file_path}",
        '.mpeg': f"{base_file_path}",
        '.rm': f"{base_file_path}",
        '.swf': f"{base_file_path}",
        '.vob': f"{base_file_path}",
        '.wmv': f"{base_file_path}",

        # Text file extensions
        '.doc': f"{base_file_path}",
        '.docx': f"{base_file_path}",
        '.odt': f"{base_file_path}",
        '.pdf': f"{base_file_path}",
        '.rtf': f"{base_file_path}",
        '.tex': f"{base_file_path}",
        '.txt': f"{base_file_path}",
        '.wpd': f"{base_file_path}",

        # Database file extensions
        '.csv': f"{base_file_path}",
        '.dat': f"{base_file_path}",
        '.db': f"{base_file_path}",
        '.dbf': f"{base_file_path}",
        '.log': f"{base_file_path}",
        '.mdb': f"{base_file_path}",
        '.sav': f"{base_file_path}",
        '.sql': f"{base_file_path}",
        '.tar': f"{base_file_path}",
        '.xml': f"{base_file_path}",

        # Executables
        '.apk': f"{base_file_path}",
        '.bat': f"{base_file_path}",
        '.com': f"{base_file_path}",
        '.exe': f"{base_file_path}",
        '.gadget': f"{base_file_path}",
        '.jar': f"{base_file_path}",
        '.msi': f"{base_file_path}",
        '.wsf': f"{base_file_path}",

        # Compressed file extensions
        '.7z': f"{base_file_path}",
        '.arj': f"{base_file_path}",
        '.deb': f"{base_file_path}",
        '.pkg': f"{base_file_path}",
        '.rar': f"{base_file_path}",
        '.rpm': f"{base_file_path}",
        '.tar.gz': f"{base_file_path}",
        '.z': f"{base_file_path}",
        '.zip': f"{base_file_path}",

        # Disc and media file extensions
        '.bin': f"{base_file_path}",
        '.dmg': f"{base_file_path}",
        '.iso': f"{base_file_path}",
        '.toast': f"{base_file_path}",
        '.vcd': f"{base_file_path}",

        # Internet file extensions
        '.asp': f"{base_file_path}",
        '.aspx': f"{base_file_path}",
        '.cer': f"{base_file_path}",
        '.cfm': f"{base_file_path}",
        '.part': f"{base_file_path}",
        '.rss': f"{base_file_path}"
    }

if __name__ == '__main__':
    main()