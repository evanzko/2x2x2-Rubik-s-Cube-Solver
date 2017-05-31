# Skyler Martens and Evan Ko
# May 30, 2017
# CSE 415 Final Project

# This file is responsible for handeling all user input
# The Graphical interface displays a 2-D view of the
# Rubik's cube as well as displaying the max Q-Value at
# each state in a comprehensive state map.

#######################################################
## How to use:                                       ##
## 1) Either Select Initialize Simple Demo or
# initialize Coplete Demo
## 2) Display Q values to show representation of state
# space
## 3) Simulate Rubix's Cube solution to initialize
# cub rep at start state
## 4) Next Rubix's Cube move to get next rubix cube state
#######################################################

# Imports section
from tkinter import *
import random
import time
import MDP, Test_Rubiks

# Initialization of MDP and GUI
rubiks_MDP = rubiks_MDP = MDP.MDP()
master = Tk()

# Global Variable to show if MDP has been initialized
is_initialized = False


# Global variables containing points for boxes
top_left_x = [21, 91, 21, 91, 161, 231, 161, 231, 161, 231, 161, 231,\
              161, 231, 161, 231, 301, 371, 301, 371, 441, 511, 441, 511]
top_left_y = [166, 166, 236, 236, 166, 166, 236, 236, 26, 26, 96, 96, 306,\
              306, 376, 376, 166, 166, 236, 236, 166, 166, 236, 236]
bottom_right_x = [89, 159, 89, 159, 229, 299, 229, 299, 229, 299, 229,\
                  299, 229, 299, 229, 299, 369, 439, 369, 439, 509, 579, 509, 579]
bottom_right_y =[234, 234, 304, 304, 234, 234, 304, 304, 94, 94, 164, 164,\
                 374, 374, 444, 444, 234, 234, 304, 304, 234, 234, 304, 304]


# Canvas to represent 2x2 rubik's cube
w = Canvas(master, width=1000, height=460)
w.pack()

# Creates box where max Q-value to state will be plotted
w.create_line(600, 34, 600, 415, fill="#000000", width=3)
w.create_line(982, 34, 982, 415, fill="#000000", width=3)
w.create_line(600, 34, 982, 34, fill="#000000", width=3)
w.create_line(600, 415, 982, 415, fill="#000000", width=3)

# Label for Q-Value Map
w.create_text(790, 15, font=("Purisa", 16), text="Q-Values")

# Label for Left Side
w.create_text(85, 150, font=("Purisa", 16), text="Left Side")
# Label for Right Side
w.create_text(365, 150, font=("Purisa", 16), text="Right Side")
# Label for Back Side
w.create_text(505, 150, font=("Purisa", 16), text="Back Side")
# Label for Top Side
w.create_text(230, 10, font=("Purisa", 16), text="Top Side")
# Label for Bottom Side
w.create_text(230, 456, font=("Purisa", 16), text="Bottom Side")

# Creates horizontal lines of Rubik's cube
w.create_line(160, 25, 300, 25, fill="#000000", width=3)
w.create_line(160, 95, 300, 95, fill="#000000", width=3)
w.create_line(20, 165, 580, 165, fill="#000000", width=3)
w.create_line(20, 235, 580, 235, fill="#000000", width=3)
w.create_line(20, 305, 580, 305, fill="#000000", width=3)
w.create_line(160, 375, 300, 375, fill="#000000", width=3)
w.create_line(160, 445, 300, 445, fill="#000000", width=3)

# Creates vertical lines of Rubik's cube
w.create_line(20, 165, 20, 305, fill="#000000", width=3)
w.create_line(90, 165, 90, 305, fill="#000000", width=3)
w.create_line(160, 25, 160, 445, fill="#000000", width=3)
w.create_line(230, 25, 230, 445, fill="#000000", width=3)
w.create_line(300, 25, 300, 445, fill="#000000", width=3)
w.create_line(370, 165, 370, 305, fill="#000000", width=3)
w.create_line(440, 165, 440, 305, fill="#000000", width=3)
w.create_line(510, 165, 510, 305, fill="#000000", width=3)
w.create_line(580, 165, 580, 305, fill="#000000", width=3)
colors = [ 'g', 'w', 'r', 'y', 'b', 'o']

# Gives intro for GUI
def intro():
    print("Welcome to the 2x2 rubik's cube solver")
    print("How to use interface:")
    print("1) Select either initialize simple demo or initialize complete demo")
    print("2) Display Q values to show representation of state space.")
    print("3) Simulate Rubik's Cube solution to initialize cube representation at start state.")
    print("4) Keep pressing next Rubik's Cube move to get next rubik's cube state to show how to solve cube.")

intro()

# initializes simple demo
def callback_1():
    print("Starting Simple Demo")
    global rubiks_MDP
    global is_initialized
    if (is_initialized):
        rubiks_MDP.QLearning(0.9, 10, 0.2)
    else:
        rubiks_MDP.register_start_state("wwoobbggrrrryyyyoowwggbb")
        rubiks_MDP.register_actions(Test_Rubiks.ACTIONS)
        rubiks_MDP.register_operators(Test_Rubiks.OPERATORS)
        rubiks_MDP.register_transition_function(Test_Rubiks.T)
        rubiks_MDP.register_reward_function(Test_Rubiks.R)
        rubiks_MDP.generateAllStates()
        is_initialized = True
        rubiks_MDP.QLearning(0.9, 20, 0.2)

