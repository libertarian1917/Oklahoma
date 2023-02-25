import pytube
import os

class Video:

    def __init__(self, save_path, link):
        self.save_path = save_path
        self.link = link

    def download_video(self):
        os.chdir(self.save_path)

        yt = pytube.YouTube(self.link)
        yt.streams.get_highest_resolution().download()