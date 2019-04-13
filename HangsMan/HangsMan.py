import random
import sys
import os
from getch import getch, pause

wordList = [
"fallout", "skyrim", "anthem", "battlegrounds", "battlefield", "uncharted", "redemption", "fortnite", 
"minecraft", "destiny", "zelda", "forza", "odyssey", "warcraft", "overwatch", "division", "innocence", 
"brotherhood", "rainbow", "cyberpunk", "dishonored", "witcher"
           ]




def beginning():
    os.system("cls")
    welcome= """



             _____                      _____                      _____            _____           _______         
            /\    \                    /\    \                    /\    \          /\    \         /::\    \        
           /::\____\                  /::\    \                  /::\____\        /::\____\       /::::\    \       
          /:::/    /                 /::::\    \                /:::/    /       /:::/    /      /::::::\    \      
         /:::/    /                 /::::::\    \              /:::/    /       /:::/    /      /::::::::\    \     
        /:::/    /                 /:::/\:::\    \            /:::/    /       /:::/    /      /:::/~~\:::\    \    
       /:::/____/                 /:::/__\:::\    \          /:::/    /       /:::/    /      /:::/    \:::\    \   
      /::::\    \                /::::\   \:::\    \        /:::/    /       /:::/    /      /:::/    / \:::\    \  
     /::::::\    \   _____      /::::::\   \:::\    \      /:::/    /       /:::/    /      /:::/____/   \:::\____\ 
    /:::/\:::\    \ /\    \    /:::/\:::\   \:::\    \    /:::/    /       /:::/    /      |:::|    |     |:::|    |
   /:::/  \:::\    /::\____\  /:::/__\:::\   \:::\____\  /:::/____/       /:::/____/       |:::|____|     |:::|    |
   \::/    \:::\  /:::/    /  \:::\   \:::\   \::/    /  \:::\    \       \:::\    \        \:::\    \   /:::/    / 
    \/____/ \:::\/:::/    /    \:::\   \:::\   \/____/    \:::\    \       \:::\    \        \:::\    \ /:::/    /  
             \::::::/    /      \:::\   \:::\    \         \:::\    \       \:::\    \        \:::\    /:::/    /   
              \::::/    /        \:::\   \:::\____\         \:::\    \       \:::\    \        \:::\__/:::/    /    
              /:::/    /          \:::\   \::/    /          \:::\    \       \:::\    \        \::::::::/    /     
             /:::/    /            \:::\   \/____/            \:::\    \       \:::\    \        \::::::/    /      
            /:::/    /              \:::\    \                 \:::\    \       \:::\    \        \::::/    /       
           /:::/    /                \:::\____\                 \:::\____\       \:::\____\        \::/____/        
           \::/    /                  \::/    /                  \::/    /        \::/    /         ~~              
            \/____/                    \/____/                    \/____/          \/____/                          """
    print(welcome)
    pause("")
    os.system("cls")
    ready= """
    .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
   | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
   | |  _______     | || |  _________   | || |      __      | || |  ________    | || |  ____  ____  | |
   | | |_   __ \    | || | |_   ___  |  | || |     /  \     | || | |_   ___ `.  | || | |_  _||_  _| | |
   | |   | |__) |   | || |   | |_  \_|  | || |    / /\ \    | || |   | |   `. \ | || |   \ \  / /   | |
   | |   |  __ /    | || |   |  _|  _   | || |   / ____ \   | || |   | |    | | | || |    \ \/ /    | |
   | |  _| |  \ \_  | || |  _| |___/ |  | || | _/ /    \ \_ | || |  _| |___.' / | || |    _|  |_    | |
   | | |____| |___| | || | |_________|  | || ||____|  |____|| || | |________.'  | || |   |______|   | |
   | |              | || |              | || |              | || |              | || |              | |
   | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
   '----------------'  '----------------'  '----------------'  '----------------'  '----------------' """
    print(ready)
    pause("")
    to= """




                                                                               .----------------.  .----------------. 
                                                                              | .--------------. || .--------------. |
                                                                              | |  _________   | || |     ____     | |
                                                                              | | |  _   _  |  | || |   .'    `.   | |
                                                                              | | |_/ | | \_|  | || |  /  .--.  \  | |
                                                                              | |     | |      | || |  | |    | |  | |
                                                                              | |    _| |_     | || |  \  `--'  /  | |
                                                                              | |   |_____|    | || |   `.____.'   | |
                                                                              | |              | || |              | |
                                                                              | '--------------' || '--------------' |
                                                                              '----------------'  '----------------' """
    print(to)
    pause("")
    os.system("cls")
    skull= """




                                                    ...
                                                  ;::::;
                                                ;::::; :;
                                               ;:::::'   :;
                                              ;:::::;     ;.
                                              ,:::::'       ;           OOO
                                              ::::::;       ;          OOOOO
                                              ;:::::;       ;         OOOOOOOO
                                             ,;::::::;     ;'         / OOOOOOO
                                           ;:::::::::`. ,,,;.        /  / DOOOOOO
                                         .';:::::::::::::::::;,     /  /     DOOOO
                                        ,::::::;::::::;;;;::::;,   /  /        DOOO
                                       ;`::::::`'::::::;;;::::: ,#/  /          DOOO
                                       :`:::::::`;::::::;;::: ;::#  /            DOOO
                                       ::`:::::::`;:::::::: ;::::# /              DOO
                                       `:`:::::::`;:::::: ;::::::#/               DOO
                                       :::`:::::::`;; ;:::::::::##                OO
                                       ::::`:::::::`;::::::::;:::#                OO
                                       `:::::`::::::::::::;'`:;::#                O
                                        `:::::`::::::::;' /  / `:#
                                         ::::::`:::::;'  /  /   `#
"""
    print(skull)
    pause("")

