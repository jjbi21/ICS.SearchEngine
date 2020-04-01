import json
from pathlib import Path
import os
import tokenizer
from collections import defaultdict
import pickle
import math

def find_json():
    """returns json file as a dict"""
    p = Path.cwd()
    q = p / 'webpages_clean' / 'WEBPAGES_CLEAN' / 'bookkeeping.json'
    json1 = open(q)
    json1_str = json1.read()
    json1_data = json.loads(json1_str)
    return json1_data


def parse_and_update(json_data):
    """
    finds relative paths in the json file and turns them into absolute paths so the files can be tokenized
    constructs an index with term frequencies initially
    changes frequency values to tf idf and then dumps to a file
    """
    p = Path.cwd()
    q = p / 'webpages_clean' / 'WEBPAGES_CLEAN'
    with open("index.json", "wb") as handle:
        temp_index = defaultdict(dict)
        n_docs = 0
        for k in json_data.keys():
            n_docs += 1
            s = k.replace('/', '\\')
            hyperlink = os.path.join(q, s)
            to_read = tokenizer.read_file(hyperlink)
            output = tokenizer.t_main(to_read)
            print(k)
            for term in output.keys():
                temp_index[term][k] = output[term]
        temp_index = dict(temp_index)
        compute_tf_idf(temp_index, n_docs)
        pickle.dump(temp_index, handle)
    print(n_docs)

def compute_tf_idf(index, n_docs):
    """
    iterates over index and creates idf values to calculate tf idf
    updates index
    normalizes tf idf values
    """
    doc_length = 0
    for term in index.keys():
        idf = math.log10(n_docs / len(index[term]))
        index[term]['idf'] = idf
        for doc_id in index[term].keys():
            if doc_id == 'idf':
                pass
            else:
            # tf = index[term][doc_id]
                index[term][doc_id] = 1 + math.log10(index[term][doc_id])
                index[term][doc_id] *= idf
                doc_length += index[term][doc_id] ** 2
    normalize(index, math.sqrt(doc_length))


def normalize(index, doc_length):
    """uses doc length to normalize tf idf values"""
    for term in index.keys():
        for doc_id in index[term].keys():
            index[term][doc_id] = index[term][doc_id]/doc_length


if __name__ == '__main__':
    rp_url = find_json()
    parse_and_update(rp_url)
