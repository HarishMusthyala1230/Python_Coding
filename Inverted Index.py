


''' Name: Harish Musthyala,   Date: 03/06/19,   Program Number: 3'''

# input of words
word = input("Enter your string of words : ")
word_list = []
word_list = word.split(" ")

# Null lists for word and position
unique = []
position = []
#Logic for finding unique words in the given strings
for y in word_list:
    if y not in unique:
        unique.append(y)
#Logic for finding index for each word
for y in unique:
    target = y
    for x in range(len(word_list)):
        if target == word_list[x]:
            position.append(x)
    print(y, " : ",position)
    position = []

