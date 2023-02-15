# Battleship Game Created for Python Project.
This Python Coded project is based on a long running game called Battlehships. The essence of this game is played with two players.<br>
It can be played one vs computer on many different platforms or advanced into a multiplayer game on a computer or on a boardgame.<br>
Each player, which can include an Artificial Intelligence(AI), has a Battleship which they place on a board, for the other player to find and sink.<br>
The way to find and sink the Battleship is by taking it in turns to guess a Row and a Column to make a co-ordinate on that board.<br>
If the players combined row and column guessed co-ordinate, is correct, the Battleship is found.<br>
The first player to sink the Battleship is the winner.<br>
The oringal boardgame Battleships also offers different size ships, so you have to hit a combination of points on the board before the Battleship sinks.<br>
The Battleship can also be part of a larger fleet, meaning you and your opponent have more Battleships to sink before winning.

## Table of Contents.

* [User Experience](#user-experience)
* [Flow Chart](#flow-chart)
	- [Lucid Chart](#lucid-chart)
* [Game Features](#game-features)
* [Trial and Errors](#trial-and-errors)
* [Testing](testing.md)
* [Clone Website](#clone-website)
* [Credits](#credits)
* [Technologies](#technologies)
     - [Module](#module)
* [Deployment](#deployment)
<br>

# Flow Chart.
## Lucid Chart.
I used [Lucid Chart](https://www.lucidchart.com/pages/) to create a flow chart of how to create a battleship game.
1. Start - welcome message
2. User name input - raises an error if no input is submitted and loops untill there is input.
3. Select Row:Column for grid - Select the numbers between 0-4 for both row and column. The input should be validated if guessed before or invalid. You would have to try again.
4. 
5.
6. <br>
![Lucid Chart](images/readme-images/LucidChart.png)



[Back to the top](#battleship-game-created-for-python-project)

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
A prompted is given to show you have tried that row and column combination already and to try again.<br>
![ALREADY MISSED](images/readme-images/AiandPreg.png)<br>
The AI would also have a prompt and the user can take appropriate action too.<br>
![AI Guess](images/readme-images/AIReguess.png)<br>
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

## VALIDATING INPUT.<br>
Validating input became abit of trail and error in itself, to find the best approach, for creating code to test that certain input was valid. It is an important feature to this website to ensure the player or an AI can play correctly wihtout crashing the game.<br>
For the 'name'. It checked the **input** entry was not empty before continuing with the next part of the code.<br>
The **input** for validating entry for certain prompts needed to checked differently. It needed to be an integer, aswell as, being an integer form a particular range.<br>
The range for this website, was the size of the boardgame.<br>
If the placement of a Battleship or, a guessed row or colum entry was an integer, it still needed to be within a range to play the game and make enteries on the boards provided.<br>
To see how this was tested click to view the [Testing](testing.md) file here.


<hr>

[Back to the top](#battleship-game-created-for-python-project)

# Trial and Errors.<br>
### APPENDING LISTS<br>
Tried using Append() method to add a HIT or MISS to the Battleship Board but it was not working correctly. Which lead to it just being added to the list and not changing the current "o" character signifying grid points at this point.<br>
![Append atempt](images/readme-images/Append.board.png)

### WRONG RANDOM NUMBER GENERATED.<br>
The selection for a range integer is between 0 - 4. The code written did not cover this value so it was raising an error.<br>
This would register any number between -1 to 6. Which I did not want. <br>
**Incorrect code -**
**Code - ai_ship_row = randint(0, len(ai_board))**<br>
**Code - ai_ship_col = randint(0, len(ai_board[0]))** <br> 
![Range error](images/readme-images/ERRORrun.png)<br>

This was corrected in the code.<br>
**Corrected code -** 
**Code - ai_ship_row = randint(1, len(ai_board)) - 1**<br>
**Code - ai_ship_col = randint(1, len(ai_board[0])) - 1**<br>
This code registered at the 0-4 range I needed<br>

### NO INPUT<br>
If no input for the name is added. It will show as an error.
Used and adapted code from the Love Sandwiches Coursework for validating name input.<br>
This can be numbers, letters or special characters.<br>
For example: Player1 or Bobby. Even @Bobby_BattleShip-game!<br>
https://p3-battleships.herokuapp.com/<br>
![NO INPUT image](images/readme-images/NOINPUTexample.png)
<hr>

### CHANGE IF - TUTOR SUPPORT

![]()


<hr>

[Back to the top](#battleship-game-created-for-python-project)


# Deployment



[Back to the top](#battleship-game-created-for-python-project)

<hr>

# Technologies

## Module.
Imported for use in this website was __randomint__ from the random module provided as use within the website from external source.<br>
[Python Random Module](https://www.w3schools.com/python/module_random.asp) has been used to import a libary of data to use when needing random integers for this website. It helped to create a position for the batlleship in the Battleship game.

## Python Tutor.
[Python Tutor](https://pythontutor.com/visualize.html). Helps to test, run and visualize parts of code.


[Back to the top](#battleship-game-created-for-python-project)

<hr>

# Credits.

1. [Codecadmey](https://www.codecademy.com/courses/learn-python/lessons/battleship/exercises/welcome-to-battleship). I ran through and completed this example of building the battleship game code on this website provided. It had useful prompts and helped improve my understanding to create the code for the website.<br>
Adapted to suit what it was needed for.
<br>

2. [Love Sandwiches Coursework.](https://p3-battleships.herokuapp.com/) Validating name.<br>

3. [RtoDto.net.](https://rtodto.net/a-simple-battleship-python-script/)<br>
Assist with getting a working statment so if the board game was already marked with a 'miss - "X"', then the game would ask you for another row and column choice. Adapted to suit what it was needed for.

4. [Python Random Module](https://www.w3schools.com/python/module_random.asp) for reference.

5. A method from[Stack Overflow](https://stackoverflow.com/questions/41718538/how-do-i-insert-a-restart-game-option) to restart the game. Adapted to suit this website.

6. [Single underline _](https://programming.vip/docs/underline-double-underline-in-python.html). Method used suggested by this site to improve on Pylint suggestions.

7. [101 Computing](https://www.101computing.net/number-only/) Helped with an exmaple of validating input. Adapted to suit what it was needed for.

8. [Largest](https://largest.org/technology/battleships/) provided an image of a Battleship.

<hr>

[Back to the top](#battleship-game-created-for-python-project)

<hr>