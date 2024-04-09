import datetime
import re
import matplotlib.pyplot as ptl
import numpy as np

def count_games_in_pgn_file(file_path):
    game_count = 0

    with open(file_path, 'r') as file:
        game_started = False
        for line in file:
            if line.strip() == '':
                if game_started:
                    game_count += 1
                    game_started = False
            elif line.startswith('[Event'):
                game_started = True

    return game_count

def read_pgn_file(file_path):
    pgn_content = ""
    with open(file_path, 'r') as file:
        pgn_content = file.read()
    games_count = count_games_in_pgn_file(file_path)
    return games_count, pgn_content


x = 0
plm = 0
plt = 0
plw = 0
plT = 0
plf = 0
pls = 0
plS = 0
apf = []
file_path = 'RetiKIA.pgn'  
games_count, pgn_content = read_pgn_file(file_path)
print("Number of games:", games_count)
ap = re.findall(r'\[Date "(?P<result>.+)"', pgn_content)
while x < 54727:
    if not(("?" in ap[x]) or ("1999.09.31" in ap[x]) or ("2000.02.31" in ap[x]) or ("2011.19.11" in ap[x]) or ("`" in ap[x])):
        apf.append(ap[x])
    x = x + 1
print(apf)
print(len(apf))
print(apf[521])
x=0
while x < len(apf):
    print(apf[x])
    a = datetime.datetime.strptime(str(apf[x]), '%Y.%m.%d').strftime('%A')
    if a == 'Monday':
        plm = plm + 1
    if a == 'Tuesday':
        plt = plt + 1
    if a == 'Wednesday':
        plw = plw + 1
    if a == 'Thursday':
        plT = plT + 1
    if a == 'Friday':
        plf = plf + 1
    if a == 'Saturday':
        pls = pls + 1
    if a == 'Sunday':
        plS = plS + 1
    x = x + 1
print(plm)
print(plt)
print(plw)
print(plT)
print(plf)
print(pls)
print(plS)


ptl.style.use('fivethirtyeight')

games = [plm, plt, plw, plT, plf, pls, plS]
day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
ptl.bar(day, games, color="black", label="All Games Played")

ptl.legend()

ptl.xlabel("Days")

ptl.ylabel("Games")

ptl.title("Chess Games Played Throughout The Week")

ptl.show()
