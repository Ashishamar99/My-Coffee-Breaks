"""
This program takes 2 numbers as input.
The first one is the total number of players and the second one is the number of players in a team and it randomly chooses players from the first list and forms teams.
The output will be teams which are generated randomly.
"""
import random
try:
    n = int(input("Enter the total number of players: "))
    m = int(input("Enter the number of players in a team: "))
except:
    print("\nException Occurred!!\n")
    exit(0)
if m>n:
    print("Enter valid input")
    exit(0)
b = []
temp = []
final_teams = []
teams = []
flag = 0
for i in range(1,n+1):
    b.append(i)
print(f'List of all players: {b}')
temp = b.copy()
while True:
    if(len(temp)<m and flag==m):
        if teams not in final_teams:
            final_teams.append(teams)
        if len(temp) != 0:
            final_teams.append(temp)
        break
    if(flag<=m-1):
        randp = random.randint(1,n)
        if(randp in temp):
            temp.remove(randp)
            teams.append(randp)
            flag += 1
            continue
        elif(randp not in temp):
            continue
    elif(flag == m):
        final_teams.append(teams)
        flag = 0
        teams = []
        continue
    else:
        print("Error")
        break
print(f"Final teams are: {final_teams}")
input("Exit")
