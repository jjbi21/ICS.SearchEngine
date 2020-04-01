from pathlib import Path
import pickle
import re
import math
from collections import defaultdict
from main import find_json


def read_query(d):
    """Reads input from the user and splits into separate lowercase queries"""
    q = input()
    #print(d.keys())
    words = [i.lower() for i in re.split("[^0-9a-zA-Z]+", q) if i != '' and d.get(i) is not None]
    return words

def process_json():
    """Processes inverted index and returns as dictionary"""
    p = Path.cwd()
    q = p / 'index.json'
    try:
        with open(q, "rb") as handle:
            d = pickle.load(handle)
            pass
    except EOFError:
        print("hi")
    return d


def get_links(d, queries):
    """Calculates query length, computes query scores into dictionary, and returns
    dictionary containing doc_id's matching query and document scores"""
    scored = defaultdict(dict)
    query_links = []
    query_length = 0
    for q in queries:
        if d.get(q) is None:
            return dict()
        query_length += 1 * d[q]['idf'] ** 2
    query_length = math.sqrt(query_length)
    for q in queries:
        for doc_id, doc_weight in d[q].items():
            if doc_id != 'idf':
                scored[q][doc_id] = doc_weight * (d[q]['idf']/query_length)
    inverse_scored = defaultdict(int)
    for query, doc_dict in scored.items():
        for doc_id, score in doc_dict.items():
            inverse_scored[doc_id] += score
    return inverse_scored


def get_urls(query_links):
    """Returns list of the url's matching query ordered by ranking"""
    links = []
    # n = 0
    for doc_id, score in sorted(query_links.items(), key=lambda kv: -kv[1]):
        # print(doc_id, score)
        links.append(json_dict[doc_id])
        # n += 1
    return links


def input_page(links):
    """Reads input from the user continuosly and checks if its valid.
    If the input is a valid page number, return page number as an int. If
    the input is exit command, return 0 as terminator. Otherwise, prompt again"""
    page_num = None
    while page_num is None:
        try:
            page_num = input("Enter page number or 'exit' when finished: ")
            if page_num == "exit":
                return 0
            else:
                page_num = int(page_num)
            if page_num >= 0 and not(page_num > len(links)/10):
                return page_num
            else:
                print("invalid input: out of bounds")
                page_num = None
        except ValueError:
            print("invalid input")
            page_num = None


if __name__ == '__main__':
    """Reads query and prints top ten results"""
    d = process_json()
    queries = read_query(d)
    query_links = get_links(d, queries)
    json_dict = find_json()
    links = get_urls(query_links)

    page_number = 0
    while page_number != -1:
        page_number = input_page(links) - 1
        n = 0
        for link in links:
            if n == -1 or n > page_number * 10 + 9:
                break

            if n >= page_number * 10:
                print(link)
            n += 1
        print("Current page:", page_number + 1)
