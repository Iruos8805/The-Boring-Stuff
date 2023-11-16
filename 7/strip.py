import re




def takeitaway(thestring,thing):
    if thing =='':
        takeRegex = re.compile(r'^\s+|\s+$')
        thestring = re.sub(takeRegex, "", thestring )
    else:
        takechar = re.compile(thing)
        thestring = re.sub(takechar, "", thestring)
    return thestring    

line = input('Enter line to strip:')
letter = input('Enter the character to strip(if nothing click enter):')
print(takeitaway(line,letter))

