


''' Name: Harish Musthyala,   Date: 03/06/19,   Program Number: 2'''

# input of words
word = input("Enter your string of words : ")
word_list = []
word_list = word.split(" ")
target = input("Enter your target word : ")
position = []
# Logic for finding index 
for x in range(len(word_list)):
    if target == word_list[x]:
        position.append(x)
if len(position) != 0:
    print(position)
else:
    print("Word not found")
