#import json
#from pathlib import Path

'''import re
import io
from collections import defaultdict
from bs4 import BeautifulSoup

#https://nlp.stanford.edu/IR-book/html/htmledition/dropping-common-terms-stop-words-1.html
STOP_WORDS = {'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from',\
              'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the',\
              'to', 'was', 'were', 'will', 'with'}

# reads a file from console and returns it, no reading/parsing is done
def read_file(file_name):
    my_file = io.open(file_name, 'r', encoding = "utf-8")
    return my_file


# tokenizes file by chunks and returns output dictionary with alphanumeric tokens as keys
def tokenize(soup, ten, five, two):
    output = defaultdict(int)
    # a string of all words (lowercased) in file
    everything = soup.get_text().lower()
    # tokenizing happens in this line, comprehension filters out empty strings
    tokens = [i for i in re.split("[^0-9a-zA-Z]+", everything) if i != '']
    for token in tokens:
        if token not in STOP_WORDS:
            if token in ten:
                output[token] += 10
            elif token in five:
                output[token] += 5
            elif token in two:
                output[token] += 2
            else:
                output[token] += 1
    return output

def t_main(r_file):
    soup = BeautifulSoup(r_file, 'html.parser')
    #body: 1, title: 10, headers: 5 , b: 2 , strong: 2

    #finds all strings in title tags
    ten = {t.text.strip() for t in soup.find_all('title')}
    #plain text before <body> tag is considered the title
    soup_text = str(soup)
    t_ten = set()
    #if there is no body tag, the whole document should not be considered the title
    if len([t.text.strip() for t in soup.find_all('body')]) != 0:
        title_list = soup_text.split('<body>')
        if title_list[0] != '':
            ten.add(title_list[0])
        #tokenizes the string for title words that should be weighted 10 times more
        for element in ten:
            t_element = [i for i in re.split("[^0-9a-zA-Z]+", element) if i != '']
            for t_e in t_element:
                t_ten.add(t_e)
        #when plain text before <body> tag is added, the tags are included as tokens ...
        #   remove the tags, unless the tags are actual words in the title
        if len(title_list[0].split('<title>')) != 1 or len(title_list[0].split('</title>')) != 1:
            t_ten.discard('title')
        if len(title_list[0].split('<h1>')) != 1 or len(title_list[0].split('</h1>')) != 1:
            t_ten.discard('h1')
        if len(title_list[0].split('<h2>')) != 1 or len(title_list[0].split('</h2>')) != 1:
            t_ten.discard('h2')
        if len(title_list[0].split('<h3>')) != 1 or len(title_list[0].split('</h3>')) != 1:
            t_ten.discard('h3')
        if len(title_list[0].split('<b>')) != 1 or len(title_list[0].split('</b>')) != 1:
            t_ten.discard('b')
        if len(title_list[0].split('<strong>')) != 1 or len(title_list[0].split('</strong>')) != 1:
            t_ten.discard('strong')

    # finds all strings in header tags
    h_text = [t.text.strip() for t in soup.find_all(['h1', 'h2', 'h3'])]
    five = set(h_text)
    # tokenizes the string for header words that should be weighted five times more
    t_five = set()
    for element in five:
        t_element = [i for i in re.split("[^0-9a-zA-Z]+", element) if i != '']
        for t_e in t_element:
            t_five.add(t_e)

    # finds all strings in bold and strong tags
    bs_text = [t.text.strip() for t in soup.find_all(['b', 'strong'])]
    two = set(bs_text)
    # tokenizes the string for bold and strong words that should be weighted two times more
    t_two = set()
    for element in two:
        t_element = [i for i in re.split("[^0-9a-zA-Z]+", element) if i != '']
        for t_e in t_element:
            t_two.add(t_e)
    ###############################################

    output = tokenize(soup, t_ten, t_five, t_two)
    r_file.close()

    return output
'''
'''
if __name__ == '__main__':
    p = Path.cwd()
    q = p / 'webpages_clean' / 'WEBPAGES_CLEAN' / '2' / '3'

    to_read = read_file(q)
    output = t_main(to_read)
'''

#import json
#from pathlib import Path

import re
import io
from collections import defaultdict
from bs4 import BeautifulSoup

