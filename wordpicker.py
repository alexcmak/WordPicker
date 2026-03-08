import random
import twl
import string 
# A, B, C... Z Counts
Counts = [9,2,2,4,12,2,3,2,9,1,1,4,2,6,8,2,1,6,4,6,4,2,2,1,2,1]

ALL_words = list(twl.iterator())

i = 0
All_Tiles = []
for letter in string.ascii_uppercase:
    for j in range(1, Counts[i]+1):
       All_Tiles.append(letter)
    i = i + 1

#print(All_Tiles)
#print(len(All_Tiles))


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
    else:
        print(f'Use word {word}')
        update_counts(word, Counts)

    show_bag(Counts)
    reduce_bag()

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
    nletter = All_Tiles[num]
    #print(f'{num} translates to {nletter}')

    # increement_letter_count(letter)
    index = 0
    for letter in string.ascii_uppercase:
        if (letter == nletter):
            bag[index] = bag[index] + 1
        index = index + 1

def menu():
    print('-------------------')
    print('l - list all words')
    print('s - show tiles')
    print('c - choose word')
    print('q - quit')
    user_input = input("Choice: ")
    return user_input

#--------------------------------------------
def main():

    global Counts

    show_bag(Counts)

    total = sum(Counts)
    print(f"total tiles {total}")

    start = 1
    stop = total-1
    n = 10

    random_numbers = random.sample(range(start, stop + 1), n)
    random_numbers.sort()
    print(f"Picked {n} tiles.")
    print(random_numbers)

    Bag = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for n in random_numbers:
        put_letter_in_bag(n, Bag)

    show_bag(Bag)

    Counts = Bag
    reduce_bag()

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
                use_word(word)
            case 'q':
                break
            case _:
                print('default ar') 

        
    # list_all_words()

if __name__ == "__main__":
    main()