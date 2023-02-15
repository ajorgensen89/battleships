# Testing.

## Pylint.
Pylint tool was used to validate my Python Code. It ensured that code being created conformed to certain rules.<br>
It helps with the user experience and understanding of what is written.<br>
It ensured development of code had certain rules to follow. Suggested fixes occured when checking pylint. <br>
One was the use of **col** as a variable name, used when creating the board game's grid. It was not used or unpacked for use again in any instance and pylint raised it as a concern under __Unused Variable__.<br>
![Single variable](images/readme-images/UnusedVcol.png)
To fix this, single underscore **'_'** for a variable name was used. <br>
Variable was not used again in this instance. Only for creating the layout of the board itself.
![Single Underscore](images/readme-images/UnusedVariable.png)