beginning()


def newFunc():
    global player_name
    os.system("cls")
    print("""\n\n\n\n\n
   |     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~           [ ABOUT ]          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     |

         PROJECT NAME: HangMan Game
         DATE: 07 October 2018, TIME: 12:06:20
         GROUP NUMBER: 14
         SEMESTER: 3rd,  YEAR: 2018

         ----------------------------        -------   GROUP MEMBERS   -------        -------------------------

         ------------------------------------------------------------------------------------------------------
         ROLL NO.         | NAME                           | ENEOLLMENT NO.                  | REGISTRATION NO.
         ------------------------------------------------------------------------------------------------------
                      53. | Atanu Das                      |                  12017009001328 |  304201700900175
                      54. | Nitesh Fatepuria               |                  12017009001416 |  304201700900381
                      55. | Somdeep Jana                   |                  12017009001009 |  304201700900661
                      56. | Soumodip Roy                   |                  12017009001422 |  304201700900677

   |     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     |
    """)
    pause("")
    os.system("cls")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n       Every word you will get here are the names of some video games. Let's see how many games have you played")
    pause("")
    os.system("cls")
    print("\n\n\n\n\n\n\n\n\n\n                                    Well, it's perfect moment to play some Hangman!\n")

    player_name= input("\n                                    What's your Name: ")

