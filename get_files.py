import urllib2
import urllib
import os
import sys
from os.path import join
from bs4 import BeautifulSoup



def processLang(plain_html, lang_name):
    print lang_name
    text = ""
    record = 0
    plain = plain_html.split("\n")

    #TODO: how do deal with languages with transliteration (maybe only look at translit;
    for line in plain:
        if "Source" in line:
            break
        if "<hr>" in line:
            break
        if record == 1:
            text = text + line + "\n"
        if "<h3>" in line and len(text) > 100:
            break
        if "<h2>" in line:
            record = 1
        
        
    
    new_soup = BeautifulSoup(text, 'html.parser')
    str_version = new_soup.get_text()

    with open(lang_name, 'w') as outfile:
        outfile.write(str_version.encode('utf-8'))
    

def readInUrlFile(url_string):
    response = urllib2.urlopen(url_string)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    links_table = soup.find("ol")
    links = links_table.find_all('a')
    for link in links:
        page_url = link.get('href')
        if ".htm" in page_url:
            link_url = url_string.replace("index.htm", page_url)
            new_response = urllib2.urlopen(link_url)
            new_html = new_response.read()
            processLang(new_html, page_url)
            





def main():
    readInUrlFile("http://omniglot.com/babel/index.htm")


if __name__ == "__main__":
    main()