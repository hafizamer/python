import random

def hangman():
    word_list=["Superman","Batman","Flash","Shazam","Cyborg"]
    random_number=random.randint(0,4)
    word=word_list[random_number]
    wrong=0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    
    remain=list(word)
    board=["_"]*len(word)
    win=False
    print("Hangman start")

    while wrong< len(stages)-1:
        print('\n')
        guess=input("Pick a letter")
        if guess in remain:
            char=remain.index(guess)
            board[char]=guess
            remain[char]='$'
        else:
            wrong +=1
        print((' '.join(board)))
        print('\n'.join(stages[0:wrong+1]))
        if '_' not in board:
            print('Correct, it is ')
            print(' '.join(board))
            win= True
            break

    if not win:
        print('\n'.join(stages[0: wrong]))
        print('You lose! The words was {}'.format(word))

hangman()