#https://nlp.stanford.edu/IR-book/html/htmledition/dropping-common-terms-stop-words-1.html
STOP_WORDS = {'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from',\
              'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the',\
              'to', 'was', 'were', 'will', 'with'}

# reads a file from console and returns it, no reading/parsing is done
def read_file(file_name):
    my_file = io.open(file_name, 'r', encoding = "utf-8")
    return my_file


# tokenizes file by chunks and returns output dictionary with alphanumeric tokens as keys
def tokenize(soup, ten, five, two):
    output = defaultdict(int)
    # a string of all words (lowercased) in file
    everything = soup.get_text().lower()
    # tokenizing happens in this line, comprehension filters out empty strings
    tokens = [i for i in re.split("[^0-9a-zA-Z]+", everything) if i != '']
    for token in tokens:
        if token not in STOP_WORDS:
            if token in ten.keys():
                output[token] += 10
                ten[token] -= 1
                if ten[token] == 0:
                    ten.pop(token)
            elif token in five.keys():
                output[token] += 5
                five[token] -= 1
                if five[token] == 0:
                    five.pop(token)
            elif token in two.keys():
                output[token] += 2
                two[token] -= 1
                if two[token] == 0:
                    two.pop(token)
            else:
                output[token] += 1
    return output

def t_main(r_file):
    soup = BeautifulSoup(r_file, 'html.parser')
    #body: 1, title: 10, headers: 5 , b: 2 , strong: 2

    #finds all strings in title tags
    ten = [t.text.strip() for t in soup.find_all('title')]
    #plain text before <body> tag is considered the title
    soup_text = str(soup)
    t_ten = defaultdict(int)
    #if there is no body tag, the whole document should not be considered the title
    if len([t.text.strip() for t in soup.find_all('body')]) != 0:
        title_list = soup_text.split('<body>')
        if title_list[0] != '':
            ten.append(title_list[0])
        #tokenizes the string for title words that should be weighted 10 times more
        for element in ten:
            t_element = [i for i in re.split("[^0-9a-zA-Z]+", element) if i != '']
            for t_e in t_element:
                t_ten[t_e] += 1
        #when plain text before <body> tag is added, the tags are included as tokens ...
        #   remove the tags, unless the tags are actual words in the title
        if len(title_list[0].split('<title>')) != 1 or len(title_list[0].split('</title>')) != 1:
            del t_ten['title']
        if len(title_list[0].split('<h1>')) != 1 or len(title_list[0].split('</h1>')) != 1:
            del t_ten['h1']
        if len(title_list[0].split('<h2>')) != 1 or len(title_list[0].split('</h2>')) != 1:
            del t_ten['h2']
        if len(title_list[0].split('<h3>')) != 1 or len(title_list[0].split('</h3>')) != 1:
            del t_ten['h3']
        if len(title_list[0].split('<b>')) != 1 or len(title_list[0].split('</b>')) != 1:
            del t_ten['b']
        if len(title_list[0].split('<strong>')) != 1 or len(title_list[0].split('</strong>')) != 1:
            del t_ten['strong']

    # finds all strings in header tags
    h_text = [t.text.strip() for t in soup.find_all(['h1', 'h2', 'h3'])]
    # tokenizes the string for header words that should be weighted five times more
    t_five = defaultdict(int)
    for element in h_text:
        t_element = [i for i in re.split("[^0-9a-zA-Z]+", element) if i != '']
        for t_e in t_element:
            t_five[t_e] += 1

    # finds all strings in bold and strong tags
    bs_text = [t.text.strip() for t in soup.find_all(['b', 'strong'])]
    # tokenizes the string for bold and strong words that should be weighted two times more
    t_two = defaultdict(int)
    for element in bs_text:
        t_element = [i for i in re.split("[^0-9a-zA-Z]+", element) if i != '']
        for t_e in t_element:
            t_two[t_e] += 1
    ###############################################

    output = tokenize(soup, t_ten, t_five, t_two)
    r_file.close()

    return output

'''
if __name__ == '__main__':
    p = Path.cwd()
    q = p / 'webpages_clean' / 'WEBPAGES_CLEAN' / '2' / '3'

    to_read = read_file(q)
    output = t_main(to_read)
'''