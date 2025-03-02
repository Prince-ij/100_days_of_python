game_bar = {
    'a': float('nan'),
    'b': float('nan'),
    'c': float('nan'),
    'd': float('nan'),
    'e': float('nan'),
    'f': float('nan'),
    'g': float('nan'),
    'h': float('nan'),
    'i': float('nan')
}

winning_criteria = [
    "(game_bar['a'] == game_bar['b']) and (game_bar['b'] == game_bar['c'])",
    "(game_bar['d'] == game_bar['e']) and (game_bar['e'] == game_bar['f'])",
    "(game_bar['g'] == game_bar['h']) and (game_bar['h'] == game_bar['i'])",
    "(game_bar['a'] == game_bar['d']) and (game_bar['d'] == game_bar['g'])",
    "(game_bar['b'] == game_bar['e']) and (game_bar['e'] == game_bar['h'])",
    "(game_bar['c'] == game_bar['f']) and (game_bar['f'] == game_bar['i'])",
    "(game_bar['a'] == game_bar['e']) and (game_bar['e'] == game_bar['i'])",
    "(game_bar['c'] == game_bar['e']) and (game_bar['e'] == game_bar['g'])"
]

positions = {
    'a': 16,
    'b': 22,
    'c': 28,
    'd': 63,
    'e': 69,
    'f': 75,
    'g': 110,
    'h': 116,
    'i': 122,
}

game_board = '''
     |     |
  -  |  -  |  -
_____|_____|_____
     |     |
  -  |  -  |  -
_____|_____|_____
     |     |
  -  |  -  |  -
     |     |
'''

game_intro = '''

▀█▀ █ █▀▀   ▀█▀ ▄▀█ █▀▀   ▀█▀ █▀█ █▀▀
░█░ █ █▄▄   ░█░ █▀█ █▄▄   ░█░ █▄█ ██▄
'''
