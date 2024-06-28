# About

## First attempt at testing

__2024-06-28:__

Ran into an issue where importing the same variable (here: `GLOB_VAR` 
in `source.py`) resultet in the first update not showing up when the second
file import `GLOB_VAR` where going to use the global variable.

After initial testing here I seem to be unable to replicate the issue.
It could be due to how the script was run. I suspect this version is far less
complex than the case where the issue occurred.
