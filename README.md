# Lights-Out
"Lights Out is an electronic game released by Tiger Electronics in 1995.[1] The game consists of a 5 by 5 grid of lights.
When the game starts, a random number or a stored pattern of these lights is switched on. 
Pressing any of the lights will toggle it and the adjacent lights. The goal of the puzzle is to switch all the lights off,
preferably in as few button presses as possible" (WIKIPEDIA)

the function in my code is an implementation of an algorithm solving the game lights out from any board state.
The algorithm has 2 stages:
1. go in an order, through all the lighten buttons, from the top left to the right bottom, and press the button underneath it,
   except the last row, which got no row underneath it.
2. correspondingly to the light which still lightning in the last row, press 1/2 specific buttons in the first row, and repeat stage 2.

the result is a clear plain board. 

the function receive the lighten buttons integers (1-25), and give back the integers of the buttons need to be pressed in order to solve 
the game.
   
