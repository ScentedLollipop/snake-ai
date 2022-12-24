# snake-ai
Deep Q Learning model for reinforcement learning of a snake game
created with tensorflow

# how to use
set up venv
as of 2022, tensorflow only supprts python 3.7 - 3.10.

this uses python 3.9


install tensorflow, pygame, numpy

run agent.py and wait like 10 mins for a decent model

# the files

snakeenv.py contain the environment. all functions are under one class for easy import to agent.py

agent.py contains the agent. It take several values which indicate the state of the game(food direction, death direction, etc) and passes them to the model
it also controls how the balance between exploration and exploitation changes as the number of games progress. Basically a bridge betweem model and env

model.py contains the model

