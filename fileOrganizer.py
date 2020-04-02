'''
    - Create a script that monitors the desktop
    - Any time there is an update while the script is running, move files accordingly
        ex. if it's a .txt file, send it to the "text" subfolder
    - Script must run in the background
    - We want to leave apps and shortcuts as is
'''

import os

def main():
    pass

fileLookup = {
    # Programming languages extensions
    ".py": "C:",
    ".c": "",
    ".cpp": "",
    ".class": "",
    ".cs": "",
    ".h": "",
    ".java": "",
    ".pl": "",
    ".sh": "",
    ".swift": "",
    ".vb": "",
    '.xhtml':"",
    '.php': "",
    '.css': "",
    '.htm': "",
    '.html': "",
    '.js': "",
    '.jsp': "",

    # Audio file extensions
    ".aif": "",
    ".cda": "",
    ".mid": "",
    ".midi": "",
    ".mp3": "",
    ".mpa": "",
    ".ogg": "",
    ".wav": "",
    ".wma": "",
    ".wpl": "",

    # Image file extensions
    '.ai': "",
    '.bmp': "",
    '.gif': "",
    '.ico': "",
    '.jpeg': "",
    '.jpg': "",
    '.png': "",
    '.ps': "",
    '.psd': "",
    '.svg': "",
    '.tif': "",
    '.tiff': "",

    # Video file extensions 
    '.3g2': "",
    '.3gp': "",
    '.avi': "",
    '.flv': "",
    '.h264': "",
    '.m4v': "",
    '.mkv': "",
    '.mov': "",
    '.mp4': "",
    '.mpg': "",
    '.mpeg': "",
    '.rm': "",
    '.swf': "",
    '.vob': "",
    '.wmv': "",

    # Text file extensions
    '.doc': "",
    '.docx': "",
    '.odt': "",
    '.pdf': "",
    '.rtf': "",
    '.tex': "",
    '.txt': "",
    '.wpd': "",

    # Database file extensions
    '.csv': "",
    '.dat': "",
    '.db': "",
    '.dbf': "",
    '.log': "",
    '.mdb': "",
    '.sav': "",
    '.sql': "",
    '.tar': "",
    '.xml': "",

    # Executables
    '.apk': "",
    '.bat': "",
    '.com': "",
    '.exe': "",
    '.gadget': "",
    '.jar': "",
    '.msi': "",
    '.wsf': "",

    # Compressed file extensions
    '.7z': "",
    '.arj': "",
    '.deb': "",
    '.pkg': "",
    '.rar': "",
    '.rpm': "",
    '.tar.gz': "",
    '.z': "",
    '.zip': "",

    # Disc and media file extensions
    '.bin': "",
    '.dmg': "",
    '.iso': "",
    '.toast': "",
    '.vcd': "",

    # Internet file extensions
    '.asp': "",
    '.aspx': "",
    '.cer': "",
    '.cfm': "",
    '.part': "",
    '.rss': ""
}

if __name__ == '__main__':
    main()