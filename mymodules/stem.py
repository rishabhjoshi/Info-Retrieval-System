# Implement porters stemmer
# Step1 - get rid of plurals and -ed -ing
# Step2 - terminal v to i when another vowel in stem
# Step3 - maps double suffixes to single ones -ization -ational
# Step4 - deal with suffixes -full -ness
# Step5 - takes off -ant -ence
# Step6 - remove final e

# Porters helper modules

def m():
    '''
    Return number of consonant sequences in current stem
    Example - <C><V> gives 0 (cry, cry-ing)
            - <C>VC<V> gives 1 (care, car-ing, scare, scar-ing)
            - <C>VCVC<V> gives 2 ( pr o b a b ility)
    '''

def r(str):
    '''
    In m function is > 0 then set the current suffix to str
    '''

def cvc(pos):
    '''
    Checks whether the previous 3 characters before pos were CVC
    '''

    
def vovelinstem(inp):
    '''
    Returns true if vovel is in stem
    '''
    vovel = "aeiou"
    for v in vovel:
        if v in inp:
            return True
    return False

def porter(inp):
    '''
    Implementation of porters algorithm to find the stem of inp
    '''
    # Step 1
    k = len(inp)
    if inp.endswith('s'):
        if inp.endswith('sses'):
            k -= 2
        elif inp.endswith('ies'):
            inp = inp[:-3]+'i'
        elif inp[k-2] != 's':
            k -= 1
    if inp.endswith('eed'):
        if m(inp) > 0
            k-=1
    elif inp.endswith('ed') or inp.endswith('ing') and vowelinstem(inp):
        k = j
        if inp.endswith('at') or inp.endswith('bl') or inp.endswith('iz'):
            inp = inp+'e'
        elif doublec(k-1):
            k -= 1
            c = inp[k-1]
            if c == 'l' or c=='s' or c=='z':
                k += 1
            elif m(inp) == 1 and cvc(k-1):
                inp = inp[-1:]+'e'


