# TODO - implement y followed by cons as vovel

# Implement porters stemmer
# Step1 - get rid of plurals and -ed -ing
# Step2 - terminal v to i when another vowel in stem
# Step3 - maps double suffixes to single ones -ization -ational
# Step4 - deal with suffixes -full -ness
# Step5 - takes off -ant -ence
# Step6 - remove final e

# Porters helper modules

def m(inp):
    '''
    Return number of consonant sequences in current stem
    Example - <C><V> gives 0 (cry, cry-ing)
            - <C>VC<V> gives 1 (care, car-ing, scare, scar-ing)
            - <C>VCVC<V> gives 2 ( pr o b a b ility)
    '''
    ret = 0
    temp = ''
    vovels = "aeiou"
    for c in inp:
        if c in vovels:
            temp+='v'
        else:
            temp += 'c'
    temp2 = ''
    i = 0
    while i < len(temp):
        if temp[i] == 'c':
            temp2 += 'C'
            while i < len(temp) and temp[i] == 'c':
                i+=1
        elif temp[i] == 'v':
            temp2 += 'V'
            while i < len(temp) and temp[i] == 'v':
                i += 1
    ret = len(temp2) - 2
    ret = ret/2
    if ret < 0:
        return 0
    return ret


def r(inp, suf):
    '''
    In m function is > 0 then set the current suffix of inp to suf
    '''
    if m(inp) > 0:
        inp += suf

def cvc(inp, pos):
    '''
    Checks whether the previous 3 characters before pos were CVC
    also if second c is not w,x,y.
    used to restore e at the end of a short.
    cav(e), lov(e), hop(e), crim(e)
    '''
    vovel = "aeiou"
    if not inp[pos] in vovel and inp[pos-1] in vovel and not inp[pos-2] in vovel:
        if inp[pos-1] == 'w' or inp[pos-1] == 'x' or inp[pos-1]=='y':
            return 0
        else:
            return 1
    return 0
    
    
def vovelinstem(inp):
    '''
    Returns true if vovel is in stem
    '''
    vovel = "aeiou"
    for v in vovel:
        if v in inp:
            return True
    return False

def doublec(inp, j):
    '''
    j j-1 contain a double consonant
    '''
    if inp[j] != inp[j-1]:
        return 0
    vovel = "aeiou"
    if inp[j] in vovel:
        return 0
    return 1

def porter(inp):
    '''
    Implementation of porters algorithm to find the stem of inp
    '''
    # Step 1
    k = len(inp) - 1
    if inp.endswith('s'):
        if inp.endswith('sses'):
            k -= 2
        elif inp.endswith('ies'):
            inp = inp[:-3]+'i'
        elif inp[k-1] != 's':
            k -= 1
    if inp.endswith('eed'):
        if m(inp) > 0:
            k-=1
    elif inp.endswith('ed') or inp.endswith('ing') and vowelinstem(inp):
        k = j
        if inp.endswith('at') or inp.endswith('bl') or inp.endswith('iz'):
            inp = inp+'e'
        elif doublec(inp, k):
            k -= 1
            c = inp[k]
            if c == 'l' or c=='s' or c=='z':
                k += 1
            elif m(inp) == 1 and cvc(inp, k):
                inp = inp[-1:]+'e'
    
    # Step 2
    if inp.endswith('y') and vovelinstem(inp):
        inp = inp[:-1]+'i'

    # Step 3
    if inp[k-1] == 'a':
        if inp.endswith('ational'):
            inp = inp[:-7] + 'ate'
        if inp.endswith('tional'):
            inp = inp[:-6] + 'tion'
    elif inp[k-1] == 'c':
        if inp.endswith('enci'):
            inp = inp[:-4] + 'ence'
        if inp.endswith('anci'):
            inp = inp[:-4] + 'ance'
    elif inp[k-1] == 'e':
        if inp.endswith('izer'):
            inp = inp[:-4] + 'ize'
    elif inp[k-1] == 'l':
        if inp.endswith('bli'):
            inp = inp[:-3] + 'ble'
        if inp.endswith('alli'):
            inp = inp[:-4] + 'al'
        if inp.endswith('entli'):
            inp = inp[:-5] + 'ent'
        if inp.endswith('eli'):
            inp = inp[:-3] + 'e'
        if inp.endswith('ousli'):
            inp = inp[:-5] + 'ous'
    elif inp[k-1] == 'o':
        if inp.endswith('ization'):
            inp = inp[:-7] + 'ize'
        if inp.endswith('ation'):
            inp = inp[:-5] + 'ate'
        if inp.endswith('ator'):
            inp = inp[:-4] + 'ate'
    elif inp[k-1] == 's':
        if inp.endswith('alism'):
            inp = inp[:-5] + 'al'
        if inp.endswith('iveness'):
            inp = inp[:-7] + 'ive'
        if inp.endswith('fulness'):
            inp = inp[:-7] + 'ful'
        if inp.endswith('ousness'):
            inp = inp[:-7] + 'ous'
    elif inp[k-1] == 't':
        if inp.endswith('aliti'):
            inp = inp[:-5] + 'al'
        if inp.endswith('iviit'):
            inp = inp[:-5] + 'ive'
        if inp.endswith('biliti'):
            inp = inp[:-6] + 'ble'
    elif inp[k-1] == 'g':
        if inp.endswith('logi'):
            inp = inp[:-4] + 'log'

    # Step 4


    


