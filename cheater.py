from Scrabble import wordlist, scores

rack=input("enter the letters")
f=open('sowpods.txt','r')
r=f.read()

valid_words = []

for word in wordlist:                                   
    valid = True                                       #initialize valid as true
    rack_letters = list(rack)
    for letter in word: 
        if letter not in rack_letters:
            valid = False                              #if a letter that is in the word but not in the given input thenproceed to next word 
            break
        else:
            rack_letters.remove(letter)                #if letter matches then remove that letter to handle dulplicate letter case
    total = 0
    if valid == True:

        for letter in word:
            total = total + scores[letter]             #if a word is found then calculate corresponding scores from the scores dictionary
        valid_words.append([total, word])

valid_words.sort()                                     #sort according to scores from high to low

for i in range(len(valid_words)-1,0,-1):               #for printing
    entry=valid_words[i]
    score = entry[0]
    word = entry[1]
    print(str(score) + " " + word)
