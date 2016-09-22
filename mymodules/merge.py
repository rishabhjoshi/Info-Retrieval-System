# This module implements the AND, OR, XOR, functions of merging the sets
# This is mainly needed for boolean queries
import os
import sys
try :
    import cPickle as pickle
except :
    import pickle

# Globally define the index for use in the comparator
#indexfolder = '../index/'
#if not os.path.exists(indexfolder+'index.index'):
#    print ("No index exists. Please create the index first!")
#    sys.exit()
#index = pickle.load(open(indexfolder+'index.index', "rb"))

# Comparator used to sort the input plists list
def comparator(plist1, plist2):
    '''
    Compare the plists' size of posting in index
    '''
    if len(plist1) <= len(plist2):
        return -1
    else:
        return 1

def AND(plists):
    return operation(plists, 'and')

def OR(plists):
    return operation(plists, 'or')

def DIFF(plists):
    return operation(plists, 'diff')

def SYMDIFF(plists):
    return operation(plists, 'symdiff')

def NOT(plists):
    return operation(plists, 'not')

def operation(plists, flag):
    '''
    This takes a list of plists (or sets), and merges the posting lists of these plists (or the sets, which are themselves postings)
    and returns a set of postings present in the merged set of the 
    plists's list
    '''
    if flag == 'not':
        # Complement (NOT)a
        doclist = glob.glob('./../corpus/*')
        for i in range(len(doclist)):
            doclist[i] = (doclist[i].strip('/')[-1]).strip('.')[0]
        ans = set(doclist) - plists[0]
        return ans
    plists = sorted(plists, cmp = comparator)
    ans = plists[0]   #postinglist of 1st plist
    for plist in plists[1:]:
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
    print ("This module has functions to merge the posting lists on conditinos such as AND, OR, DIFF, SYMDIFF")
    print ("The functions of this module can be used by passing a list of posting to \n   -- AND\n   -- OR\n   -- DIFF\n   -- SYMDIFF\n   -- NOT")
    sys.exit()
