import tkinter
import customtkinter
import service
from service import DataInput
from sort import Sort
from video_downloader import Video
from image_downloader import Image

customtkinter.set_appearance_mode('System')  # Modes: 'System' (standard), 'Dark', 'Light'
customtkinter.set_default_color_theme('dark-blue')  # Themes: 'blue' (standard), 'green', 'dark-blue'


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Window
        self.title('Oklahoma')
        self.geometry(f'{345}x{260}')
        self.minsize(345, 260)
        self.maxsize(345, 260)

        # Grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        # Label
        self.logo_label = customtkinter.CTkLabel(master=self, text='Oklahoma', justify='center', width=200, font=customtkinter.CTkFont(size=20, weight='bold'))
        self.logo_label.grid(row=0, column=0, padx=70, pady=10)
        # Widgets for Left Sidebar
        self.button_sort = customtkinter.CTkButton(master=self, width=200, command=self.sort_button_event)
        self.button_sort.grid(row=1, column=0, padx=70, pady=5)

        self.button_download_video = customtkinter.CTkButton(master=self, width=200, command=self.download_video_button_event)
        self.button_download_video.grid(row=2, column=0, padx=70, pady=5)

        self.button_download_image = customtkinter.CTkButton(master=self, width=200, command=self.download_image_button_event)
        self.button_download_image.grid(row=3, column=0, padx=70, pady=5)

        self.button_select_path = customtkinter.CTkButton(master=self, width=200, command=self.select_path_event)
        self.button_select_path.grid(row=4, column=0, padx=70, pady=5)

        self.path_label = customtkinter.CTkLabel(master=self, text='', justify='center', width=200, font=customtkinter.CTkFont(size=11, weight='bold'))
        self.path_label.grid(row=5, column=0, padx=70, pady=10)

        # set default values
        self.button_sort.configure(state='active', text='Sort Files in Folder')
        self.button_download_video.configure(state='active', text='Download Video',)
        self.button_download_image.configure(state='active', text='Download Image')
        self.button_select_path.configure(state='active', text='Select save folder')

    def save_path_setter(self, save_path):
        self.save_path = save_path

    def save_path_getter(self):
        return self.save_path
    
    def path_error(self):
        self.path_label.configure(text='You need to select right folder!')

    def sort_button_event(self):
        try:
            sort_object = Sort(self.save_path)
            sort_object.sort_function()
        except:
            self.path_error()

    def download_video_button_event(self):
        try:
            video_data_input = DataInput('Input Video URL:', 'URL Input Dialog')
            video_link = video_data_input.dialog()
            new_video = Video(self.save_path, video_link)
            new_video.download_video()
        except:
            self.path_error()

    def download_image_button_event(self):
        try:
            image_data_input = DataInput('Input image URL:', 'URL Input Dialog')
            image_url = image_data_input.dialog()
            new_image = Image(self.save_path, image_url)
            new_image.download_image()
        except:
            self.path_error()
    
    def change_path_label(self):
        self.path_text = service.check_text_size(self.save_path)
        self.path_label.configure(text=self.path_text)
    
    def select_path_event(self):
        selected_path = service.open_folder_dialog()
        self.save_path_setter(selected_path)
        self.change_path_label()



if __name__ == '__main__':
    app = App()
    app.mainloop()