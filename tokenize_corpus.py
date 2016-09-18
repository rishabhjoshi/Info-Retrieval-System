'''
This scripts takes all documents in the corpus and creates tokens of the 
files present in it. It skips the files who's tokens already exist in 
the index folder.
If you pass -f as a flag, or forced tokenization, this script will create
tokens of all the files in the corpus. No questions asked.
'''

import sys
import os
import subprocess
import re
from mymodules import tokenizer

if __name__ == '__main__':
    try:
        corpusfolder = sys.argv[1]
    except IndexError:
        print ("Usage : python tokenize_corpus.py <flag> <fullpathofCorpus>")
        print ("flag is -f if forced tokenization")
        sys.exit()
    forced = False
    if corpusfolder == '-f':
        forced = True
        try:
            corpusfolder = sys.argv[2]
        except IndexError:
            print ("Usage : python tokenize_corpus.py <flag> <pathofCorpus>")
            sys.exit()
    elif not os.path.exists(corpusfolder):
        print ("Wrong flag or wrong folder. Please check flag and check \nif folder exists. Flag permissible is -f")
        sys.exit()
    else :
        print ("Some error")
        sys.exit()

    cwd = os.getcwd()
    if corpusfolder[-1] != '/':
        corpusfolder += '/'
#    os.chdir(corpusfolder)
    file_list = os.listdir(corpusfolder)
    
    file_list = [filename for filename in file_list \
            if os.path.isfile('./'+filename)]

    print file_list
    for filename in file_list:
        if not forced and os.path.exists("./index/"+filename+".tokens"):
            continue
        else:
            print ("tokenizing "+filename)
            tokenizer(filename)
    
