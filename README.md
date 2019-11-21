
#  game of the hanged

The first point of the mission is to make a hangman game. I briefly remind the rules, in case: the computer chooses a random word from a list, a word of up to eight letters. The player tries to find the letters composing the word. At each stroke, he grabs a letter. If the letter is in the word, the computer displays the word with the letters already found. Those that are not yet are replaced by stars (*). The player has 8 chances. Beyond, he lost.

We will complicate a little rules by asking the player to give his name at the beginning of the game. This will allow the program to record its score.

The player's score will be simple to calculate: we take the current score (0 if the player has no score already recorded) and, at each game, we add the number of moves remaining as part points. If, for example, I still have three hits when I find the word, I gain three points.
