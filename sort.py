import os
import tkinter
import tkinter.filedialog as filedialog


class Sort:
    
    def __init__(self, save_path):
        
        self.save_path = save_path
        # Constans with extensions of file types
        self.VIDEO_EXTENSIONS = ['.mp4', '.mov', '.wmv', '.avi', '.avchd', '.flv', '.f4v', '.swf', '.mkv', '.webm',  '.html5', '.mpg', '.mpeg']
        self.IMAGE_EXTENSIONS = ['.jpeg', '.jpg', '.png', '.pdf', '.webp', '.gif', '.tiff', '.psd', '.ico', '.eps', '.ai',  '.indd', '.raw']
        self.AUDIO_EXTENSIONS = ['.mp3', '.aac', '.ogg', '.flac', '.alac', '.wav', '.aiff', '.dsd', '.pcm']
        self.DOCUMENT_EXTENSIONS = [ '.doc', '.docx', '.docm', '.xls', '.xlsx', '.ppt', '.pptx',  '.txt']

    # Function for final sort and move files
    def sort_lists(self, files, path):
        self.video_num, self.image_num, self.audio_num, self.document_num, self.other_num = 0, 0, 0, 0, 0
        self.result = 'Sorting Completed Successfully!\n'
        self.folder_list = []

        # Moving of files to folders with default name
        for file in files:
            file_name, file_extension = os.path.splitext(file)
            self.file_old_path = path + '/' + file

            if file_extension in self.VIDEO_EXTENSIONS:
                self.file_new_path = path + '/Videos/'
                self.video_num += 1
            elif file_extension in self.IMAGE_EXTENSIONS:
                self.file_new_path = path + '/Images/'
                self.image_num += 1
            elif file_extension in self.AUDIO_EXTENSIONS:
                self.file_new_path = path + '/Audio/'
                self.audio_num += 1
            elif file_extension in self.DOCUMENT_EXTENSIONS:
                self.file_new_path = path + '/Documents/'
                self.document_num += 1
            else:
                self.file_new_path = path + '/Other/'
                self.other_num += 1
            # Check existence of folder
            if os.path.exists(self.file_new_path) == False:
                os.mkdir(self.file_new_path)
                self.folder_list.append(self.file_new_path)
            self.file_new_path = self.file_new_path + file
            os.rename(self.file_old_path, self.file_new_path)


        # Rename of existing folders by iteration
        for old_folder_path in self.folder_list:
            # Videos renaming
            if old_folder_path == path + '/Videos/':
                self.new_folder_path = path + '/Videos - ' + str(self.video_num) + '/'
                self.result = self.result + 'Videos: ' + str(self.video_num) + '\n'
            # Images renaming
            if old_folder_path == path + '/Images/':
                self.new_folder_path = path + '/Images - ' + str(self.image_num) + '/'
                self.result = self.result + 'Images: ' + str(self.image_num) + '\n'
            # Audio renaming
            if old_folder_path == path + '/Audio/':
                self.new_folder_path = path + '/Audio - ' + str(self.audio_num) + '/'
                self.result = self.result + 'Audio: ' + str(self.audio_num) + '\n'
            # Documents renaming
            if old_folder_path == path + '/Documents/':
                self.new_folder_path = path + '/Documents - ' + str(self.document_num) + '/'
                self.result = self.result + 'Documents: ' + str(self.document_num) + '\n'
            # Other renaming
            if old_folder_path == path + '/Other/':
                self.new_folder_path = path + '/Other - ' + str(self.other_num) + '/'
                self.result = self.result + 'Other: ' + str(self.other_num) + '\n'
            os.rename(old_folder_path, self.new_folder_path)
        # Return results
        return self.result


    def get_file_list(self, path):
        # List to store files
        self.file_list = []
        # Iterate directory by file, and get files to list "fileList"
        for file in os.listdir(path):
            # Check if current file is a file (not folder)
            if os.path.isfile(os.path.join(path, file)):
                self.file_list.append(file)
        return self.file_list

    def sort_function(self):
        files = self.get_file_list(self.save_path)
        result = self.sort_lists(files, self.save_path)
        return result