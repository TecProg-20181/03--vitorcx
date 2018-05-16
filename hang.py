# -*- coding: utf-8 -*-
import random
import string

WORDLIST_FILENAME = "words.txt"

def getRandomElement(wordlist):
    return random.choice(wordlist)

def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."

    noBuffering = 0;
    readMode = 'r';
    inputFile = open(WORDLIST_FILENAME, readMode, noBuffering)

    line = inputFile.readline()
    wordlist = string.split(line)
    wordsAmount = len(wordlist)

    print "  ", wordsAmount, "words loaded."

    return wordlist

def setDifficulty():
    print 'Choose the game difficulty:'
    print '0 - Easy'
    print '1 - Medium'
    print '2 - Hard'
    difficulty = input()
    return difficulty

def handleDifficulty(difficulty, guesses):
    EASY = 0
    MEDIUM = 1
    HARD = 2
    if difficulty == EASY:
        guesses[0] = 12
    elif difficulty == MEDIUM:
        guesses[0] = 10
    elif difficulty == HARD:
        guesses[0] = 8

def isWordGuessed(secretWord, lettersGuessed):
    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False
    return True

def getAvailableLetters():
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase
    return available

def popLetterFromString(availableLetters, lettersGuessed):
    for letter in availableLetters:
        if letter in lettersGuessed:
            availableLetters = availableLetters.replace(letter, '')
    return availableLetters

def updateGuessedWord(letter, lettersGuessed, secretWord):
    guessed = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_ '
    return guessed

def handleGuessedLetter(letter, lettersGuessed, secretWord, guesses):
    if letter in lettersGuessed:
        #Letter already guessed
        guessed = updateGuessedWord(letter, lettersGuessed, secretWord)
        print 'Oops! You have already guessed that letter: ', guessed
    elif letter in secretWord:
        #Success guess
        guesses[0] -=1
        lettersGuessed.append(letter)
        guessed = updateGuessedWord(letter, lettersGuessed, secretWord)
        print 'Good Guess: ', guessed
    elif len(letter) >1:
        print 'Please guess only one letter per guess!'
    else:
        #Fail guess
        guesses[0] -=1
        lettersGuessed.append(letter)
        guessed = updateGuessedWord(letter, lettersGuessed, secretWord)
        print 'Oops! That letter is not in my word: ',  guessed

def hangman(secretWord):
    difficulty = setDifficulty()
    guesses = [8]
    handleDifficulty(difficulty, guesses)
    lettersGuessed = []
    secretWordSize = len(secretWord)
    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', secretWordSize, ' letters long.'
    print '-------------'

    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses[0] >0:
        print 'You have ', guesses[0], 'guesses left.'

        available = getAvailableLetters()
        available = popLetterFromString(available, lettersGuessed)

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        handleGuessedLetter(letter, lettersGuessed, secretWord, guesses)
        print '------------'

    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'



wordlist = loadWords()
secretWord = getRandomElement(wordlist).lower()
hangman(secretWord)
