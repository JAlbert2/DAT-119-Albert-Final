#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 07:53:40 2019

Jonah Albert
5/7/19
Python 1-DAT 119-Spring 2019
Final code
Cipher Tools
"""
print('Begin\n')
cipher = ''#Empty string for working cipher

def freq(cipher):
    freqList = [['','','','','','','','','','','','','','','','','','','','','','','','','',''],
                 ['','','','','','','','','','','','','','','','','','','','','','','','','','']]#,
                 #['','','','','','','','','','','','','','','','','','','','','','','','','','']]
    fInput = []
    try:#Catch for file not existing
        file = open('freq.txt','r')
        fInput = file.readlines()
        file.close()
    except:
        print('freq.txt is missing.')

    for x in range(len(fInput)):
        fInput[x] = fInput[x].rstrip('\n')

    for y in range(len(fInput)):
        holder = fInput[y]
        freqList[0][y] = holder[0].upper()
        freqList[1][y] = holder[2:8].rstrip(':')
        #freqList[2][y] = holder[8:14].strip(':')

    frace = cipher.lower()
    letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
              'n','o','p','q','r','s','t','u','v','w','x','y','z']#Alphabet array
    count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#Count of each letter
    average = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#Average of each letter
    #Checks each letter in the cipher and tallies each letter
    for control in range(len(frace)):
        if (frace[control] == 'a'):
            count[0] += 1
        elif (frace[control] == 'b'):
            count[1] += 1
        elif (frace[control] == 'c'):
            count[2] += 1
        elif (frace[control] == 'd'):
            count[3] += 1
        elif (frace[control] == 'e'):
            count[4] += 1
        elif (frace[control] == 'f'):
            count[5] += 1
        elif (frace[control] == 'g'):
            count[6] += 1
        elif (frace[control] == 'h'):
            count[7] += 1
        elif (frace[control] == 'i'):
            count[8] += 1
        elif (frace[control] == 'j'):
            count[9] += 1
        elif (frace[control] == 'k'):
            count[10] += 1
        elif (frace[control] == 'l'):
            count[11] += 1
        elif (frace[control] == 'm'):
            count[12] += 1
        elif (frace[control] == 'n'):
            count[13] += 1
        elif (frace[control] == 'o'):
            count[14] += 1
        elif (frace[control] == 'p'):
            count[15] += 1
        elif (frace[control] == 'q'):
            count[16] += 1
        elif (frace[control] == 'r'):
            count[17] += 1
        elif (frace[control] == 's'):
            count[18] += 1
        elif (frace[control] == 't'):
            count[19] += 1
        elif (frace[control] == 'u'):
            count[20] += 1
        elif (frace[control] == 'v'):
            count[21] += 1
        elif (frace[control] == 'w'):
            count[22] += 1
        elif (frace[control] == 'x'):
            count[23] += 1
        elif (frace[control] == 'y'):
            count[24] += 1
        elif (frace[control] == 'z'):
            count[25] += 1

    for z in range(len(count)):#Take the average of each value and round to three places
        average[z] = format(count[z] / sum(count) * 100,'.3f')
    final = dict(set(zip(letter,average)))#Make a dictionary

    #Print everything out!
    print('\nFrequency as a percent','Frequency of letters in English',sep = '\t\t')
    print('---------------------------------------------------------------')
    print('A: ' + str(final['a']) + ' ','N: ' + str(final['n']),
          '| A: '+freqList[1][0]+' ','N: '+freqList[1][13], sep = '\t')
    print('B: ' + str(final['b']) + ' ','O: ' + str(final['o']),
          '| B: '+freqList[1][1]+' ','O: '+freqList[1][14],sep = '\t')
    print('C: ' + str(final['c']) + ' ','P: ' + str(final['p']),
          '| C: '+freqList[1][2]+' ','P: '+freqList[1][15],sep = '\t')
    print('D: ' + str(final['d']) + ' ','Q: ' + str(final['q']),
          '| D: '+freqList[1][3]+' ','Q: '+freqList[1][16],sep = '\t')
    print('E: ' + str(final['e']) + ' ','R: ' + str(final['r']),
          '| E: '+freqList[1][4]+' ','R: '+freqList[1][17],sep = '\t')
    print('F: ' + str(final['f']) + ' ','S: ' + str(final['s']),
          '| F: '+freqList[1][5]+' ','S: '+freqList[1][18],sep = '\t')
    print('G: ' + str(final['g']) + ' ','T: ' + str(final['t']),
          '| G: '+freqList[1][6]+' ','T: '+freqList[1][19],sep = '\t')
    print('H: ' + str(final['h']) + ' ','U: ' + str(final['u']),
          '| H: '+freqList[1][7]+' ','U: '+freqList[1][20],sep = '\t')
    print('I: ' + str(final['i']) + ' ','V: ' + str(final['v']),
          '| I: '+freqList[1][8]+' ','V: '+freqList[1][21],sep = '\t')
    print('J: ' + str(final['j']) + ' ','W: ' + str(final['w']),
          '| J: '+freqList[1][9]+' ','W: '+freqList[1][22],sep = '\t')
    print('K: ' + str(final['k']) + ' ','X: ' + str(final['x']),
          '| K: '+freqList[1][10]+' ','X: '+freqList[1][23],sep = '\t')
    print('L: ' + str(final['l']) + ' ','Y: ' + str(final['y']),
          '| L: '+freqList[1][11]+' ','Y: '+freqList[1][24],sep = '\t')
    print('M: ' + str(final['m']) + ' ','Z: ' + str(final['z']),
          '| M: '+freqList[1][12]+' ','Z: '+freqList[1][25],sep = '\t')
    print('\n')


def ceaser(cipher):
    cipher = cipher.lower()
    error = False#Catch for file not existing
    try:
        file = open('mostWords.txt','r')#File is used later to see if cipher is solved
        most = file.readlines()
        file.close()
    except:
        error = True

    if (error == False):
        for x in range(len(most)):#Input formatting
            most[x] = most[x].rstrip('\n')

        #Pre initalized string arrays to handle letter shifting
        pairs = [['a','b','c','d','e','f','g','h','i','j','k','l','m',
                  'n','o','p','q','r','s','t','u','v','w','x','y','z'],
                ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                  'n','o','p','q','r','s','t','u','v','w','x','y','z']]
        holderList = ['','','','','','','','','','','','','','','','','','','','','','','','','','']

        loop = 0#Control Variable. Loop terminates if all combinations have been checked

        solved = False
        while(not solved):
            loop += 1
            for x in range(26):
                if(x == 25):#Last letter goes back to A, Out of bounds if not caught
                    holderList[x] = pairs[1][0]
                else:
                    holderList[x] = pairs[1][x+1]#Shifts letter to next space in holder list

            for y in range(26):#Takes values in holder and resets the main array
                pairs[1][y] = holderList[y]

            key = {}#Empty dictionary to make swapping letters easier
            for j in range(26):
                key[pairs[0][j]] = pairs[1][j]#Fills dictionary

            #Code in changeCipher goes here if everthing breaks

            answer = changeCipher(cipher,key)#Swaps encoded message into decoded message

            score = 0#Score of correctness
            for var in range(len(most)):#Runs words in cipher against top 50 most used words
                if (most[var] in answer):#Runs if a word is in the decoded string
                    score += 1
            if(score >= 4):#Must be four or more words
                solved = True

            if(loop == 27):#Terminates if checks all combinations
                solved=True

        if(loop >= 27):#Tells user of the findings
            print('This cipher cannot be solved by Ceaser Cipher.\n')
        else:
            print('Solved with '+str(score)+' of the top 50 most used words\n')
            print(answer)
            print('\nYou will be redirected to the save menu to save the solution.\n\n')
            save(answer)
    else:
        print('mostWords.txt is missing.')

    return(cipher)#Returns to the menu


def simple(cipher):
    choice = 0#Control variable
    key = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z']#Key to the cipher
    mess = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']#Key pairings

    while(choice == 0):
        final = dict(set(zip(key,mess)))#Makes a dictionary to print

        print('\nPairings')#Prints current pairings
        print('--------')
        print('A: ' + str(final['a']) + ' ','N: ' + str(final['n']), sep='\t')
        print('B: ' + str(final['b']) + ' ','O: ' + str(final['o']), sep='\t')
        print('C: ' + str(final['c']) + ' ','P: ' + str(final['p']), sep='\t')
        print('D: ' + str(final['d']) + ' ','Q: ' + str(final['q']), sep='\t')
        print('E: ' + str(final['e']) + ' ','R: ' + str(final['r']), sep='\t')
        print('F: ' + str(final['f']) + ' ','S: ' + str(final['s']), sep='\t')
        print('G: ' + str(final['g']) + ' ','T: ' + str(final['t']), sep='\t')
        print('H: ' + str(final['h']) + ' ','U: ' + str(final['u']), sep='\t')
        print('I: ' + str(final['i']) + ' ','V: ' + str(final['v']), sep='\t')
        print('J: ' + str(final['j']) + ' ','W: ' + str(final['w']), sep='\t')
        print('K: ' + str(final['k']) + ' ','X: ' + str(final['x']), sep='\t')
        print('L: ' + str(final['l']) + ' ','Y: ' + str(final['y']), sep='\t')
        print('M: ' + str(final['m']) + ' ','Z: ' + str(final['z']), sep='\t')
        print('\n')

        user = input('What would you like to chage(Ex: A=F):')
        while('=' not in user):
            user = input('What would you like to chage(Ex: A=F)[Need the =]:')

        user = user.lower()
        change = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#Used to ensure no doubles

        #main = user[0]
        #switch = user[2]
        find = mess[key.index(user[0])]#Letter that has to be found to be switched
        #replace = mess[key.index(switch)]

        #switch = user[2]
        for letter in range(26):
            #print(mess[letter],user[0],user[2])
            if(mess[letter] == user[2]):
                #If the letter being checked in the key pairings equals what the user stated
                mess[letter] = find.upper()
                #Make the letter in the key pairings the other letter in the switch

        #Executes the change when the user states a change
        if (user[0] == 'a'):
            mess[0] = user[2].upper()
        elif (user[0] == 'b'):
            mess[1] = user[2].upper()
        elif (user[0] == 'c'):
            mess[2] = user[2].upper()
        elif (user[0] == 'd'):
            mess[3] = user[2].upper()
        elif (user[0] == 'e'):
            mess[4] = user[2].upper()
        elif (user[0] == 'f'):
            mess[5] = user[2].upper()
        elif (user[0] == 'g'):
            mess[6] = user[2].upper()
        elif (user[0] == 'h'):
            mess[7] = user[2].upper()
        elif (user[0] == 'i'):
            mess[8] = user[2].upper()
        elif (user[0] == 'j'):
            mess[9] = user[2].upper()
        elif (user[0] == 'k'):
            mess[10] = user[2].upper()
        elif (user[0] == 'l'):
            mess[11] = user[2].upper()
        elif (user[0] == 'm'):
            mess[12] = user[2].upper()
        elif (user[0] == 'n'):
            mess[13] = user[2].upper()
        elif (user[0] == 'o'):
            mess[14] = user[2].upper()
        elif (user[0] == 'p'):
            mess[15] = user[2].upper()
        elif (user[0] == 'q'):
            mess[16] = user[2].upper()
        elif (user[0] == 'r'):
            mess[17] = user[2].upper()
        elif (user[0] == 's'):
            mess[18] = user[2].upper()
        elif (user[0] == 't'):
            mess[19] = user[2].upper()
        elif (user[0] == 'u'):
            mess[20] = user[2].upper()
        elif (user[0] == 'v'):
            mess[21] = user[2].upper()
        elif (user[0] == 'w'):
            mess[22] = user[2].upper()
        elif (user[0] == 'x'):
            mess[23] = user[2].upper()
        elif (user[0] == 'y'):
            mess[24] = user[2].upper()
        elif (user[0] == 'z'):
            mess[25] = user[2].upper()


        #Loop to count the amount of each letter
        for cont in range(len(change)):
            if (mess[cont] == 'a' or mess[cont] == 'A'):
                change[0] += 1
            elif (mess[cont] == 'b' or mess[cont] == 'B'):
                change[1] += 1
            elif (mess[cont] == 'c' or mess[cont] == 'C'):
                change[2] += 1
            elif (mess[cont] == 'd' or mess[cont] == 'D'):
                change[3] += 1
            elif (mess[cont] == 'e' or mess[cont] == 'E'):
                change[4] += 1
            elif (mess[cont] == 'f' or mess[cont] == 'F'):
                change[5] += 1
            elif (mess[cont] == 'g' or mess[cont] == 'G'):
                change[6] += 1
            elif (mess[cont] == 'h' or mess[cont] == 'H'):
                change[7] += 1
            elif (mess[cont] == 'i' or mess[cont] == 'I'):
                change[8] += 1
            elif (mess[cont] == 'j' or mess[cont] == 'J'):
                change[9] += 1
            elif (mess[cont] == 'k' or mess[cont] == 'K'):
                change[10] += 1
            elif (mess[cont] == 'l' or mess[cont] == 'L'):
                change[11] += 1
            elif (mess[cont] == 'm' or mess[cont] == 'M'):
                change[12] += 1
            elif (mess[cont] == 'n' or mess[cont] == 'N'):
                change[13] += 1
            elif (mess[cont] == 'o' or mess[cont] == 'O'):
                change[14] += 1
            elif (mess[cont] == 'p' or mess[cont] == 'P'):
                change[15] += 1
            elif (mess[cont] == 'q' or mess[cont] == 'Q'):
                change[16] += 1
            elif (mess[cont] == 'r' or mess[cont] == 'R'):
                change[17] += 1
            elif (mess[cont] == 's' or mess[cont] == 'S'):
                change[18] += 1
            elif (mess[cont] == 't' or mess[cont] == 'T'):
                change[19] += 1
            elif (mess[cont] == 'u' or mess[cont] == 'U'):
                change[20] += 1
            elif (mess[cont] == 'v' or mess[cont] == 'V'):
                change[21] += 1
            elif (mess[cont] == 'w' or mess[cont] == 'W'):
                change[22] += 1
            elif (mess[cont] == 'x' or mess[cont] == 'X'):
                change[23] += 1
            elif (mess[cont] == 'y' or mess[cont] == 'Y'):
                change[24] += 1
            elif (mess[cont] == 'z' or mess[cont] == 'Z'):
                change[25] += 1


        #print(change)
        #print(change.index(0))

        double = 0#Double letter index
        aught = 0#Missing letter index(Aught means zero)

        for x in range(26):
            if(change[x] == 2):
                double = x#Double equals index of the double letter
            if(change[x] == 0):
                aught = x#Aught equals index of missing letter

        #print(double,aught)
        if (double != 0 and aught != 0):#Only runs if double exists
            for y in range(26):
                if(mess[y].lower() == key[double]):#If the letters are the same
                    if(key[y].lower() != user[0]):#And is not what the user wated to change
                        mess[y] = key[aught].upper()#Change the second part of the flip

        final = dict(set(zip(key,mess)))#Recreates dictionary to be printed

        print('\nPairings')
        print('--------')
        print('A: ' + str(final['a']) + ' ','N: ' + str(final['n']), sep='\t')
        print('B: ' + str(final['b']) + ' ','O: ' + str(final['o']), sep='\t')
        print('C: ' + str(final['c']) + ' ','P: ' + str(final['p']), sep='\t')
        print('D: ' + str(final['d']) + ' ','Q: ' + str(final['q']), sep='\t')
        print('E: ' + str(final['e']) + ' ','R: ' + str(final['r']), sep='\t')
        print('F: ' + str(final['f']) + ' ','S: ' + str(final['s']), sep='\t')
        print('G: ' + str(final['g']) + ' ','T: ' + str(final['t']), sep='\t')
        print('H: ' + str(final['h']) + ' ','U: ' + str(final['u']), sep='\t')
        print('I: ' + str(final['i']) + ' ','V: ' + str(final['v']), sep='\t')
        print('J: ' + str(final['j']) + ' ','W: ' + str(final['w']), sep='\t')
        print('K: ' + str(final['k']) + ' ','X: ' + str(final['x']), sep='\t')
        print('L: ' + str(final['l']) + ' ','Y: ' + str(final['y']), sep='\t')
        print('M: ' + str(final['m']) + ' ','Z: ' + str(final['z']), sep='\t')
        print('\n')

        show = input('Would you like to see the cipher?(y/n)').lower()
        answer = ''
        if ('y' in show):#If a y exists in the user's answer
            answer = changeCipher(cipher,final)
            print(answer)
            #Code in changeCipher goes here if everything breaks

        choice = input('Save?(y/n)').lower()
        if ('y' in choice):
            save(answer)#Saves the user's work in the moment


        choice = input('Return home?(y/n)').lower()
        if ('y' in choice):#Loops if the user wants to loop
            choice = 0


def enterCode():
    option = '0'
    while (option != '1' and option != '2'):#User has to enter a 1 or 2 only
        option = input('Would you like to (1)Enter a code manually or (2)Use code from file:')

    if (option == '1'):#Allows user to enter a code
        cipher = input('Enter code here: ')
    elif(option == '2'):#Reads code from the file
        try:#Catch for the file not existing
            file = open('cipher.txt','r')
            cipher = file.readlines()
            file.close()

            cipher = str(cipher)
            cipher = cipher.lstrip('[').rstrip(']').strip('"')
        except:
            print('cipher.txt does not exist.')
            cipher = enterCode()

    return cipher


def save(cipher):#Saves user's work to a file
    print('Every time you save, a copy is appended to solved.txt. To continue work from another'
          ' session, copy the encoded text you would like to use and paste it into cipher.txt.'
          ' This saves past itterations in case irreperable mistakes are made.')
    file = open('solved.txt','a')
    file.write(cipher)
    file.close()


def changeCipher(cipher, key):
    letters = []
    for z in range(len(cipher)):#Pulls cipher apart into seperate letters
        letters.append(cipher[z])

    for i in range(len(letters)):#Runs through each single letter and changes it per the key
        if (letters[i] == 'a'):
            letters[i] = key['a']
        elif (letters[i] == 'b'):
            letters[i] = key['b']
        elif (letters[i] == 'c'):
            letters[i] = key['c']
        elif (letters[i] == 'd'):
            letters[i] = key['d']
        elif (letters[i] == 'e'):
            letters[i] = key['e']
        elif (letters[i] == 'f'):
            letters[i] = key['f']
        elif (letters[i] == 'g'):
            letters[i] = key['g']
        elif (letters[i] == 'h'):
            letters[i] = key['h']
        elif (letters[i] == 'i'):
            letters[i] = key['i']
        elif (letters[i] == 'j'):
            letters[i] = key['j']
        elif (letters[i] == 'k'):
            letters[i] = key['k']
        elif (letters[i] == 'l'):
            letters[i] = key['l']
        elif (letters[i] == 'm'):
            letters[i] = key['m']
        elif (letters[i] == 'n'):
            letters[i] = key['n']
        elif (letters[i] == 'o'):
            letters[i] = key['o']
        elif (letters[i] == 'p'):
            letters[i] = key['p']
        elif (letters[i] == 'q'):
            letters[i] = key['q']
        elif (letters[i] == 'r'):
            letters[i] = key['r']
        elif (letters[i] == 's'):
            letters[i] = key['s']
        elif (letters[i] == 't'):
            letters[i] = key['t']
        elif (letters[i] == 'u'):
            letters[i] = key['u']
        elif (letters[i] == 'v'):
            letters[i] = key['v']
        elif (letters[i] == 'w'):
            letters[i] = key['w']
        elif (letters[i] == 'x'):
            letters[i] = key['x']
        elif (letters[i] == 'y'):
            letters[i] = key['y']
        elif (letters[i] == 'z'):
            letters[i] = key['z']

    answer = ''
    for k in range(len(letters)):#Splice the cipher back together
        answer += letters[k]
    return answer


def main(cipher):#Main menu
    menu = -1
    while(menu != 0):
        if(cipher == ''):
            cipher = enterCode()#Forces user to enterCode if cipher is emtpy
        print('\n         Menu')
        print('----------------------')
        print('1) Freq Analysis','2) Ceaser Cipher','3) Simple Substitution',
                '4) Enter a code','5) Save your work',sep = '\n')

        error = True
        while(error):#Loops until user enters a number
            try:
                menu = int(input('Enter a number for a menu(0 to exit):'))
                #print('\n')
                error = False#Only runs if user enters a valid number

                if(menu > 5 or menu < 0):#Number out of range
                    print('You entered a number out of the range')
                    error = True
            except:#Runs if an int is not entered
                print('You did not enter a valid number')
                error = True
        #Menu switch
        if(menu == 1):
            freq(cipher)
        elif(menu == 2):
            cipher = ceaser(cipher)
        elif(menu == 3):
            cipher = simple(cipher)
        elif(menu == 4):
            cipher = enterCode()
        elif(menu == 5):
            save(cipher)


if __name__ == "__main__":
    main(cipher)

print('\nEnd')