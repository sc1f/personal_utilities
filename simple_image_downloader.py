# downloads images with relative URLs, very buggy but worked for my specific use case

import urllib.request, requests, re
from bs4 import BeautifulSoup
#input validation
def validate_url(input_url):
    if "http" not in input_url:
        raise ValueError("not a valid URL!")
#user input
baseurl = input("enter the baseurl: ")
validate_url(baseurl)
parseurl = input("enter the url to be parsed: ")
validate_url(parseurl)
# start
page = BeautifulSoup(urllib.request.urlopen(parseurl), "html.parser")
images = page.findAll('img')
source_list = []
# create our list of src urls
for image in images:
    src = image['src']
    if src.find("../") != -1:
        src = src.replace("../", "")
    source_list.append(baseurl + src)
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
