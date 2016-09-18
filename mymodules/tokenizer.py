''' 
script to take in a directory and create a .index file that has inverted
index of all the files

stop words - textfixer.com/resources/common-english-words.txt

* works only on single level directly, not recursively
* Static indexing
'''

import sys
import subprocess
import datetime
import re
import os
try:
    import cPickle as pickle
except ImportError:
    import pickle

stop_words = set(["a","able","about","across","after","all","almost",
    "also","am","among","an","and","any","are","as","at","be","because",
    "been","but","by","can","cannot","could","dear","did","do","does",
    "either","else","ever","every","for","from","get","got","had","has",
    "have","he","her","hers","him","his","how","however","i","if","in",
    "into","is","it","its","just","least","let","like","likely","may",
    "me","might","most","must","my","neither","no","nor","not","of",
    "off","often","on","only","or","other","our","own","rather","said",
    "say","says","she","should","since","so","some","than","that","the",
    "their","them","then","there","these","they","this","tis","to","too",
    "twas","us","wants","was","we","were","what","when","where","which",
    "while","who","whom","why","will","with","would","yet","you","your"])

def tokenizer (filepath):
    ''' This function take a filepath as argument
        It creates a set of tokens of the terms in the file and dumps them
        to a filename.tokens file in the folder "$PWD/../index/"
    '''
    
    filename = (filepath.split('/'))[-1]
    cwd = filepath
    print "creating index for %s" % filename
    file = open(filepath, 'r')
    tokens = set([])

    for line in file:
        line = re.sub("[^a-zA-Z\-\']", " ", line) #will take - and 's
        token_list = (line.lower()).split()

        for tk in token_list:
            tk = re.sub("[^a-zA-Z]", "", tk)
            if tk not in stop_words:
                tokens.add(tk)

    file.close()
    cwd = os.getcwd()
    folder = "./../index"
    if not os.path.exists(folder):
        os.makedirs(folder)
    os.chdir(folder)
    print "creating file %s.tokens" % filename
    pickle.dump(tokens, open(filename+".tokens", "wb"))
    os.chdir(cwd)
    print "%s tokenized successfully" % filename

def init():
    cwd = os.getcwd()
    corpusdir = cwd+'/../corpus'
    if not os.path.exists(corpusdir):
        os.makedirs(corpusdir)
    os.chdir(directory)
    
    filelist = glob.glob("*")
    for filename in filelist:
        tokenizer(filename)


if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except IndexError:
        print ("Usage : python tokenizer.py <full path of file>")
        sys.exit()
    tokenizer(filename)
