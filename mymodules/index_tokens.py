import sys
import os
import re
import glob
from tokenizer import tokenizer
try:
    import cPickle as pickle
except :
    import pickle

def index_tokens (flag):
    path_of_index_folder = '../index/'
    if flag == '-f':
        corpusfolder = '../corpus/'
        filelist = os.listdir(corpusfolder)
        if len(filelist) == 0:
            print ("No files in corpus. Please insert docs in corpus.")
            sys.exit()
        filelist = [filename for filename in filelist if os.path.isfile(corpusfolder+filename)]
        for filename in filelist:
            print ("tokenizing "+filename)
            tokenizer(filename)

    elif flag == '-n':
        cwd = os.getcwd()
        if not os.path.exists(path_of_index_folder):
            print ("Index folder containing tokens doesnt exist.")
            print ("Please create tokens first")
            sys.exit()

    filelist = glob.glob(path_of_index_folder+'*.tokens')
    if len(filelist) == 0:
        print ("No tokens file in the index folder!")
        print ("Please create the tokens first")
        sys.exit()

    index = dict()
    for filename in filelist:
        file_tokens = pickle.load(open(filename, "rb"))
        for token in file_tokens:
            if index.has_key(token):
                index[token].add(filename)
            else:
                index.update({token:set([filename])})
        print ("Index of "+filename+" done!")

    pickle.dump(index, open(path_of_index_folder+'index.index', 'wb'))

if __name__ == '__main__':
    try:
        files = sys.argv[1]
    except IndexError:
        print ("Usage : python index_tokens.py <files>")
        print ("files is list of files you want to add to index")
        print ("or \"all\" if you want to index all files whose tokens are present in the corpus")
        sys.exit()
       #TODO

    if files == 'all':
        index_tokens('-n')
    else:
        print ("Sorry that feature is not yet implemented")

