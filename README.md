# opengraph
Extractor for OpenGraph meta tags

This is a a quick and easy script to parse Facebook's OpenGraph protocol using Python 3.

You can scrape article title, description, url, featured image and body text. As this utilises a parser to scrape html documents, you can adjust code to scrape whatever else you want to scrape in the article (eg. Twittercards)

Fake Agent to mask http headers helps with bypassing some website filters. 

# Usage

`$ python3 opengraph.py -u https://example.com`


