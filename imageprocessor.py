
from PIL import  Image, ImageTk
class ImageProcessor:
    def __init__(self, image_path: str):
        self.image_path = image_path

    def getImage(self):
        return ImageTk.PhotoImage(Image.open(self.image_path))

    def __call__(self, image_path: str):
        return ImageTk.PhotoImage(Image.open(self.image_path))