def hint(word_check):
    global h1, h2, h3
    if word_check== 'fallout':
        h1= "Creation Engine"
        h2= "MMORPG Version was Cancelled"
        h3= "Vault-Tec Corporation"

    elif word_check== 'skyrim':
        h1= "Fus ro dah"
        h2= "Dovahkiin"
        h3= "Game of The Year 2011"

    elif word_check== 'anthem':
        h1= "The JAVELIN EXOSUITS"
        h2= "The FREELANCERS"
        h3= "Our World my Story"

    elif word_check== 'battlegrounds':
        h1= "Created by Brendan Greene"
        h2= "Inspired by Film Battle Royale"
        h3= "Full name comes from uncertainty of creator identity"

    elif word_check== 'battlefield':
        h1= "Of 120 generals present at Gettysburg, nine were killed or mortally wounded during the battle"
        h2= "The Plot Involves U.S. Soldiers Trying to Escape From Shanghai"
        h3= "The First War-Game to be released with RTX"

    elif word_check== 'uncharted':
        h1= 'Nathan Morgan the Real'
        h2= 'Preceded by Drakes Deception'
        h3= 'A Thiefs End'

    elif word_check== 'redemption':
        h1= "Play as Arthur Marston"
        h2= "John Marsh is also included in the game"
        h3= "Red Dead Camp is your games home"

    elif word_check== 'fortnite':
        h1= "One of the EPIC GAMES"
        h2= "Unreal Engine"
        h3= "Similar to Hunger Games"

    elif word_check== 'minecraft':
        h1= "8-bit ALU"
        h2= "Sandbox video game"
        h3= "Creepers began as a Codding Error"

    elif word_check== 'destiny':
        h1= "The Taken King"
        h2= "First Teased in Halo 3: ODST"
        h3= "That Wizard came from the Moon!"

    elif word_check== 'zelda':
        h1= "The Legend of"
        h2= "Breath of the Wild"
        h3= "Game of the year 2017"

    elif word_check== 'forza':
        h1= "Horizon 4"
        h2= "Motorsport 7"
        h3= "Horizon 3 is a Microsoft Exclusive"

    elif word_check== 'odyssey':
        h1= "One of two major ancient Greek epic poems attributed to Homer"
        h2= "First RPG game in the long franchise"
        h3= "Science fiction game based on Historical Events"

    elif word_check== 'warcraft':
        h1= "Orcs & Humans"
        h2= "Tides of Darkness"
        h3= "Reign of Chaos"

    elif word_check== 'division':
        h1= "Set in New York after a deadly virus has spread throughout the city"
        h2= "Developed on Ubisoft’s Snow Drop engine"
        h3= "Tom Clancy's"

    elif word_check== 'innocence':
        h1= "Unstoppable swarms of rats incarnating the Black Death"
        h2= "14th century France, a dark time for protagonists Amicia and her little brother Hugo"
        h3= "A Plague Tale"

    elif word_check== 'brotherhood':
        h1= "Plot 1503 ROME"
        h2= "Ezio Auditore"
        h3= "Pieces of eden"

    elif word_check== 'rainbow':
        h1= "Six"
        h2= "Fictional international counter-terrorist unit "
        h3= "Tom Clancy’s"

    elif word_check== 'cyberpunk':
        h1= "2020"
        h2= "Combination of lowlife and high tech"
        h3= "Pen-and-Paper Role-Playing-Game"

    elif word_check== 'dishonored':
        h1= "Corvo Attano"
        h2= "Revenge Solves Everything"
        h3= "No Honour"

    elif word_check== 'witcher':
        h1= "Game of The Generation"
        h2= "Andrzej Sapkowski"
        h3= "Most Number of Game of The Year awarded game"



def game_display(guess_number, hint_numb):
    os.system("cls")
    print("\n\n                                                                                             Player: ", player_name)
    print("   ------------------------------------------------------------------------------------------------------------------")
    
    if hint_numb== 0:
        print("\n                                         No Hint Taken, enter 0 to take one                                                    ")
    elif hint_numb== 1:
        print("\n    Hint[1]: ", h1)
    elif hint_numb== 2:
        print("\n    Hint[1]: ", h1)
        print("\n    Hint[2]: ", h2)
    elif hint_numb== 3:
        print("\n    Hint[1]: ", h1)
        print("\n    Hint[2]: ", h2)
        print("\n    Hint[3]: ", h3)

    print("\n   ------------------------------------------------------------------------------------------------------------------\n")
    print("    Guess Left: ",length_word- 2- guess_number,"                                                                                  Guess Taken: ", guess_number)
    print("    Guess Characters: ", guessed_letterwrong)
    print("\n   ------------------------------------------------------------------------------------------------------------------\n")
    print("\n    Word State: ", guess_word)
    print("\n\n   ------------------------------------------------------------------------------------------------------------------\n\n")

