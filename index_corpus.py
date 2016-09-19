import sys
import os
import glob
from mymodules import index_tokens

if __name__ == '__main__':
    try :
        flag = sys.argv[1]
    except IndexError:
        print ("Usage : python index_corpus.py <flag>")
        print ("<flag> is -f if you want to force index creation. This will create index for all files in the corpus, regardless if tokens created")
        print ("<flag> is -n if no-force, so index will be created if index.index file is not present, and for only those files whose token is already created")
        sys.exit()
    indexfolder = '../index/'
    
    cwd = os.getcwd()
    os.chdir('./mymodules')
    if flag == '-n':
        if not os.path.exists(indexfolder):
            print ("Index folder doesnt exist")
            print ("Please create the index folder and the tokens first.")
            print ("Call tokenize_corpus first, or use -f flag")
            sys.exit()
        elif len(glob.glob(indexfolder+'*.tokens')) == 0:
            print ("No tokens in index folder!")
            print ("Create some tokens using the tokenize_corpus script!")
            sys.exit()
        else:
            index_tokens(flag) #noforce index creation

    elif flag == '-f':
        index_tokens(flag)  #force index creation
    else :
        print ("wrong flag. Use -f or -n for forced or no-force index creation.")

    os.chdir(cwd)
