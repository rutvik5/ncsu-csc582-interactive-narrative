'''
BDI Model Prototype

Instructions- Run the python script and enter a choice from the given alternatives. The program will automatically generate a
correct sequence of actions in order to resemble a real player. No additional dependencies need to be installed.

We have taken a scenario of day-2 of the game Anchorhead. The plot points of this storyline have been included in the following
dictionaries. These dictionaries are modeled based on requirements of the story as mentioned in the paper.
This prototype tries to model the behavior of a human player by predicting the correct sequence of actions that are required to
reach to a particular end-point- expected by the author. There are two end points in the story- 'see_evil_god' and 'discover_book_in_sewer'.
This program is developed in a way to ensure that every pre-requisite condition is met before the agent adds the plot point to the list
of discovered plot points. If the agent reaches a dead-end, it starts from another plot point which has not been discovered yet.

Future Scope-
'Exploration'- is an aspect that can be worked upon. Currently, the agent only discovers plot-points in the story.
However, the agent can explore different areas of the map rather than focusing on the plot points.
'Object Interaction'- We can control the interaction that the agent has once it encounters an object. The interactions should be
limited to natural interactions that a real player would perform rather than performing every action on the object.
Certain weights can be assigned to each plot point if the author wants to favor a particular a path in the story
'''

import random as random

initial_actions = ['discover_safe', 'get_safe_combo', 'get_card', 'get_flask', 'get_crypt_key', 'find_magic_shop', 'examine_album',
                   'read_basement_clipings', 'get_silver_locket', 'find_observatory']

path_dict = {'discover_safe': ['open_safe'], 'get_safe_combo': ['open_safe'], 'find_magic_shop': ['get_amulet', 'open_puzzle_box'],
            'open_safe': ['open_puzzle_box'], 'open_puzzle_box':['see_evil_god'], 'get_amulet': ['give_bum_amulet'],
            'give_bum_amulet': ['discover_book_in_sewer'], 'find_observatory': ['see_evil_god'], 'get_card': ['read_library_book'],
            'get_flask': ['give_bum_flask'], 'give_bum_flask': ['give_bum_amulet', 'talk_to_bum_about_crypt', 'talk_to_bum_about_anna','talk_to_bum_about_william','show_bum_skull'],
             'get_crypt_key': ['find_williams_coffin'], 'find_williams_coffin': ['get_skull', 'talk_to_bum_about_william'], 'get_skull': ['show_bum_skull']}

pre_requisite_dict = {'open_safe':['discover_safe', 'get_safe_combo'], 'open_puzzle_box': ['open_safe', 'find_magic_shop'],
                  'see_evil_god':['open_puzzle_box', 'find_observatory'], 'get_amulet': ['find_magic_shop'],
                  'give_bum_amulet': ['get_amulet', 'give_bum_flask'], 'read_library_book': ['get_card'], 'give_bum_flask': ['get_flask'],
                  'talk_to_bum_about_crypt': ['give_bum_flask'], 'talk_to_bum_about_anna': ['give_bum_flask'],
                  'talk_to_bum_about_william': ['give_bum_flask', 'find_williams_coffin'], 'show_bum_skull':['give_bum_flask', 'get_skull'],
                  'get_skull':['find_williams_coffin'], 'find_williams_coffin': ['get_crypt_key'], 'discover_book_in_sewer':['give_bum_amulet']}

action_history = []

correct_input = True
while(correct_input):
    print('Enter one of the following actions (without trailing spaces): ')
    print()
    for actions in initial_actions:
        print(actions)
    print()
    first_action = input('-->')

    if first_action in initial_actions:
        break

action_history.append(first_action)
initial_actions.remove(first_action)


actions_exhausted = False
while ('see_evil_god' not in action_history) and ('discover_book_in_sewer' not in action_history):
    current_action = action_history[-1]

    if current_action in path_dict:
        current_pre_requisite = random.choice(path_dict[current_action])


        in_action_history = True

        for item in pre_requisite_dict[current_pre_requisite]:
            if item not in action_history:
                in_action_history = False
                if len(initial_actions) > 0:
                    random_action = random.choice(initial_actions)
                    action_history.append(random_action)
                    initial_actions.remove(random_action)

                    break
                else:
                    print("All available actions are exhausted, explore a different path!")
                    actions_exhausted = True

        if (in_action_history):
            action_history.append(current_pre_requisite)
            if current_pre_requisite in initial_actions:
                initial_actions.remove(current_pre_requisite)


        if(actions_exhausted):
            break
    else:
        if len(initial_actions) > 0:
            random_action = random.choice(initial_actions)
            action_history.append(random_action)
            initial_actions.remove(random_action)

        else:
            print("All available actions are exhausted, explore a different path!")
            break
print("Complete action sequence: ")
print()

for action in action_history[:-1]:
    print(action + " -> ", end="")
print(action_history[-1])
