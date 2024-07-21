# Meme Generator

## Setup

### Prerequisites

* OS: Ubuntu 22.04 
* Python version: 3.10.12
* Install ```pdftotext```

  ```
  sudo apt install poppler-utils
  ```
### Installation

* Step 1: Unzip project
2. Setup virtual environment.
   ```
   cd ./meme-gen
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install all project Python dependencies
   ```
   pip install -r requirements.txt
   ```

## Usage

#### Using the cli

```
$ mkdir tmp

$ python meme.py --help
usage: meme.py [-h] [-p PATH] [-b BODY] [-a AUTHOR]

options:
  -h, --help            show this help message and exit
  -p PATH, --path       Input image file path.
  -b BODY, --body       Quote body text.
  -a AUTHOR, --author   Quote author.
```
Or you can run **```python meme.py```** to create a random meme in folder `./tmp`

#### Flask Web Development Server
Starting dev server
```
$ mkdir static

$ export FLASK_APP=app

$ flask run
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```
Go to http://127.0.0.1:5000/ and start to generate meme.

## Submodules

### Libraries
* `Flask`: For webserver interface
* `Pillow`: Process image
* `Pandas`: Process .csv files

### Source code
* `Ingestor`: Module Ingestor includes ingestors to ingest/parse file types (.csv, .docx, .pdf, .txt). Each file type ingestor has it's corresponding class. Then Ingestor class will use all of them to create QuoteModel object.
* `QuoteModule`: Module QuoteModel represents the quote under the format of body and author.
* `MemeEngine`: Moddule MemeEngine create a meme from input image and quote body, author. It first resizes the image to 500x500 pixels and then write the quote on the resized image.




