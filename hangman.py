import random
from wordlist import word_list


def main():
    word=get_word()
    play(word)

def get_word():
    word=random.choice(word_list)
    return word.upper()

def play(word):
    guessed=False
    tries=10
    guessed_letters=[]
    guessed_words=[]
    
    while(not guessed and tries > 0 ):
        guess = input("Give a letter or a word: ").upper()
        print(guess)
        if len(guess)==1:
            if (guess in word):
                guessed_letters.append(guess)
            else:
                    tries-=1
                    print("False guess")
        else:
            if len(guess)==len(word):
                correct_guess=True
                for i in word: 
                    if guess[i]!=word[i]:
                        correct_guess=False
                        print("You are burnt.")
                if correct_guess:
                    print("You won")
                    guessed=True
                else:
                    tries=0       
