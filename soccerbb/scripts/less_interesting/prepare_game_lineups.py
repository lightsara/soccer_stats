#!/usr/bin/env python3

##prepare data 
import json

##Prepare team/club data.

##dirprep
outdir = '/home/sara/main/FrontEnd_2025/Projects/soccer_stats/data/'
rawdata = '/home/sara/main/FrontEnd_2025/Projects/soccer_stats/data/csv_files/game_lineups.csv'
output = '/home/sara/main/FrontEnd_2025/Projects/soccer_stats/data/game_lineups.json'

##fileprep
outfile = open(output, 'w')
infile = open(rawdata, 'r')

adict = {}
c = 0
for aline in infile:
    ##strip the line
    aline = aline.strip()
    ##split the line  
    aline = aline.split(',')
    ##get the data
    game_lineups_id = aline[0]
    date = aline[1]
    game_id = aline[2]
    player_id = aline[3]
    club_id = aline[4]
    player_name = aline[5]
    type = aline[6]
    position = aline[7]     
    number = string.strip(aline[8])
    #print(game_lineups_id, c)
    #print(aline)
    team_captain = aline[9]
    c += 1
    ##create a dictionary for each line
    adict[game_lineups_id] = {}
    adict[game_lineups_id]['date'] = date
    adict[game_lineups_id]['game_id'] = game_id
    adict[game_lineups_id]['player_id'] = player_id
    adict[game_lineups_id]['club_id'] = club_id
    adict[game_lineups_id]['player_name'] = player_name
    adict[game_lineups_id]['type'] = type
    adict[game_lineups_id]['position'] = position
    adict[game_lineups_id]['number'] = number
    adict[game_lineups_id]['team_captain'] = team_captain

##dump the dictionary to a json file        
json.dump(adict, outfile, indent=4, sort_keys=True) 
##close the files
outfile.close() 
infile.close()


##Data looks like this
##game_lineups_id,date,game_id,player_id,club_id,player_name,type,position,number,team_captain

##The first few lines:
##2dbe01c3656b06c8e23e9de714e26bb,2013-07-27,2317258,1443,610,Christian Poulsen,substitutes,Defensive Midfield,5,0
##b50a3ec6d52fd1490aab42042ac4f738,2013-07-27,2317258,5017,610,Niklas Moisander,starting_lineup,Centre-Back,4,0
##7d890e6d0ff8af84b065839966a0ec81,2013-07-27,2317258,9602,1090,Maarten Martens,substitutes,Left Winger,11,0

##The last few lines:
## ",0
'''
e3b5e9d4f76c9f6ec3c87fffa3cd01ca,2024-03-16,4300789,171679,543,Matt Doherty,substitutes,Right-Back,"
                     2
                ",0 
d85fc63542ff1f7d1eb3ecfe7fce5dc8,2024-03-16,4300789,231572,543,Nélson Semedo,starting_lineup,Right Midfield,"
                  22
                ",0
04e63f09518d99bda356b07704aafe55,2024-03-16,4300789,249994,543,José Sá,starting_lineup,Goalkeeper,"
                  1
                ",0
851a21f550d62d39d50a82cf3e4436a9,2024-03-16,4300789,258216,990,Kasey Palmer,starting_lineup,Attacking Midfield,"
                  45
                ",0
2b400f2a9dd35d711e9210178c85ab92,2024-03-16,4300789,258914,990,Brad Collins,starting_lineup,Goalkeeper,"
                  40
                ",0
09f09e8c8fc49862f3a87550a42c6436,2024-03-16,4300789,258915,990,Jay Dasilva,substitutes,Left-Back,"
                  3
                ",0
'''

##Next steps:
##1. Identify where the errors start
##2. Fix the errors
##3. Test the code
##4. Run the code
##5. Check the output
##6. If the output is correct, move on to the next step
