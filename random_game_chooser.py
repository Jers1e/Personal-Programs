import random

#Lists of game systems
game_systems = ['Commodore 64', 'Original Xbox', 'Xbox 360', 'Xbox One',
    'MS-DOS', 'Nintendo 3DS', 'Nintendo 64','Nintendo DS', 'Nintendo Entertainment System (NES)', 'Famicom',
    'Game Boy', 'Game Boy Advance','Game Boy Color', 'GameCube', 'Nintendo Switch', 'Nintendo Wii',
    'Wii U', 'SuperGrafx', 'SEGA Tower of Power', 'SEGA Dreamcast', 'SEGA Game Gear', 'SEGA Master System',
    'SEGA Saturn', 'NEO GEO Lineup', 'Playstation', 'Playstation2','Playstation3','Playstation4','Playstation5',
    'Playstation Vita', 'Playstation Portable (PSP)', 'Super Nintendo Entertainment System (SNES)', 'WonderSwan',
    'WonderSwan Color', 'WonderSwan Crystal', ]
sega_tower_of_power = ['SEGA 32X', 'SEGA CD', 'SEGA CD 32X']
neo_geo_lineup = ['AES', 'CD', 'MVS', 'Neo Geo Pocket', 'Neo Geo Color']

def game_chooser():
    chosen_system = random.choice(game_systems)
    #These two categories have a lot of their own specific software that is worth putting into their own
    # category, thus the if statements
    if chosen_system == 'SEGA Tower of Power':
        print("Hold on! SEGA had a lot of retro stuff, let's choose specifically which hardware.")
        print(f"Ok, you got {random.choice(sega_tower_of_power)}, enjoy!")
    elif chosen_system == 'NEO GEO Lineup':
        print("Hold on! NEO GEO had a lot of retro stuff, let's choose specifically which hardware.")
        print(f"Ok, you got {random.choice(neo_geo_lineup)}, enjoy!")
    else:
        print(f"The game system you got was {chosen_system}, enjoy! ")

game_chooser()