import argparse, urllib.request, requests, re
from bs4 import BeautifulSoup
from queue import Queue
from threading import Thread
#input validation
def validate_url(input_url):
    if "http://" not in input_url:
        raise ValueError("not a valid URL!")
    elif "https://" not in input_url:
        raise ValueError("not a valid URL!")
#user input
input = argparse.ArgumentParser()
input.add_argument("url", help="enter the URL you would like to parse")
input_arguments = input.parse_args()
#start
def main():
    validate_url(input_arguments.url)
    page = BeautifulSoup(urllib.request.urlopen(input_arguments.url), "html.parser")
    images = page.findAll('img')
    source_list = []
    # create our list of src urls
    for image in images:
        src = image['src']
        if src.find("../") != -1:
            src = src.replace("../", "")
        source_list.append(src)
    if len(source_list)  == 0:
        raise ValueError("no sources!")
    # download images from url list
    for src in source_list:
        filename = re.search('\/[^\/]+$', src).group(0).replace("/","") 
        print("downloading " + filename)
        with open( filename, 'wb') as handler:
            data = requests.get(src, stream=True)        
            if not data.ok:
                print(data)

            for block in data.iter_content(1024):
                if not block:
                    break
                handler.write(block)
            print(filename + " downloaded!")

if __name__ == '__main__':
    main()
