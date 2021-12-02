# zip(*iterables) = aggregate elements fron two or more iterables (list.tuples,sets,etc.)
#                   creates a zip object with paired elements stored in tuples for each element

english = ["Death", "Love","Robots"]
italian = ("Morte", "Amore", "Robot")
german = ["Tod", "Liebe", "Roboter"]

words = list(zip(english,italian,german))

for i in words:
    print(i)
