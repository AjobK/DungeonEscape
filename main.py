# Ajob Kustra 2022, Guest lecture material. Open-source (MIT License)
#
# WARNING:
# Code is meant to educate and to display core concepts in a game context.
# It is for beginners at the end of the first programming course, therefore
# optimilization and principles were not taken into account.

import keyboard
import time
import os

levels = [ # For now only two maps
    [
        [ 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', '    ', '    ', 'key ', 'wal ', 'tlp ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', 'up  ', 'wal ', 'wal ', 'wal ', 'qst3', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', 'lok2', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', 'lok1', 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', 'qst2', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', 'qst1', 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'usr ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ' ]
    ],
    [ # Dummy and the same as first map (at index one, so the 2D array above), except the user starts at the spot where they teleported
        [ 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', '    ', '    ', 'key ', 'wal ', 'usr ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', 'qst3', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', 'lok2', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', 'lok1', 'wal ', 'wal ', 'wal ', 'lok3 ', 'wal ', 'wal ', 'wal ', 'qst2', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', '    ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', 'qst1', 'wal ', 'wal ', 'wal ', 'up  ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'tlp ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ' ],
        [ 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ', 'wal ' ]
    ],
]

icons = {
    'wal': '🟫',
    '   ': '  ',
    'tlp': '📶',
    'up ': '⬆️ ',
    'usr': '🦖', # Can be any character, for example a cow! 🐄
    'lok': '🔒',
    'olk': '🔓',
    'qst': '❓',
    'key': '🗝️ ',
    'trch': '🕯️ ',
    'swch': '🥪 ',
    'snal': '🐌'
}

def end_game(extraInfo = ''):
    print('\n\n   💀 💔  GAME OVER  💔 💀\n')

    if len(extraInfo) > 1:
        print('   {}'.format(extraInfo.strip()))

    quit()

# Below we face a complex datastructure in the common shape of a dictionary. Let's disect it:
# The initial properties of the dictionary (ex. 'qst1') contain key information for each dialogue.
# These dialogues must contain a question and answers. Therefore, we nest from the general dictionary
# into nested dictionaries for both questions and answers. Here, the question can only be a string value,
# whereas the answer is another nested dictionary. The reason being, that each answer has its own message,
# potential follow-up action (followup_action).
quests = {
    'qst1': {
        'question': """
            Around the corner you notice the silhouette of a skeleton on the wall.
            You also hear a crackling sound.
        """,
        'answers': {
            'Take a look': {
                'message': """
                    Nothing interesting to find besides a torch and an expired sandwich...
                    Might as well take both.

                    [Gained a torch 🕯️  and sandwich 🥪  ]
                """,
                'followup_action': lambda: add_to_inventory('trch', 'swch'),
            },
            'Turn back': {
                'message': 'You turn back'
            }
        }
    },
    'qst2': {
        'question': """
            You are at the entrance of a dark cave. On the sign above it says 'Frog Cave'.
        """,
        'answers': {
            'Enter the dark cave': {
                'followup_action': lambda: trigger_prompt('qst2.1') if 'trch' in inventory else end_game("""
                    🐸  It's dark. You stand on a toxic frog by accident and die.

                    [You need a torch 🕯️  ]
                """)
            },
            'Turn back': {
                'message': 'You turn back'
            }
        }
    },
    'qst2.1': {
        'question': """
            You enter the cave with your torch in hand. After walking for a while the road splits in two.
            From the left side you hear croaking. On the right side you hear a tune playing.
        """,
        'answers': {
            'Go left': {
                'message': 'You walk towards the croaking',
                'followup_action': lambda: trigger_prompt('qst2.1.1')
            },
            'Go right': {
                'message': 'That tune is intriguing, let\'s check it out',
                'followup_action': lambda: trigger_prompt('qst2.1.2')
            }
        }
    },
    'qst2.1.1': {
        'question': """
            At the end of the tunnel you see a giant frog with a crown on it's head.
            "Welcome ugly one" it says. "I see you have entered my kingdom for the trial of wisdom!"

            You have no idea what it's talking about.

            "To leave unharmed you must answer correctly... What is my favourite food?"

            Uh-oh. I better get this right.
        """,
        'answers': {
            'Snails': {
                'message': '"I WOULD NEVER EAT SOMETHING SO DISGUSTING! You shall die for this foolish mistake."',
                'followup_action': lambda: end_game('🐸  You angered the frog king. I guess they don\'t like snails')
            },
            'Skittles': {
                'message': """
                    Yes, yes! You are indeed very wise! Take this gold snack as your reward!

                    [Gained a key 🗝️   and smelly snail 🐌  ]
                """,
                'followup_action': lambda: add_to_inventory('key', 'snal'),
            }
        }
    },
    'qst2.1.2': {
        'question': """
            At the end of the tunnel you find an owl singing a song. That's it.
        """,
        'answers': {
            'Go back': {
                'message': 'Oh well. You go back disappointed.',
                'followup_action': lambda: trigger_prompt('qst2.1')
            }
        }
    },
    'qst3': {
        'question': """
            Behind the gate you find a whining dog. It seems like it's hungry
        """,
        'answers': {
            '[OFFER SNAIL]': {
                'message': """
                    The dog gets very nauseous. When it looks up you notice that it was actually an angry wolf.
                    Just as it tries to attack you it faints and vomits out something sparkly.

                    [Gained a key 🗝️   and survived an attack!]
                """,
                'followup_action':  lambda: add_to_inventory('key'),
            },
            '[OFFER SANDWICH]': {
                'message': 'The dog eats the sandwich. When it looks up you realize it was actually an angry wolf...',
                'followup_action': lambda: end_game('🐺  Compassion didn\'t take you far this time')
            }
        }
    },
}

current_level_index = 0
current_level = levels[current_level_index].copy()
player_position = None
inventory = { 'key': 0 }
message = ''

def render():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear') # Haalt alle oude tekst weg
    print('   🚫 Press \'q\' to quit\n')

    render_map()
    render_inventory()

    if len(message) > 1:
        print('\n   [🗯️  {}]'.format(message))

def render_map():
    global player_position

    for row_index, _ in enumerate(current_level):
        row_text = ''

        for column_index, column in enumerate(current_level[row_index]):
            icon_key = column[0:3]
            
            if (not player_position and icon_key == 'usr'):
                player_position = [column_index, row_index]
                row_text += icons[icon_key]
            elif (player_position == [column_index, row_index]):
                row_text += icons['usr']
            elif (icon_key != 'usr'):
                row_text += icons[icon_key]
            else:
                row_text += icons['   ']

        print(row_text)

def advance_level():
    global current_level_index, current_level, player_position

    current_level_index += 1
    current_level = levels[current_level_index].copy()
    player_position = None # This will be calculated again by render_map
    render_map()

def add_to_inventory(*items):
    global inventory

    for item in items:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1

def render_inventory():
    global inventory

    print_string = '\n    '
    for item in inventory:
        print_string += icons[item] + '  ' + str(inventory[item]) + '    '

    print(print_string)

def next_block_action(delta):
    global player_position, message

    next_position = [
        player_position[0] + delta[0],
        player_position[1] + delta[1]
    ]

    message = ''

    next_position_text = current_level[next_position[1]][next_position[0]]

    if next_position_text[0:3] in ['key']:
        current_level[next_position[1]][next_position[0]] = '    '
        add_to_inventory(next_position_text[0:3])
        message = 'Picked up 1 {}'.format(icons[next_position_text[0:3]])
    elif next_position_text.startswith('lok'):
        amount_required = int(next_position_text[3:4])

        if 'key' in inventory.keys() and amount_required <= inventory['key']:
            current_level[next_position[1]][next_position[0]] = '    '
            message = 'Gate opened!'
        else:
            message = 'You need {} 🗝️  keys for this gate'.format(amount_required)
    elif next_position_text.startswith('qst'):
        player_position = next_position
        trigger_prompt(next_position_text)
    elif next_position_text.startswith('tlp'):
        player_position = next_position
        render()
        if current_level_index < len(levels)-1:
            advance_level()
        else:
            print('\n   👑  Congratulations! You have left the dungeon safely!')
            quit()
    elif next_position_text != 'wal ':
        player_position = next_position

def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def trigger_prompt(questId):
    # Prevent from errors of invalid quests
    if questId not in quests: return

    answers = list(quests[questId]['answers'].keys())
    question = quests[questId]['question'].strip()
    max_line_length = 38 if len(question) <= 18 else len(question) + 20
    answer = -1

    while answer < 0 or answer > len(answers) - 1:
        render()
        print('\n{}\n'.format('#' * max_line_length))   # Top line
        print('   ❓  {}\n'.format(question))

        for i, answer_element in enumerate(answers):
            print('   [{}] {}'.format(i+1, answer_element))

        print('\n{}\n'.format('#' * max_line_length))   # Bottom line
        flush_input()
        answer_before_parse = input('   🔢  ')

        if answer_before_parse.isdigit() and int(answer_before_parse) >= 1 and int(answer_before_parse) <= len(answers):
            answer = int(answer_before_parse) - 1

    answerObj = quests[questId]['answers'][answers[answer]]
    
    if 'message' in answerObj:
        print('\n   {}\n'.format(answerObj['message'].strip()))
        message_without_whitespace = answerObj['message'].replace('  ', '')
        wait_time = len(message_without_whitespace) / 25.0
        time.sleep(wait_time)

    if 'followup_action' in answerObj:
        answerObj['followup_action']()


render()
while True:
    key = str(keyboard.read_key()).lower()

    if key in [ 'w', 'a', 's', 'd' ]:
        if keyboard.is_pressed('w'):
            next_position_delta = [0, -1]
        elif keyboard.is_pressed('s'):
            next_position_delta = [0, 1]
        elif keyboard.is_pressed('a'):
            next_position_delta = [-1, 0]
        elif keyboard.is_pressed('d'):
            next_position_delta = [1, 0]

        next_block_action(next_position_delta)
        render()

        time.sleep(0.1)
    elif key == 'q':
        print('\n    🚫  Game stopped (Pressed \'q\')')
        quit()
