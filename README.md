# snake-ai
Deep Q Learning model for reinforcement learning of a snake game
created with pytorch

# how to use
set up venv
as of 2022, pytorch does not support python 3.11 so download 3.10 to venv
install pytorch, pygame, numpy
run agent.py and wait like 10 mins

# the files

snakeenv.py contain the environment. all functions are under one class for easy import to agent.py

agent.py contains the agent. It take several values which indicate the state of the game(food direction, death direction, etc) and passes them to the model
it also controls how the balance between exploration and exploitation changes as the number of games progress. Basically a bridge betweem model and env

model.py contains the model

