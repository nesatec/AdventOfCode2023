def day1():
    text = open("day1.txt", "r")
    addsum = 0
    replacements_dictionary = {'one' : 'o1ne', 'two' : 'tw2o', 'three' : 'thre3e','four': 'fo4ur', 'five':'fi5ve','six': 'si6x','seven': 'sev7en','eight' : 
    'ei8ght','nine':'ni9ne'}
    for zeile in text:
        numlist = []
        for key,value in replacements_dictionary.items():
            zeile = zeile.replace(key, value)
        zeillist = list(zeile)
        for i in zeillist:
            if i.isnumeric():
                numlist.append(i)
        addsum = addsum +  int(numlist[0]) + int(numlist[len(numlist)-1])
    print(addsum)

day1()