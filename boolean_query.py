from mymodules import merge
import sys
import os

if __name__ == '__main__':
    try :
        querystr = sys.argv[1]
    except IndexError:
        print ("Error! Usage: python boolean_query.py '<querystring>'")
        print ("Example query string: 'dont & !eragon'")
        sys.exit()
    if not os.path.exists('./index/index.index'):
        print ("Index doesnt exist!")
        print ("First create the index!")
        sys.exit()




