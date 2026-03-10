import random
import twl
import string 
# A, B, C... Z Counts
Scrabble_Counts = [9,2,2,4,12,2,3,2,9,1,1,4,2,6,8,2,1,6,4,6,4,2,2,1,2,1]
Scrabble_Words = list(twl.iterator())

Counts = []
ALL_words = []
All_Tiles = []

chosen_words = []

def init():
    global Counts
    global ALL_Tiles
    global ALL_words
    global Scrabble_Words
    global Scrabble_Counts

    Counts = Scrabble_Counts.copy()
    ALL_words = Scrabble_Words.copy()

    i = 0
    All_Tiles = []
    for letter in string.ascii_uppercase:
     for j in range(1, Counts[i]+1):
        All_Tiles.append(letter)
     i = i + 1

    reduce_bag()


def show_bag(counts_arr):
    index = 0
    for letter in string.ascii_uppercase:
        print( " " + letter + " ", end = "")
    print()
    for i in range(0,26):
        print(f'{counts_arr[i]:2}' , end = " ")
    print()


def update_counts(word, counts_arr):

    index = 0
    for letter in string.ascii_uppercase:
        #print(letter)
        
        count = word.count(letter)
        if (count > 0):
            #print(letter + ': ', end = "")
            #print(count)
            counts_arr[index] = counts_arr[index] - count

        index = index + 1


def check_word(word):

    global Counts

    if (twl.check(word) == False):
        print(f"according to dictionary {word} is not a word.")
        return False

    word = word.upper()
    counts_copy = Counts.copy()
    update_counts(word, counts_copy)

    for i in range(0,26):
        if (counts_copy[i] < 0):
            return False

    return True

def use_word(word):

    if (check_word(word.lower()) == False):
        print(f'use word {word} failed.')
        return False
    else:
        print(f'Use word {word}')
        update_counts(word, Counts)

    show_bag(Counts)
    reduce_bag()

    return True

def reduce_bag():

    global ALL_words
   
    words = []

    for word in ALL_words:
        if (check_word(word) == True):
            words.append(word)

    ALL_words = words # replace with new list, so working with smaller list
    print(f'{len(ALL_words)} words')

def list_all_words():
    for word in ALL_words:
        print(word)

    print(f'{len(ALL_words)} words')
    

# put n into alphabet count
def put_letter_in_bag(num, bag):
    global All_Tiles

    nletter = All_Tiles[num]
    #print(f'{num} translates to {nletter}')

    # increment_letter_count(letter)
    index = 0
    for letter in string.ascii_uppercase:
        if (letter == nletter):
            bag[index] = bag[index] + 1
        index = index + 1

def remove_word(word):

    global chosen_words

    try:
        chosen_words.remove(word)
        print(f'{word} removed')
        init()

        for word in chosen_words:
            use_word(word)

    except:
        print(f'{word} did not exist')


def menu():
    global chosen_words

    print('-------------------')
    print('l - list all words')
    print('s - show tiles')
    print('c - choose word')
    if (len(chosen_words) > 0):
        print('r - remove word')
    print('q - quit')
    user_input = input("Choice: ")
    return user_input

#--------------------------------------------
def main():

    global Counts
    global chosen_words

    init()
    show_bag(Counts)

    total = sum(Counts)
    print(f"total tiles {total}")
    print(f'{len(ALL_words)} words')

    # ------ main loop -----
    while(True):

        choice = menu()
        print(choice)
        match choice:
            case 'l':
                list_all_words()
            case 's':
                show_bag(Counts)
            case 'c':
                word = input ('Choose word:')
                word = word.upper()
                if (use_word(word) == True):
                    chosen_words.append(word)
                    print(f"words chosen: {chosen_words}")
            case 'r':

                if (len(chosen_words) > 0):
                    word = input ('Remove which word:')
                    word = word.upper()
                    remove_word(word)
                    print(f"words chosen: {chosen_words}")
                else:
                    print('no chosen words yet.')
            case 'q':
                break
            case _:
                print('unknown option {choice}') 

if __name__ == "__main__":
    main()