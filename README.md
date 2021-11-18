# sneks-and-ladders
Discord based board game, Sneks and Ladders

# intro
This is the code-base for the Discord based game, Sneks and Ladders, as used for season 1.

# development
Written entirely in Python, pulls attributes from PixelBeasts from a csv file, runs as a discord bot, and saves results into a csv.

# log_season1
log_season1.csv is the log file for the first season of Sneks and Ladders. We had a total of 245 beasties roll 622 times. Winner was PixelBeast #2487.

# game details (from game lobby)

Welcome to the game lobby for Sneks and Ladders

This is a text-based board game in Discord where each PixelBeast starts at 0, and rolls dice to move forward with the goal of landing on 100.

There are many spaces on the board that may move you backwards (sneks) or forwards (ladders). For some of these spaces, the amount you move will be determined by a dice roll (where the dice roll is determined by one of the PixelBeasts attributes). Just as a heads up, if you land on 99, you will be bumped back 75 spaces!

Winner will receive a free PixelBeast!

To play, you must read and agree to the rules below by reacting to this message with 🐍 

- To win, you must land on exactly 100. If you roll past 100, you will bounce back that many spaces.
- Each roll is based on the PixelBeast's speed attribute, where you roll a dice between 1 and 3+round(speed/3).
       (eg. if your speed is a 9, your max roll is a 6).
- After each roll, each PixelBeast must rest for (24-endurance/2) hours. (FYI - this is forced)
       (eg. if your endurance is 8, you must wait 20 hours).
- To roll, type "%roll" followed by your PixelBeast number in the play-sneks-and-ladders channel. (eg. %roll 6928)
- Do not roll for other players. (an accident here or there is fine)
- If you own multiple PBs, you may play with all of them.
- You understand that this game is in beta, and may have errors or possibly even have to shut down.
- Any attempts at cheating or hacking will result in immediate banning from the server.
- Most importantly, have fun!

-- 
As context, the goal for this specific game is to (1) get a game out the door quickly and test out some mechanics, (2) give you another reason to keep coming back to this discord, because it's always been about (3) making friends and having fun.
