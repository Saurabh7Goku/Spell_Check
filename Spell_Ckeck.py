from textblob import TextBlob
words = []
correction = []
again = True

# While loop to continue the loop until user hit keys rather than t/T
while again==True or again == 't' or again =='T':
    user_input = input(f"Enter a to check its spelling: ")

    # Storing user input in a list(words[])
    words.append(user_input)

    #Compairing user words to the TextBlob method for correction
    correction.append(TextBlob(user_input))
    print(f"After Correction: ")

    #using set to remove duplicates
    correction = list(set(correction))
    # to get word from list(correction[])
    # and get the correct spelling
    for i in correction:
        print(i.correct(), sep="")
    print("If continue enter 't/T', else 'N/n'")
    again = input()