def game_end(end_state, guess_take, hint_take):
    os.system("cls")
    if end_state== 'lost':
        print("""	
                                       @@@@@                                        @@@@@
                                      @@@@@@@                                      @@@@@@@
                                      @@@@@@@           @@@@@@@@@@@@@@@            @@@@@@@
                                       @@@@@@@@       @@@@@@@@@@@@@@@@@@@        @@@@@@@@
                                           @@@@@     @@@@@@@@@@@@@@@@@@@@@     @@@@@
                                             @@@@@  @@@@@@@@@@@@@@@@@@@@@@@  @@@@@
                                               @@  @@@@@@@@@@@@@@@@@@@@@@@@@  @@
                                                  @@@@@@@    @@@@@@    @@@@@@
                                                  @@@@@@      @@@@      @@@@@
                                                  @@@@@@      @@@@      @@@@@
                                                   @@@@@@    @@@@@@    @@@@@
                                                    @@@@@@@@@@@  @@@@@@@@@@
                                                     @@@@@@@@@@  @@@@@@@@@
                                                  @@   @@@@@@@@@@@@@@@@@   @@
                                                 @@@@  @@@@ @ @ @ @ @@@@  @@@@
                                                @@@@@   @@@ @ @ @ @ @@@   @@@@@
                                              @@@@@      @@@@@@@@@@@@@      @@@@@
                                            @@@@          @@@@@@@@@@@          @@@@
                                         @@@@@              @@@@@@@              @@@@@
                                        @@@@@@@                                 @@@@@@@
                                         @@@@@                                   @@@@@
        """)
    elif end_state== 'win':
        print("""
                                                      ,~.
                                                   ,-'__ `-,
                                                  {,-'  `. }              ,')
                                                 ,( a )   `-.__         ,',')~,
                                                <=.) (         `-.__,==' ' ' '}
                                                  (   )                      /)
                                                   `-'\   ,                    )
                                                      |  \        `~.        /
                                                      \   `._        \      /
                                                       \     `._____,'    ,'
                                                        `-.             ,'
                                                           `-._     _,-'
                                                               77jj'
                                                              //_||
                                                           __//--'/`
                                                             ,--'/`""")
        print("""
 .----------------.  .----------------.  .-----------------. .-----------------. .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  ________    | || |     _____    | || | ____  _____  | || | ____  _____  | || |  _________   | || |  _______     | |
| | |_   ___ `.  | || |    |_   _|   | || ||_   \|_   _| | || ||_   \|_   _| | || | |_   ___  |  | || | |_   __ \    | |
| |   | |   `. \ | || |      | |     | || |  |   \ | |   | || |  |   \ | |   | || |   | |_  \_|  | || |   | |__) |   | |
| |   | |    | | | || |      | |     | || |  | |\ \| |   | || |  | |\ \| |   | || |   |  _|  _   | || |   |  __ /    | |
| |  _| |___.' / | || |     _| |_    | || | _| |_\   |_  | || | _| |_\   |_  | || |  _| |___/ |  | || |  _| |  \ \_  | |
| | |________.'  | || |    |_____|   | || ||_____|\____| | || ||_____|\____| | || | |_________|  | || | |____| |___| | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' """)
    pause("")
    os.system("cls")
    print("\n\n\n\n\n\n\n   ------------------------------------------------------------------------------------------------------------------\n\n")
    print("                                                          summary\n")
    print("    player: ", player_name)
    print("\n    Guess Taken: ", guess_take, "                                                                                  Hint Taken: ", hint_take)
    if end_state== "lost":
        print("\n\n                                             Correct Word: ", secretWord)
        print("\n   ------------------------------------------------------------------------------------------------------------------")
        print("\n\n    Better Luck Next Time........")
    elif end_state== "win":
        print("\n\n                                                congratulations")
        print("\n   ------------------------------------------------------------------------------------------------------------------")
        print("\n\n    See You Next Time........")

def guessing():

    guess_taken = 0
    hint_taken= 0

    for character in secretWord:
        guess_word.append("-")

    while guess_taken < length_word- 2:

        game_display(guess_taken, hint_taken)
        guess = input("\n    Take a Guess: ").lower()

        if len(guess)>1:
            if guess== secretWord:
                game_end("win", guess_taken, hint_taken)
                break
            else:
                guess_taken+= 1
                continue
        elif guess in guess_word and len(guess)== 1:
            continue
        elif guess in guessed_letterwrong and len(guess)== 1:
            continue
        elif guess== '0' and hint_taken== 0:
            hint_taken= 1
            continue
        elif guess== '0' and hint_taken== 1:
            hint_taken= 2
        elif guess== '0' and hint_taken== 2:
            hint_taken= 3
        else: 
            if guess in secretWord:
                for x in range(0, length_word):
                    if secretWord[x] == guess:
                        guess_word[x] = guess
                guess_taken += 1
            else:
                guessed_letterwrong.append(guess)
                guess_taken += 1
        if guess_taken == length_word-2:
            game_end("lost", guess_taken, hint_taken)
    pause("")


while True:
    guess_word = []
    secretWord = random.choice(wordList)
    hint(secretWord)
    length_word = len(secretWord)
    guessed_letterwrong= []
    newFunc()
    guessing()
    print("Game Over!")