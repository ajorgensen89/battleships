
Making a choice.
https://www.codecademy.com/courses/learn-python/lessons/battleship/exercises/welcome-to-battleship

Trial and Errors.<br>
Tried using Append() method to add a HIT or MISS to the Battleship Board but it was not working correctly as I had not identified the user's guess for row and column are in separate lists. It lead to it just being added to the list and not changing the current "o" character which makes the hidden board.<br>
![Append atempt](images/readme-images/Append.board.png)

HIT.<br>
Method for showing a hit on a Battleship in combat.<br>
![HIT image](images/readme-images/HITexample.png)


# Create empty list to store the game's board.
board = []
computer = []

from collections import Counter
list = [1, 2, 3, 4]
ob = Counter(list)
items = ob.items()
for i in items:
     print(i)
 
