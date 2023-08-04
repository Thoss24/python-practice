display = []

word = 'helloworld'

for i in range(len(word)):
    display += "_"

letter = input("Choose word")

for j in range(len(word)):
    if word[j] == letter:
        display[j] = letter

print(display)