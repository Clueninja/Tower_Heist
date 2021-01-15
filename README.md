# Tower_Heist
A code competition on repl.it, this was my first coding hackathon/ team based competition
Controls:

Player 1 - WASD
Player 2 - Arrow keys
Summary:
Collect coin bags and evade guards while making for the exit of
each floor as fast as possible. Both players need to be in the exit or entrance to go to the next room.If you get to the exit in room 7 the game will crash but you can still compare scores.Guards can lose you after a little
while so being spotted isn't the end for you, however without your comrade its
GAMEOVER, you can still compare scores. Two players are recommended (the only way really) and you can even play
online multiplayer through the repl.it multiplayer!
This game is best played NOT in a new window, just increase the window size on the pygame window and if you want to see the scores the text window too.

The Process:
Made by 5 people over, the whole month. We worked really hard on it during our own time and all our sprites were made in house! So we sincerely hope you enjoy :)

Known issues:

The guard can glitch through walls.
The guard does not change textures while alerted.
Some coins spawn outside the level and inside the walls.
If you attempt to exit on the final level it will crash.
For future:

Firstly we would like to fix the known issues listed above.

We would definitely would like to add more game mechanics (something we are somewhat lacking at the moment) we have a experimental guard dog going currently.
-We would love to add more diverse tiles and rooms in future however this is fairly time consuming.

Credits:
Finn (Programmer)
Sammy (Programmer)
Will (Graphics & room design)
Dan( Graphics & room design)
William (Graphics & room design)

For nerds:

We used a 2D list with the first dimension being the y (the rows), and the items within being the x (the column) and used strings the represent tiles so anyone could create a tile-map and it be automatically created!

We created folders for our characters animation and all files in those folders are
automatically included in the characters animation for example; there might be a walk left folder and if there is only one file inside it it will just display that image when moving left, however you could put in the folder as many images as you want and it will scroll over them only switching after a certain distance, this can be done without any further configuration.
We use the time module to queue events set for the future such as a guard losing interest if he doesn't see a player within 6 seconds.
We use a 2D lists called patrols to control our guard AI with with each list within being a instruction containing three simple components; X direction, Y direction, and length of time traveling at that vector, this means anyone can make a patrol for the project and easily incorporate it into a guard.

No guards were beaten during the making of this game
