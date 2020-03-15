# Belief Desire Intention Model
An intelligent agent that predicts various sequence of plot-points in an interactive narrative Inform7 game. We have taken a scenario of day-2 of the game Anchorhead. The plot points of this storyline have been included in the following dictionaries. These dictionaries are modeled based on requirements of the story as mentioned in the paper. This prototype tries to model the behavior of a human player by predicting the correct sequence of actions that are required to reach to a particular end-point- expected by the author. There are two end points in the story- 'see_evil_god' and 'discover_book_in_sewer'.

This program is developed in a way to ensure that every pre-requisite condition is met before the agent adds the plot point to the list of discovered plot points. If the agent reaches a dead-end, it starts from another plot point which has not been discovered yet.

### Instructions  
Run the python script and enter a choice from the given alternatives. The program will automatically generate a
correct sequence of actions in order to resemble a real player. No additional dependencies need to be installed.
