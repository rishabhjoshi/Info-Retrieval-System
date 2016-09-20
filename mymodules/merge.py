# This module implements the AND, OR, XOR, functions of merging the sets
# This is mainly needed for boolean queries
import os
import sys
try :
    import cPickle as pickle
except :
    import pickle

# Globally define the index for use in the comparator
indexfolder = '../index/'
if not os.path.exists(indexfolder+'index.index'):
    print ("No index exists. Please create the index first!")
    sys.exit()
index = pickle.load(open(indexfolder+'index.index', "rb"))

# Comparator used to sort the input terms list
def comparator(term1, term2):
    '''
    Compare the terms' size of posting in index
    '''
    if len(index[term1]) <= len(index[term2]):
        return -1
    else:
        return 1

def AND(terms):
    return operation(terms, 'and')

def OR(terms):
    return operation(terms, 'or')

def DIFF(terms):
    return operation(terms, 'diff')

def SYMDIFF(terms):
    return operation(terms, 'symdiff')

def operation(terms, flag):
    '''
    AND takes a list of terms, and merges the posting lists of these terms
    and returns a set of postings present in the intersection of the 
    terms's list
    '''
    terms = sorted(terms, cmp = comparator)
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

if __name__ == '__main__':
    print ("This module has functions to merge the posting lists of terms on conditinos such as AND, OR, DIFF, SYMDIFF")
    print ("The functions of this module can be used by passing a list of terms to \n   -- AND\n   -- OR\n   -- DIFF\n   -- SYMDIFF")
    sys.exit()
