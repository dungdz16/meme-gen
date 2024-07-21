import random
import os
import requests
from flask import Flask, render_template, abort, request
from PIL import Image
from io import BytesIO

# @TODO Import your Ingestor and MemeEngine classes
from Ingestor.Ingestor import Ingestor
from QuoteEngine import QuoteModel
from MemeEngine import MemeEngine
app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))
    images_path = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]
    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    print(path)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    response = requests.get(request.form['image_url'])
    if response.status_code == 200:
        # open the image using Pillow
        img = Image.open(BytesIO(response.content))
        # save the image in JPG format
        tmp = f'/tmp/{random.randint(0,1000000)}.jpg'
        img.save(tmp, "JPEG")
        print(f"Image successfully saved to {tmp}")
    else:
        print(f"Failed to get image. HTTP Status code: {response.status_code}")
        return

    quote = QuoteModel(body=request.form['body'],
                       author=request.form['author'])
    path = meme.make_meme(tmp, quote.body, quote.author)
    os.remove(tmp)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
