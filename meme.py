import os
import random
import argparse
from QuoteEngine.Ingestor import Ingestor
from QuoteEngine.Quote import QuoteModel
from MemeGenerator.MemeEngine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a Quote """
    img = None
    Quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = [
            './_data/DogQuotes/DogQuotesTXT.txt',
            './_data/DogQuotes/DogQuotesDOCX.docx',
            './_data/DogQuotes/DogQuotesPDF.pdf',
            './_data/DogQuotes/DogQuotesCSV.csv'
        ]
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        Quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        Quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, Quote.body, Quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a motivational meme")
    parser.add_argument('-path', type=str, help="path to the meme image")
    parser.add_argument('-body', type=str, help="the body of the Quote")
    parser.add_argument('-author', type=str, help="the author of the Quote")

    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
