import re
def sortirovka():
    s = ['анТОн', 'НАТАЛЬЯ', 'никита', 'МаРиЯ', '!СЕРГЕЙ!', 'Владимир747', 'Павел+100500']
    for i in s:
        print(re.sub("[$|@|&|!|+|1234567890|]","",i.lower().title()), end = " ")
sortirovka()