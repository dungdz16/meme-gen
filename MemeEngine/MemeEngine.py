from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    def __init__(self, out_path):
        """
        Initialize MemeEngine object.

        @param self: The object pointer.
        @param out_path: Output path for generated image.
        """
        self.out_path = out_path
        self.font_path = "MemeEngine/fonts/LilitaOne-Regular.ttf"

    def make_meme(self, img_path=None, body=None, author=None):
        """
        Create a meme from input image and quotes.

        @param self: The object pointer.
        @param img_path: Input path for the image.
        @param body: Body text of the quote.
        @param author: Author of the quote.
        """
        with Image.open(img_path) as im:
            # resize the image to 500x500
            im.thumbnail((500, 500))
            fnt = ImageFont.truetype(self.font_path, 30)
            # get a drawing context
            d = ImageDraw.Draw(im)
            # draw text, half opacity
            d.text((50, 50), body, font=fnt, fill=(255, 255, 255, 128))
            d.text((90, 90), "-" + author, font=fnt, fill=(255, 255, 255, 128))
            # save image
            img_out_path = self.out_path + '/' + 'img_crop_resized.jpg'
            im.save(img_out_path, 'JPEG')

            return img_out_path
