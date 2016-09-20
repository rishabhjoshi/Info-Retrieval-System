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
    operation(terms, 'and')

def OR(terms):
    operation(terms, 'or')

def diff(terms):
    operation(terms, 'diff')

def symdiff(terms):
    operation(terms, 'symdiff')

def operation(terms, flag):
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
    terms = sort(terms, cmp = comparator)
    ans = index[terms[0]]   #postinglist of 1st term
    for term in terms:
        plist = index[term]
        if flag == 'and':
            ans = ans & plist
        elif flag == 'or':
            ans = ans | plist
        elif flag == 'diff':
            ans = ans - plist
        elif flag == 'symdiff':
            ans = ans ^ plist
    return ans         
