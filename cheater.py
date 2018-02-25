from Scrabble import wordlist, scores

rack=input("enter the letters")
f=open('sowpods.txt','r')
r=f.read()
#wordlist.append(r.split("\n"))
# try:
#     with open("sowpods.txt", "r") as f:
#         for line in f:
#             wordlist.append('\n')
#
# except EnvironmentError:
#     print("Oops, I couldn't find sowpods.txt.")
#     print("Am I in the right place?")
#     exit(1)

valid_words = []

for word in wordlist:
    valid = True
    rack_letters = list(rack)
    for letter in word:
        if letter not in rack_letters:
            valid = False
            break
        else:
            rack_letters.remove(letter)
    total = 0
    if valid == True:

        for letter in word:
            total = total + scores[letter]
        valid_words.append([total, word])

valid_words.sort()

for i in range(len(valid_words)-1,0,-1):
    entry=valid_words[i]
    score = entry[0]
    word = entry[1]
    print(str(score) + " " + word)