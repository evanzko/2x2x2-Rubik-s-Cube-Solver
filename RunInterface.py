# Skyler Martens and Evan Ko
# May 30, 2017
# CSE 415 Final Project

import MDP, Rubiks_Cube, Test_Rubiks

def test():
    '''Create the MDP, then run an episode of random actions for 10 steps.'''
    rubiks_MDP = MDP.MDP()
    rubiks_MDP.register_start_state("wwggbbwwrrrryyyyoobbggoo")
    rubiks_MDP.register_actions(Test_Rubiks.ACTIONS)
    rubiks_MDP.register_operators(Test_Rubiks.OPERATORS)
    #rubiks_MDP.generateAllStates()
    #print("Total number of generated states: " + str(len(rubiks_MDP.known_states)))
    rubiks_MDP.register_transition_function(Test_Rubiks.T)
    rubiks_MDP.register_reward_function(Test_Rubiks.R)
    #rubiks_MDP.random_episode(1000)
    rubiks_MDP.QLearning(0.98, 500, 0.2)


test()