# Represents Q-Values by showing each state as a box with
# color determined by max Q value
def callback_2():
    global  rubiks_MDP
    if rubiks_MDP is None:
        print("Please press initialization button")
    else :
        rubiks_MDP.extractPolicy()
        best_vals = rubiks_MDP.return_best_policy()
        top_left_x = 601
        top_left_y = 32
        bottom_right_x = 611
        bottom_right_y = 42
        '''for i in range(16128):
            curr_val =random.randrange(1000)
            max_state_vals.append(curr_val)'''
        j = 0
        for element in best_vals:
            curr_val = rubiks_MDP.maxPolicyVal.get(element)
            if(j % 38 == 0):
                top_left_x = 601
                bottom_right_x = 611
                top_left_y = top_left_y + 10
                bottom_right_y = bottom_right_y + 10
            else:
                top_left_x = top_left_x + 10
                bottom_right_x = bottom_right_x + 10
            r = 0
            g = 0
            b = 0
            if (curr_val < 500) :
                if curr_val < 0:
                    r = 255
                    g = 0
                    b = 0
                else :
                    r = 255
                    g = 255 - round((500 - curr_val) / 2)
                    b = 0
            else :
                if curr_val > 1000:
                    r = 0
                    g = 255
                    b = 0
                else :
                    g = 255
                    r = abs(round((1000 - curr_val) / 2))
                    b = 0
            hex_string = convert_to_hex(r, g, b)
            w.create_rectangle(top_left_x, top_left_y, bottom_right_x, bottom_right_y, fill=hex_string)
            j = j + 1

# Converts base 10 to hex
def convert_to_hex(r, g, b):
    hex_string = "#"
    r_str = "0x{:02x}".format(r)
    g_str = "0x{:02x}".format(g)
    b_str = "0x{:02x}".format(b)
    hex_string = hex_string + r_str[2] + r_str[3] + g_str[2] + g_str[3] + b_str[2] + b_str[3]
    return hex_string

# Represents initial state of cube
def callback_3():
    global top_left_x
    global top_left_y
    global bottom_right_x
    global bottom_right_y
    if rubiks_MDP.optPolicy is None:
        print("Please initialize and find Q values")
    else:
        color_vals = []
        start_state = rubiks_MDP.start_state
        for i in range (24):
            curr_color = start_state[i]
            fill_val = ""
            if (curr_color == 'g'):
                fill_val = "#10c10d"
            elif (curr_color == 'w'):
                fill_val = "#ffffff"
            elif (curr_color == 'r'):
                fill_val = "#e50d0d"
            elif (curr_color == 'y'):
                fill_val = "#f0f407"
            elif (curr_color == 'b'):
                fill_val = "#0622f4"
            else:
                fill_val = "#f48c06"
            color_vals.append(fill_val)
        for j in range(24):
            w.create_rectangle(top_left_x[j], top_left_y[j], bottom_right_x[j], bottom_right_y[j],
                               fill=color_vals[j])
        rubiks_MDP.current_state = rubiks_MDP.start_state

#  Updates representation of cube based on optimal action
def callback_4():
    global top_left_x
    global top_left_y
    global bottom_right_x
    global bottom_right_y
    if rubiks_MDP.optPolicy is None:
        print("Please initialize and find Q values")
    if rubiks_MDP.current_state != "GAME_OVER":
        action = rubiks_MDP.optPolicy.get(rubiks_MDP.current_state)
        act_val = rubiks_MDP.maxPolicyVal.get(rubiks_MDP.current_state)
        print("Optimal Action: " + action)
        print("Policy value: " + str(act_val))
        rubiks_MDP.take_action(action)
        curr_state = rubiks_MDP.current_state
        if (curr_state == "GAME_OVER"):
            w.create_text(300, 230, font=("Purisa", 80), text="CUBE SOLVED!")
        else:
            color_vals = []
            for i in range(24):
                curr_color = curr_state[i]
                fill_val = ""
                if (curr_color == 'g'):
                    fill_val = "#10c10d"
                elif (curr_color == 'w'):
                    fill_val = "#ffffff"
                elif (curr_color == 'r'):
                    fill_val = "#e50d0d"
                elif (curr_color == 'y'):
                    fill_val = "#f0f407"
                elif (curr_color == 'b'):
                    fill_val = "#0622f4"
                else:
                    fill_val = "#f48c06"
                color_vals.append(fill_val)
            for j in range(24):
                w.create_rectangle(top_left_x[j], top_left_y[j], bottom_right_x[j], bottom_right_y[j],
                                   fill=color_vals[j])

# initializes complete demo of cube
def callback_5():
    print("Starting complete demo")
    global rubiks_MDP
    global is_initialized
    if (is_initialized):
        rand_state = rubiks_MDP.get_random_state()
        rubiks_MDP.register_start_state(rand_state)
        rubiks_MDP.QLearning(0.97, 100, 0.2)
    else :
        rubiks_MDP.register_start_state("wwoobbggrrrryyyyoowwggbb")
        rubiks_MDP.register_actions(Test_Rubiks.ACTIONS)
        rubiks_MDP.register_operators(Test_Rubiks.OPERATORS)
        rubiks_MDP.register_transition_function(Test_Rubiks.T)
        rubiks_MDP.register_reward_function(Test_Rubiks.R)
        rubiks_MDP.generateAllStates()
        rand_state = rubiks_MDP.get_random_state()
        rubiks_MDP.register_start_state(rand_state)
        is_initialized = True
        rubiks_MDP.QLearning(0.97, 100, 0.2)

## Button Section
a = Button(master, text = "Initialize Solver Simple Demo", command=callback_1)
a.pack()

e = Button(master, text = "Initialize Solver Complete Demo", command=callback_5)
e.pack()

b = Button(master, text="Display Q Values", command=callback_2)
b.pack()

c = Button(master, text="Simulate Rubik's Cube Solution", command=callback_3)
c.pack()

d = Button(master, text="Next Rubik's Cube Move", command=callback_4)
d.pack()

mainloop()
