# Skyler Martens and Evan Ko
# May 30, 2017
# CSE 415 Final Project

import MDP, Rubiks_Cube, Test_Rubiks

def displayOptimalPolicy(world):
    world.extractPolicy()
    for key, value in world.optPolicy.items():
        print(key, value)



def test():
    '''Create the MDP, then run an episode of random actions for 10 steps.'''
    rubiks_MDP = MDP.MDP()
    setup = False
    print("Welcome to Skyler and Evan's Pocket Cube solver")
    answer = input("Since setup and solving takes a bit would you like to setup the problem before running? (y/n) ")
    # while answer != "y" or answer != "n":
    #     print(answer)
    #     answer = input("Since setup and solving takes a bit would you like to setup the problem before running? (y/n) ")
    if answer == 'y': #the user only wants to setup and not solve at the moment
        setup = True
        rubiks_MDP.register_start_state(Test_Rubiks.createInitialState())
        rubiks_MDP.register_actions(Test_Rubiks.ACTIONS)
        rubiks_MDP.register_operators(Test_Rubiks.OPERATORS)
        rubiks_MDP.generateAllStates()
    if answer == 'n': #the user wants to setup and solve the problem
        #run normally
        rubiks_MDP.register_start_state(Test_Rubiks.createInitialState())
        rubiks_MDP.register_actions(Test_Rubiks.ACTIONS)
        rubiks_MDP.register_operators(Test_Rubiks.OPERATORS)
        rubiks_MDP.generateAllStates()
        # print("Total number of generated states: " + str(len(rubiks_MDP.known_states)))
        rubiks_MDP.register_transition_function(Test_Rubiks.T)
        rubiks_MDP.register_reward_function(Test_Rubiks.R)
        #rubiks_MDP.random_episode(1000)
        rubiks_MDP.QLearning(0.98, 2, 0.1)
        displayOptimalPolicy(rubiks_MDP)
    if setup == True:
        #setup before so only need to solve
        start = input("Type start anytime you are ready to solve the puzzle ")
        # while start != "start": #wait till the correct answer: "start" is typed
        #     start = input("Type start anytime you are ready to solve the puzzle ")
        rubiks_MDP.register_transition_function(Test_Rubiks.T)
        rubiks_MDP.register_reward_function(Test_Rubiks.R)
        # rubiks_MDP.random_episode(1000)
        rubiks_MDP.QLearning(0.98, 2, 0.1)
        displayOptimalPolicy(rubiks_MDP)



test()