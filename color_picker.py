from colorthief import ColorThief
from PIL import Image
from werkzeug.utils import secure_filename


class ColorPicker(ColorThief):
    def __init__(self, file):
        # We gotta resize and compress the image before passing it to ColorThief
        resized_image = self.resize_and_compress_image(file)
        super().__init__(resized_image)
        self.color_thief = ColorThief(resized_image)
        self.dominant_color = self.color_thief.get_color(quality=1)
        self.palette = self.color_thief.get_palette(color_count=11)

    def resize_and_compress_image(self, file):
        img = Image.open(file)
        print(file)
        resized_img = img.resize((800, 600))
        filename = secure_filename(file.filename)
        resized_img_path = "./static/img/resized_" + filename
        resized_img.save(resized_img_path, quality=90)
        img.close()
        return resized_img_path
