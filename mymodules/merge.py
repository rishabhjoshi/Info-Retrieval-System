# This module implements the AND, OR, XOR, functions of merging the sets
# This is mainly needed for boolean queries
import os
import sys
try :
    import cPickle as pickle
except :
    import pickle

def comparator(term1, term2, index):
    '''
    Compare the terms' size of posting in index
    '''
    if len(index[term1]) <= len(index[term2]):
        return -1
    else:
        return 1

def AND(terms):
    '''
    AND takes a list of terms, and merges the posting lists of these terms
    and returns a set of postings present in the intersection of the 
    terms's list
    '''
    indexfolder = '../index/'
    if not os.path.exists(indexfolder+'index.index'):
        print ("No index exists. Please create the index first!")
        sys.exit()
    index = pickle.load(open(indexfolder+'index.index', "rb"))
    ans = set([])
    terms = sort(terms, cmp = comparator)
    for term in terms:
        plist = index[term]
        ans.union(
            

