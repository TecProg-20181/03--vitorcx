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

    print "  ", len(wordlist), "words loaded."

    return wordlist


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

def hangman(secretWord):

    guesses = 8
    lettersGuessed = []
    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print '-------------'

    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:
        print 'You have ', guesses, 'guesses left.'

        available = getAvailableLetters()
        available = popLetterFromString(available, lettersGuessed)

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')

        if letter in lettersGuessed:
            guessed = updateGuessedWord(letter, lettersGuessed, secretWord)
            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in secretWord:
            lettersGuessed.append(letter)
            guessed = updateGuessedWord(letter, lettersGuessed, secretWord)
            print 'Good Guess: ', guessed
        else:
            guesses -=1
            lettersGuessed.append(letter)
            guessed = updateGuessedWord(letter, lettersGuessed, secretWord)
            print 'Oops! That letter is not in my word: ',  guessed
        print '------------'

    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'



wordlist = loadWords()
secretWord = getRandomElement(wordlist).lower()
hangman(secretWord)
