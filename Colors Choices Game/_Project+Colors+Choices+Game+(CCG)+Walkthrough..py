#!/usr/bin/env python
# coding: utf-8

# # Colors Choices Game coding in python(red, yellow, orange, green, blue)
# # (CCG):

# ## Table of Contents
# - [Introduction](#intro)
# - [Asking Questions](#Asking_Questions)
# - [Project Helpful Notes](#Project_Helpful_Notes)
# - [Project Helpful Steps](#Project_Helpful_Steps)
# - [Importing needed modules for our project](#Importing_needed_modules_for_our_project)
# - [Show colors choices to user to choose and enter a color](#Show_colors_choices_to_user_to_choose_&_enter_a_color)
# - [Thanks for playing and the overall result of the game](#Thanks_for_playing_and_the_overall_result_of_the_game)
# - [Conclusions](#Conclusions)

# <a id='intro'></a>
# ## Introduction:
# ### Here is some notes to help you understand how to start coding and think about the solution, and your solution maylook completely different than the given solution that is right if it work properly. If these notes below isn,t fully helpful for you , check out the "Project Walkthrough" for more explanation and help. 

# <a id='Asking_Questions'></a>
# ## Asking Questions:
# ### Before looking at the Colors Choices Game Project, you should start by asking questions you might want to understand  the Colors Choices Game(CCG) 
# ### Consider, for example, if you were working for Motivate. What kinds of game is CCG?
# ### order to create and build this project you need to know what is the type of CCG game? 
# ### If you were a user CCG , Do you know what the level of difficulty this game has? 
# ### Do you enjoy playing those types of games?
# 
# **Question**: 
# 
# **Answer**:

# <a id='Project_Helpful_Notes'></a>
# ## Project Helpful Notes:
# ### 1.We need to create choices for players and choices for computer then ask the players for inputs.
# ### 2.compare their inputs with the choice of the computer.
# ### 3.Check if the game is won,tied, lost, or ongoing.
# ### 4.Repeat thess steps until the game has been won or tied.
# ### 5.Ask if players want to play again.
# ### 6.and if the players agree restart the game again.
# ### 7.and if the player say "No" end the game and say thanks for the player.

# <a id='Project_Helpful_Steps'></a>
# ## Project Helpful Steps:
# ### 1.importing needed modules for our project.
# ### 2.Then we will define the main while loop and put the second while loop inside it.
# ### 3.declare colors choices as variables and specify colors of the game inside the nested while loop.
# ### 4.define the game roles by using the second while loop, If Statements and the random module’s randint function to get an integer between one and five.
# ### 5.then print the outputs of this big nested loop and hte If statements inside this big while loop.
# ### 6.show the scores of computer and player after each player turn.
# ### 7.use the If statements to ask the player if he want to play again.
# ### 8.if the player choose "Yes" so restart the game.
# ### 9.if the player say "No" so end the game and say "thanks for playing".
# 

# ## importing needed modules for our project:

# In[6]:


# import random module 
import random 


# <a id='Show_colors_choices_to_user_to_choose_&_enter_a_color'></a>
# ## Declare computer_score and player_score as variables
# ## Show colors choices to user to choose & enter a color value number:

# In[8]:


# Print multiline instruction 
# performstring concatenation of string 
print("Winning Rules of the Colors choices Game as follows: "+ "\nEnter a number from one two five and match computer choice to Win the computer.") 
computer_score = 0
player_score = 0 

while True: 
    print("red = 1 \nyellow = 2 \norange = 3 \ngreen = 4 \nblue = 5 \ntake a turn: ") 
 