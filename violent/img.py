import requests
from bs4 import BeautifulSoup
from urlparse import urlsplit
from os.path import basename
from PIL import Image
from PIL.ExifTags import TAGS

def find_images(url):
    content = requests.get(url).text
    soup = BeautifulSoup(content)
    im_tags = soup.findAll('img')
    return im_tags

def download_img(im_tag):
    try:
        im_src = "https://ocw.mit.edu" + im_tag['src']
        im_content = requests.get(im_src, stream=True).raw
        im_file_name = basename(urlsplit(im_src)[2])
        with open(im_file_name, 'wb') as im_file:
            for chunk in im_content:
                im_file.write(chunk)
        return im_file_name
    except:
        return ''

def get_exif(im_file_name):
    try:
        exif_data = {}
        im_file = Image.open(im_file_name)
        info = im_file._getexif()
        if info:
            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)
                exif_data[decoded] = value
            exif_gps = exif_data['GPSInfo']
            return exif_gps
    except:
        pass

for im_tag in find_images("https://ocw.mit.edu/index.htm")[1:3]:
    print(im_tag['src'])
    im_file_name = download_img(im_tag)
    print(get_exif(im_file_name))
