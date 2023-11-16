import re

password = input('Enter the password: ')

passRegex = re.compile(r'''
    ^
    (?=.*[a-z])     
    (?=.*[A-Z])     
    (?=.*[0-9])     
    .{8,}           
    $
''', re.VERBOSE)

mo = passRegex.search(password)

if mo:
    print("That is a strong password")
else:
    print("That is not a strong password")
