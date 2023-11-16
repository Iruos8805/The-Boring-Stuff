from pathlib import Path
import os,glob,re

regex = re.compile(input('Enter the regex:'))

for file in glob.glob("/home/souri/Desktop/test/*.txt"):
    current = open(file)
    text = current.read()
    

    regtext = regex.search(text)
    if regtext:
        print(regtext.group())

