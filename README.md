# Game Features.<br>
### HIT.<br>
Method for showing a hit on a Battleship in combat with a "*" and a HIT statment.<br>
![HIT image](images/readme-images/HITexample.png)

### MISSED AND BATTLESHIP LOCATION.<br>
Method for showing a missed on a Battleship in combat with a "X" and a MISSED statment.<br>
Method for showing the Battleship's location is with an "S"<br>
![MISSED image](images/readme-images/MISSEDexample.png)

### END OF GAME.<br>
At the end of 5 turns, the Battleship is revealed to the user as an "S". With a statement saying the Battleship was to hard to find - GAME OVER.<br> 
Even though you can now see the Battleship on the grid, the co-ordinates of the row and column numbers, are revealed too.<br>
![GAME OVER](images/readme-images/SHIPreveal.png)

### NAME<br>
The player of the game can enter their name. That data is used to show them which board is theirs to play on, showing any hits, misses or the batttleship.
![NAME](images/readme-images/NAMEfeature.png)

### GUESS ROW AND COLUMN.<br>
There is a prompt created for the player to guess a row and column value to try and find the battleship on the grid.<br>
An error prompt shows, and the player can put in another valid input for their row and column guesses.
![GUESS PROMPT](images/readme-images/ValidRC.png)

<hr>

# Trial and errors.<br>
### APPENDING LISTS<br>
Tried using Append() method to add a HIT or MISS to the Battleship Board but it was not working correctly. Which lead to it just being added to the list and not changing the current "o" character.<br>
![Append atempt](images/readme-images/Append.board.png)

### READING ROW AND COLUMN OUT OR RANGE.<br>
The selection for a range integer between was between 0 - 4. The code written did not cover this value so it was raising an error. One was needed as a row value and the other as a value for column in the grid for the Battleship game.<br>
**Code -** This would register any number between -1 to 6. Which I did not want. <br>
**random_row = randint(0, len(board))**<br>
**random_column = randint(0, len(board[0]))**<br> 
![Range error](images/readme-images/ERRORrun.png)<br>
This was corrected in the code.<br>
**Corrected code -** This code registered at the 0-4 range I needed<br>
**random_row = randint(1, len(board)) - 1**<br>
**random_column = randint(1, len(board[0])) - 1**<br>

### NO INPUT<br>
If no input for the name is added. It will show as an error.
Used and adapted code from the Love Sandwiches Coursework for validating name input.<br>
This can be numbers, letters or special characters.<br>
For example: Player1 or Bobby. Even @Bobby_BattleShip-game!<br>
https://p3-battleships.herokuapp.com/<br>
![NO INPUT image](images/readme-images/NOINPUTexample.png)
<hr>

# Credits.
1. Codecadmey. Building the battleship game code on this website provided.
https://www.codecademy.com/courses/learn-python/lessons/battleship/exercises/welcome-to-battleship
<br>
2. Love Sandwiches Coursework. Validating name.
https://p3-battleships.herokuapp.com/