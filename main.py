def word_count():
    text = (str(input("Écrivez une phrase")))

    print("Le nombre de mots dans votre phrase est de : " + str(len(text.split(" "))))

word_count()