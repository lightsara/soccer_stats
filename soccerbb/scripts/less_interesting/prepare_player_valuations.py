#!/usr/bin/env python3

##prepare data 
import json

##Prepare team/club data.

##dirprep
outdir = '/home/sara/main/FrontEnd_2025/Projects/soccer_stats/data/'
rawdata = '/home/sara/main/FrontEnd_2025/Projects/soccer_stats/data/player_valuations.csv'
output = '/home/sara/main/FrontEnd_2025/Projects/soccer_stats/data/player_valuations.json'

##fileprep
outfile = open(output, 'w')
infile = open(rawdata, 'r')

adict = {}
for aline in infile:
    ##strip the line
    aline = aline.strip()
    ##split the line  
    aline = aline.split(',')
    ##get the player id         
    player_id = aline[0]
    ##get the date
    date = aline[1]
    ##get the market value in eur
    market_value_in_eur = aline[2]
    ##get the current club id
    current_club_id = aline[3]
    ##get the player club domestic competition id
    player_club_domestic_competition_id = aline[4]
    ##create a dictionary for the player    
    player_dict = {}
    player_dict['date'] = date  
    player_dict['market_value_in_eur'] = market_value_in_eur
    player_dict['current_club_id'] = current_club_id
    player_dict['player_club_domestic_competition_id'] = player_club_domestic_competition_id
    ##add the player dictionary to the main dictionary
    if player_id not in adict:
        adict[player_id] = []   
    adict[player_id].append(player_dict)


##dump the dictionary to a json file
json.dump(adict, outfile, indent=4, sort_keys=True) 
##close the files
outfile.close() 
infile.close()



##Data looks like this
#player_id,date,market_value_in_eur,current_club_id,player_club_domestic_competition_id

