## Description

People love to see their results as they're running to their goal.
So, let's learn how to show the user the score of the game.

When the game starts, the user should enter his/her name. After that, the program should greet the user and read a file named `rating.txt` . This is a file containing current scores for different players. You can see the file format below: it's just lines containing user's name and his/her score divided by a single space.
```
Tim 350
Jane 200
Alex 400
```
If there’s a record for the user with the same name in the file, the program should take his/her rating and use it as a reference point for counting current user’s score (for example, if the user entered name `Tim`, then his score at the start of the game will be 350). If the user's name isn't written in the file, then your program should count user's score from 0.

You don't need to write anything in the `rating.txt` file!

The program should print user's score when the user enters `!rating`. For example, if your rating is 0 then the program should print:
```C
Your rating: 0
```
Your program should add 50 points to the player for every draw, 100 for every win, and nothing for losing.

## Objectives

Your program should:

   1. Output a line `Enter your name: `. Note that the user should enter his/her name on the same line (not the one following the output!)
   2. Read input specifying the user's name and output a new line Hello, <name>
   3. Read a file named `rating.txt` and check if there's a record for the user with the same name; if yes, use the score specified in the `rating.txt` for this user as a starting point for calculating the score in the current game. If no, start counting user's score from 0.
   4. Play the game by the rules defined on the previous stages:
   5. Read user's input
   6. If the input is `!exit`, output `Bye!` and stop the game
   7. If the input is the name of the option, then:
   8. Pick a random option
   9. Output a line with the result of the game in the following format (<option> is the name of the option chosen by the program):
       - Lose -> `Sorry, but the computer chose <option>`
       - Draw -> `There is a draw (<option>)`
       - Win -> `Well done. The computer chose <option> and failed`
   10. For each draw, add 50 point to the score. For each user's win, add 100 to his/her score. In case the user loses, don't change the score.
   11. If the input corresponds to anything else, output `Invalid input`
   12. Play the game again

## Examples

The greater-than symbol followed by space (`>` ) represents the user input. Notice that it's not the part of the input.

### Example 1
```
Enter your name: > Tim
Hello, Tim
> !rating
Your rating: 350
> rock
Sorry, but the computer chose paper
> paper
Well done. The computer chose rock and failed
> scissors
There is a draw (scissors)
> !rating
Your rating: 500
> !exit
Bye!
```
### Example 2
```
Enter your name: > Chuck
Hello, Chuck
> scissors
There is a draw (scissors)
> rock
Well done. The computer chose scissors and failed
> paper
Well done. The computer chose rock and failed
> !rating
Your rating: 250
> !exit
Bye!
```
