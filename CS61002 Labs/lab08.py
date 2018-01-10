#Nikhil Vemula
#March 5,2016
#CS61002

## Matching DNA Program

# function for adjusting hypens for given strings
def getcurrentstring(firstString,secString):
    firstlen = len(firstString)
    seclen = len(secString)
    if firstlen>seclen:
        secString = secString.ljust(firstlen,'-')
    if seclen>firstlen:
        firstString = firstString.ljust(seclen,'-')

    return firstString,secString

# function for getting hyphen indexes for strings
def getindexces(string):
    indexes = []
    for i in range(len(string)):
        if string[i] == '-':
            indexes.append(i+1)
    return indexes

# Mainfunction for entire show
def mainfunction():
    firstString = raw_input('String 1: ').lower()
    secString = raw_input('String 2: ').lower()

    if firstString=='' or secString=='':
        print 'Given inputs are not valid, Please try again.'
        return

    quit_sel = 0
    while not quit_sel:
        selection = raw_input('\nWhat do you want to do:\n\ta (Add an Indel)\n\td (Delete an Indel)\n\ts (Score)\n\tq (Quit) : ')

        if selection=='s':
            firstString,secString = getcurrentstring(firstString,secString)
            match = 0
            misMatch = 0
            Str1 = ''
            Str2 = ''
            for i in range(len(firstString)):
                if firstString[i]=='-' or secString[i]=='-':
                    misMatch = misMatch+1
                    Str1 = Str1+firstString[i].upper()
                    Str2 = Str2+secString[i].upper()                    
                else:
                    if firstString[i]==secString[i]:
                        match = match+1
                        Str1 = Str1+firstString[i]
                        Str2 = Str2+secString[i]
                    else:
                        misMatch = misMatch+1
                        Str1 = Str1+firstString[i].upper()
                        Str2 = Str2+secString[i].upper()
                
            print '\nMatches: %s\tMismatches: %s'%(match,misMatch)
            print 'Str1: %s'%(Str1)
            print 'Str2: %s'%(Str2)


        elif selection=='a':
            stringsel = raw_input('Which string to change (1 or 2): ')
            if stringsel!='1' and stringsel!='2':
                print 'Given input is wrong, Please try again.'
            else:
                toaddString = [firstString,secString][int(stringsel)-1]
                indexpoint = raw_input('At what index do you wish to place Indel (1 to %s): '%(len(toaddString)))
                try:
                    indexpoint = int(indexpoint)
                except:
                    indexpoint= 0

                if indexpoint<1 or indexpoint>(len(toaddString)):
                    print 'Given input is wrong, Please try again.'
                else:
                    hashlist = list(toaddString)
                    hashlist.insert(indexpoint-1,'-')
                    toaddString = ''.join(hashlist)
                    if stringsel=='1':
                        firstString,secString = getcurrentstring(toaddString,secString)
                    elif stringsel=='2':
                        firstString,secString = getcurrentstring(firstString,toaddString)

        elif selection == 'd':                            
            stringsel = raw_input('Which string to change (1 or 2): ')
            if stringsel!='1' and stringsel!='2':
                print 'Given input is wrong, Please try again.'
            else:
                toaddString = [firstString,secString][int(stringsel)-1]
                indexes = getindexces(toaddString)
                if indexes==[]:
                    print 'No Indels present in the selected string. Please try another option.'
                else:
                    indexpoint = raw_input('At what index do you wish to delete Indel (%s): '%(', '.join(map(str, indexes))))
                    try:
                        indexpoint = int(indexpoint)
                    except:
                        indexpoint= 0

                    if indexpoint<1 or indexpoint not in indexes:
                        print 'Given input is wrong, Please try again.'
                    else:
                        hashlist = list(toaddString)
                        del hashlist[indexpoint-1]
                        toaddString = ''.join(hashlist)
                        if stringsel=='1':
                            firstString,secString = getcurrentstring(toaddString,secString)
                        elif stringsel=='2':
                            firstString,secString = getcurrentstring(firstString,toaddString)

        elif selection == 'q':
            quit_sel = 1

        else:
            print 'Given input is wrong, Please try again.'


mainfunction()
