#Adapted from Althoff, C. (2017) 'The Self-Taught Programmer: The Definitive Guide to Programming Professionally'.  
import random

def hm(word):
    #word_list = ["Python", "Java", "computer", "hacker", "painter", "informatica", "good day", "look out"]
    #random_number = random.randint(0, len(word_list) - 1)
    #word = word_list[random_number].lower()
    alpha = ["a", "b", "c", "d", "e", "f", "g","h", "i", "j", "k", "l",\
        "m", "n", "o", "p", "q", "r", \
        "s", "t", "u", "v", "w", "x", "y", "z"]
    wrong = 0
    stages = ["",
              "______     ",
              "|     |    ",
              "|     |    ",
              "|     0    ",
              "|    /|\   ",
              "|    / \   ",
              "|          "]
    rletters = []
    [rletters.append(l) for l in word]
    
    for l in range(len(rletters)):
        if rletters[l] == " ":
            rletters[l] = "_"
    rletters
    word_split = word.split(" ")
    
    letter_board = []
    for l in word_split:
        if l != word_split[-1]:
            letter_board.append("#" * len(l))
            letter_board.append("_") 
        else:
            letter_board.append("#" * len(l))
    letter_board
    display_board = []
    [display_board.append(i) for i in "".join(letter_board)]
    display_board
   
    win = False
    print("Welcome")

    while wrong < len(stages) - 1:
        print((" ".join(display_board)))
        print(" ".join(alpha))
        guess = "Guess a letter. "
        char = input(guess).lower()
        
        try:
            alpha.remove(char)
        except ValueError:
            print("Please try again.")

        if char in rletters:
            while char in rletters:
                cindex = rletters.index(char)
                display_board[cindex] = char
                rletters[cindex] = '$'
        else:
            wrong += 1
        
        #print((" ".join(display_board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))

        if "#" not in display_board: #Ignores the "_"
            print("You win!")
            print(" ".join(word))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose.  It was: {}".format(word))

hm("good day sir")