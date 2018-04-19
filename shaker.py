import random

def generateGuess(length):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    guess = ''
    for i in range(length):
        guess += alphabet[random.randrange(length - 1)]
    return guess
    
def compareGuess(guess, phrase):
    return guess == phrase

def matchingScore(phrase, guess):
    matchingCount = 0
    l = len(phrase)
    for i in range(l):
        if phrase[i] == guess[i]:
            matchingCount += 1
    
    return matchingCount / float(l)


def main():
    
    phrase = 'methinks it is like a weasel'
    guess = generateGuess(28)
    bestScore = 0
    score = matchingScore(phrase, guess)
    
    while score < 1.0 :
        if score > bestScore:
            bestScore = score
            print("score: %.4f guess: %s" % (bestScore, guess))
        guess = generateGuess(28)
        score = matchingScore(phrase, guess)

if __name__ == '__main__':
    main()