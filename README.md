# ICS.SearchEngine
## main.py
Builds an inverted index using pre-crawled set of webpages (not provided but tested on pages from the ics.uci.edu subdomain).
Uses TF-IDF weighting.
Uses pickle to store index locally as a json file.
## query_launcher.py
Computes user query score and fetches relevant links by processing the inverted index.
Paginates ranked results to display links in console.
## tokenizer.py
Custom tokenizer that uses bs4 to parse html and give heavier weights to keywords
