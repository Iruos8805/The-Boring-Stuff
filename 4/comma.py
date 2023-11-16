
def commaList(spam):
    for i in range(len(spam)-1):
        print(f'{spam[i]}, ', end='')
    if spam:
        print(f'and {spam[i]}')    

spam = ['apples', 'bananas', 'tofu', 'cats']

commaList(spam)
