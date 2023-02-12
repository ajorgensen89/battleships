# Battleship Game Created for Python Project.

## Table of Contents.

* [User Experience](#user-experience)
	- [Lucid Chaft](#lucidchart)
* [Data Model](#data-model)
	- [Lucid Chart]
     - [Random Module](#random-module)
* [Game Features](#game-features)
* [Testing](testing.md)
* [Clone Website](#clone-website)
* [Deployment](#deployment)
* [Technologies](#technologies)
<br>

# Data Model.
## Lucid Chart.
## Random Module.
Imported for use in this website was __randomint__ from the random module provided as use within the website from external source.<br>
[Python Random Module](https://www.w3schools.com/python/module_random.asp) for reference.

# Game Features.

## HIT.<br>
Method for showing a hit on a Battleship in combat with a "*" on the game board and a HIT statment.<br>
![HIT image](images/readme-images/HITexample.png)

## MISSED AND BATTLESHIP LOCATION.<br>
Method for showing a miss on a Battleship in combat with a "X" on the game board and a MISSED statment.<br>
Method for showing the Battleship's location is with an "S" on the game board.<br>
![MISSED image](images/readme-images/MISSEDexample.png)

## LOCATION ALREADY TRIED.<br>
If the row and column selected shows on the game board as an "X" already. Then this feature prompts you, it can not place an "X" on thre board, as you have already tried that guess of row and column combination.<br>
You then get prompted that you have lost a turn to find the Battleship.<br>
![ALREADY MISSED]()<br>
I used assitance for the code to correct what I had written. I did try two different methods but could not quite get it to work for this instances.<br>
First try. Within an IF statement.<br>
![FIRST TRY](images/readme-images/IFalready.png)<br>
Second try. I tried to append lists of the guesses given by the player.<br>
![SECOND TRY](images/readme-images/Xalready.png)<br>
End Result from code. See [RtoDto.net.](https://rtodto.net/a-simple-battleship-python-script/) in credit also.<br>
It still has been adapted from the original code source.<br>
Look of the code in its final state for this website.<br>
![FINAL CODE USED](images/readme-images/XalreadyFix.png)


## END OF GAME.<br>
At the end of 5 turns, the Battleship is revealed to the user as an "S" on the game board. With a statement saying the Battleship was to hard to find - GAME OVER.<br> 
Even though you can now see the Battleship on the game board, the co-ordinates of the row and column numbers, are revealed too.<br>
![GAME OVER](images/readme-images/SHIPreveal.png)

## NAME<br>
The player of the game can enter their name. That data is used to show them which board is theirs to play on, showing any hits, misses or the batttleship.
![NAME](images/readme-images/NAMEfeature.png)

## GUESS ROW AND COLUMN.<br>
There is a prompt created for the player to guess a row and column value to try and find the battleship on the board.<br>
An error prompt shows, and the player can put in another valid input for their row and column guesses.
![GUESS PROMPT](images/readme-images/ValidRC.png)

<hr>

# Trial and errors.<br>
## APPENDING LISTS<br>
Tried using Append() method to add a HIT or MISS to the Battleship Board but it was not working correctly. Which lead to it just being added to the list and not changing the current "o" character.<br>
![Append atempt](images/readme-images/Append.board.png)

## READING ROW AND COLUMN OUT OR RANGE.<br>
The selection for a range integer between was between 0 - 4. The code written did not cover this value so it was raising an error. One was needed as a row value and the other as a value for column in the grid for the Battleship game.<br>
**Code -** This would register any number between -1 to 6. Which I did not want. <br>
**random_row = randint(0, len(board))**<br>
**random_column = randint(0, len(board[0]))**<br> 
![Range error](images/readme-images/ERRORrun.png)<br>
This was corrected in the code.<br>
**Corrected code -** This code registered at the 0-4 range I needed<br>
**random_row = randint(1, len(board)) - 1**<br>
**random_column = randint(1, len(board[0])) - 1**<br>

## NO INPUT<br>
If no input for the name is added. It will show as an error.
Used and adapted code from the Love Sandwiches Coursework for validating name input.<br>
This can be numbers, letters or special characters.<br>
For example: Player1 or Bobby. Even @Bobby_BattleShip-game!<br>
https://p3-battleships.herokuapp.com/<br>
![NO INPUT image](images/readme-images/NOINPUTexample.png)
<hr>

# Credits.
1. [Codecadmey](https://www.codecademy.com/courses/learn-python/lessons/battleship/exercises/welcome-to-battleship). Building the battleship game code on this website provided.
<br>

2. [Love Sandwiches Coursework.](https://p3-battleships.herokuapp.com/) Validating name.<br>

3. [RtoDto.net.](https://rtodto.net/a-simple-battleship-python-script/)<br>
Assist with getting a working statment so if the board game was already marked with a 'miss - "X"', then the game would ask you for another row and column choice.

4. [Python Random Module](https://www.w3schools.com/python/module_random.asp) for reference.

# Technologies
[Python Random Module](https://www.w3schools.com/python/module_random.asp) has been used to import a libary of data to use when needing random integers for this website. It helped to create a position for the batlleship in the Battleship game.