#!/bin/env python3
""" processing the UTF-8 list documents 
   Args: 
     python3 fetch_words_function <url>

"""
from sys import argv
from urllib.request import urlopen
def fetch_words(url):
  """ fetch a list of words from a URL. 
    
      Args: 
         url: this URL should be UTF-8 list document.
      
      Returns: 
           A list of strings containing the words from the documents.

  """
  story = urlopen(url)
  story_words=[]
  for line in story :
    line_words = line.decode('utf8').split()

    for word in line_words :
         story_words.append(word)
  story.close()
  return story_words


def print_words(items):
   
  for item in items :
    print (item)


def main(url) :
       items = fetch_words(url)
       print_words(items)
    
if __name__ == '__main__' :
     main(argv[1])
