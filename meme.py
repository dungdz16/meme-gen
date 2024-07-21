import os
import random
import argparse
import pathlib
# @TODO Import your Ingestor and MemeEngine classes
from Ingestor.Ingestor import Ingestor
from QuoteEngine import QuoteModel
from MemeEngine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # @TODO Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path',
                        type=pathlib.Path,
                        default=None,
                        help="Input image file path.")
    parser.add_argument('-b', '--body',
                        type=str,
                        default=None,
                        help="Quote body text.")
    parser.add_argument('-a', '--author',
                        type=str,
                        default=None,
                        help="Quote author.")
    args = parser.parse_args()
    print("Output image path: " + generate_meme(args.path,
                                                args.body,
                                                args.author))
