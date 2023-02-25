#from urllib.parse import urlparse
from datetime import datetime
import requests
import os


class Image:

    def __init__(self, save_path, url):

        self.url = url
        self.save_path = save_path

        now = datetime.now()
        current_time = now.strftime("%d%m%Y_%H%M%S")
        self.image_name = 'img_' + current_time + '.jpg'

    def download_image(self):

        os.chdir(self.save_path)

        with open(self.image_name, 'wb') as handle:
            response = requests.get(self.url, stream=True)

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)