from mymodules import merge
import sys
import os
try :
    import cPickle as pickle
except:
    import pickle

    #Code for boolean_query in python.
indexfolder = './index/'
if not os.path.exists(indexfolder + 'index.index'):
    print ("No index exists. Please create index first!")
    sys.exit()
index = pickle.load(open(indexfolder+'index.index', 'rb'))

if __name__ == '__main__':
    try :
        querystr = sys.argv[1]
    except IndexError:
        print ("Error! Usage: python boolean_query.py '<querystring>'")
        print ("Example query string: '( dont & ( ! eragon ) )'")
        print ("DONT FORGET TO PUT BRACKETS(proper spacing)!!! The system is not that good to handle precedence. Well really,.... i dont have the time to add the feature. Sorry.")
        print ("Brackets are only of the form ( a op b ) or ( ! a )")
        sys.exit()
    if not os.path.exists('./index/index.index'):
        print ("Index doesnt exist!")
        print ("First create the index!")
        sys.exit()
    stack = []
    top = 0
    querystr = querystr.split(' ')
    operators = ['(', ')', '&', '|', '!']
    pliststr = []
    for term in querystr:
        if term in operators:
            pliststr.append(term)
        else:
            pliststr.append(index[term])
    for op in pliststr:
        if not op == ')':
            stack.append(op)
        else:
            plist2 = stack.pop()
            opn = stack.pop()
            if opn == '!':
                ans = merge.NOT(plist2)
                stack.pop() # matching (
                stack.append(ans)
            else:
                plist1 = stack.pop()
                stack.pop() # for matching (
                if opn == '&':
                    ans = merge.AND([plist1, plist2])
                elif opn == '|':
                    ans = merge.OR([plist1, plist2])
                stack.append(ans)
    finalplist = stack[0]
    print ("The final posting list is the set :")
    print finalplist
    print ("Thank you for using this application!")
    print ("Author : RISHABH JOSHI - BITS Pilani")
    sys.exit()
