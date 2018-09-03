import string
#1A
def is_word_guessed(secret_word,letters_guessed):
    ''' This Function is used to check if all the letters guessed are in the secret word, str1 is a blank string used to convert the set of characters in
    letters_guessed into a string to compare it with the secret word'''   
    S1 = set(secret_word)
    S2 = set(letters_guessed)
    
    if (S2.issubset(S1)):
        return True
    else:
        return False

#1B
def get_guessed_word(secret_word,letters_guessed):
    str1 = ''
    returnString =''
    for char in secret_word:
        if char in str1.join(letters_guessed):
            returnString = returnString + (char)
        else:
            returnString = returnString +'_'
    return returnString

#1C
def get_available_letters(letters_guessed):
    str1 = ''
    returnString =''
    for char in string.ascii_lowercase:
        if char not in str1.join(letters_guessed):
            returnString = returnString + (char)
    return returnString
                
def hangman(secret_word):
    
    letters_guessed = []
    print 'The secret word Contains ',len(secret_word),'letters'
    guesses = len(secret_word) - 1
    
    while(guesses>0):
        
        print 'You have ',guesses,'guesses remaining.'
        print 'letters remaining ->',get_available_letters(letters_guessed)
        charinput = list(raw_input('Enter you letter.. --->'))
        letters_guessed = letters_guessed + charinput
        if (is_word_guessed(secret_word, letters_guessed) == True):
            print 'The Word you guessed is in the secret word.'
        else:
            print 'The word you guessed is not in the secret word.'
        
        print(get_guessed_word(secret_word, letters_guessed))
        print'letters remaining ->' ,(get_available_letters(letters_guessed))
        guesses = guesses - 1
        
        print '==============================='
    print 'The letters you guessed are ->',letters_guessed
hangman('hurshwa')   
        
   
        
        