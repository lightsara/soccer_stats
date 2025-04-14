#!/usr/bin/env python3

##prepare data 
import json

##Prepare team/club data.

##dirprep
outdir = '/home/sara/main/FrontEnd_2025/Projects/soccer_stats/data/'
rawdata = '/home/sara/main/FrontEnd_2025/Projects/soccer_stats/data/club_games.csv'
output = '/home/sara/main/FrontEnd_2025/Projects/soccer_stats/data/club_games.json'

##fileprep
outfile = open(output, 'w')
infile = open(rawdata, 'r')

adict = {}
for aline in infile:
    ##strip the line
    aline = aline.strip()
    ##split the line  
    aline = aline.split(',')
    ##get the data
    game_id = aline[0]
    club_id = aline[1]
    own_goals = aline[2]
    own_position = aline[3]
    own_manager_name = aline[4]
    opponent_id = aline[5]
    opponent_goals = aline[6]
    opponent_position = aline[7]
    opponent_manager_name = aline[8]
    hosting = aline[9]
    is_win = aline[10]
    ##create a dictionary
    adict[game_id] = {}
    adict[game_id]['club_id'] = club_id
    adict[game_id]['own_goals'] = own_goals
    adict[game_id]['own_position'] = own_position
    adict[game_id]['own_manager_name'] = own_manager_name
    adict[game_id]['opponent_id'] = opponent_id
    adict[game_id]['opponent_goals'] = opponent_goals
    adict[game_id]['opponent_position'] = opponent_position
    adict[game_id]['opponent_manager_name'] = opponent_manager_name
    adict[game_id]['hosting'] = hosting
    adict[game_id]['is_win'] = is_win


##dump the dictionary to a json file        
json.dump(adict, outfile, indent=4, sort_keys=True) 
##close the files
outfile.close() 
infile.close()


##data looks like this
##game_id,club_id,own_goals,own_position,own_manager_name,opponent_id,opponent_goals,opponent_position,opponent_manager_name,hosting,is_win
