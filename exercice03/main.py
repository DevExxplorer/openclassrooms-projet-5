words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]
list = ()

for word in words:
    count = len([char for char in word if char in "aeiouyAEIOUY"])
    list += (word, count)

print(list)