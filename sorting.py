import eel

import os
import tkinter
from tkinter import filedialog

# Constans with extensions of file types
VIDEO_EXTENSIONS = ['.mp4', '.mov', '.wmv', '.avi', '.avchd', '.flv', '.f4v', '.swf', '.mkv', '.webm',  '.html5', '.mpg', '.mpeg']
IMAGE_EXTENSIONS = ['.jpeg', '.jpg', '.png', '.pdf', '.gif', '.tiff', '.psd', '.ico', '.eps', '.ai',  '.indd', '.raw']
AUDIO_EXTENSIONS = ['.mp3', '.aac', '.ogg', '.flac', '.alac', '.wav', '.aiff', '.dsd', '.pcm']
DOCUMENT_EXTENSIONS = [ '.doc', '.docx', '.docm', '.xls', '.xlsx', '.ppt', '.pptx',  '.txt']

# Function for final sort and move files
def sort_lists(files, path):
    video_num, image_num, audio_num, document_num, other_num = 0, 0, 0, 0, 0
    result = 'Sorting Completed Successfully!\n'
    folder_list = []

    # Moving of files to folders
    for file in files:
        file_name, file_extension = os.path.splitext(file)
        file_old_path = path + '/' + file
        if file_extension in VIDEO_EXTENSIONS:
            file_new_path = path + '/Videos/'
            video_num += 1
        elif file_extension in IMAGE_EXTENSIONS:
            file_new_path = path + '/Images/'
            image_num += 1
        elif file_extension in AUDIO_EXTENSIONS:
            file_new_path = path + '/Audio/'
            audio_num += 1
        elif file_extension in DOCUMENT_EXTENSIONS:
            file_new_path = path + '/Documents/'
            document_num += 1
        else:
            file_new_path = path + '/Other/'
            other_num += 1
        # Check existence of folder
        if os.path.exists(file_new_path) == False:
            os.mkdir(file_new_path)
            folder_list.append(file_new_path)
        file_new_path = file_new_path + file
        os.rename(file_old_path, file_new_path)
    # Rename of existing folders by iteration
    for old_folder_path in folder_list:
        if old_folder_path == path + '/Videos/':
            new_folder_path = path + '/Videos - ' + str(video_num) + '/'
            result = result + 'Videos: ' + str(video_num) + '\n'
        if old_folder_path == path + '/Images/':
            new_folder_path = path + '/Images - ' + str(image_num) + '/'
            result = result + 'Images: ' + str(image_num) + '\n'
        if old_folder_path == path + '/Audio/':
            new_folder_path = path + '/Audio - ' + str(audio_num) + '/'
            result = result + 'Audio: ' + str(audio_num) + '\n'
        if old_folder_path == path + '/Documents/':
            new_folder_path = path + '/Documents - ' + str(document_num) + '/'
            result = result + 'Documents: ' + str(document_num) + '\n'
        if old_folder_path == path + '/Other/':
            new_folder_path = path + '/Other - ' + str(other_num) + '/'
            result = result + 'Other: ' + str(other_num) + '\n'
        os.rename(old_folder_path, new_folder_path)
    # Return results for js alert
    return result


def get_file_list(path):
    # List to store files
    file_list = []
    # Iterate directory by file, and get files to list "fileList"
    for file in os.listdir(path):
        # Check if current file is a file (not folder)
        if os.path.isfile(os.path.join(path, file)):
            file_list.append(file)
    return file_list


def open_folder_dialog():
    # Create window of explorer
    root = tkinter.Tk()
    root.iconbitmap('web\icon.ico')
    root.withdraw()
    # Without it explorer closes too fast
    root.wm_attributes('-topmost', 1)
    directory_path = filedialog.askdirectory()
    return directory_path


@eel.expose
def sort_function():
    path = open_folder_dialog()
    files = get_file_list(path)
    result = sort_lists(files, path)
    eel.ShowResult(result)
