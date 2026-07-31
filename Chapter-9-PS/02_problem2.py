'''
2. The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.

'''
import random

def game():
    print("You are playing the game...")
    score = random.randint(1, 89)
    # Fetch the Hiscore
    with open("Hiscore.txt") as f:
        Hiscore = f.read()
        if (Hiscore != ""):
            Hiscore = int(Hiscore)
        else:
            Hiscore = 0

    print(f"Your score: {score}")
    if (score > Hiscore):
        # Write this hiscore in the file
        with open ("Hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()

    
        
