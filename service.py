import tkinter
import tkinter.filedialog as filedialog
import customtkinter

def open_folder_dialog():
    # Create window of explorer
    root = tkinter.Tk()
    root.withdraw()
    # Without it explorer closes too fast
    root.wm_attributes('-topmost', 1)
    directory_path = filedialog.askdirectory()
    return directory_path

def check_text_size(text):
    size = len(text)
    if size > 30:
        new_text = text[0:30] + '...'
        return new_text
    else:
        return text
    

class DataInput:

    def __init__(self, text, title):
        self.text = text
        self.title = title

    def dialog(self):
        self.data_input_dialog = customtkinter.CTkInputDialog(text=self.text, title=self.title)
        self.input_result = self.data_input_dialog.get_input()
        return self.input_result