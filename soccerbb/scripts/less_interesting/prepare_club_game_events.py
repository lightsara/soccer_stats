#!/usr/bin/env python3

##prepare data 
import json

##Prepare team/club data.

##dirprep
outdir = '/home/sara/main/FrontEnd_2025/Projects/soccer_stats/data/'
rawdata = '/home/sara/main/FrontEnd_2025/Projects/soccer_stats/data/game_events.csv'
output = '/home/sara/main/FrontEnd_2025/Projects/soccer_stats/data/game_events.json'

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
    game_event_id = aline[0]
    date = aline[1]
    game_id = aline[2]
    minute = aline[3]
    type = aline[4]
    club_id = aline[5]
    player_id = aline[6]
    description = aline[7]
    player_in_id = aline[8]
    player_assist_id = aline[9]
    ##create the dictionary
    adict[game_event_id] = {}
    adict[game_event_id]['date'] = date
    adict[game_event_id]['game_id'] = game_id
    adict[game_event_id]['minute'] = minute
    adict[game_event_id]['type'] = type
    adict[game_event_id]['club_id'] = club_id
    adict[game_event_id]['player_id'] = player_id
    adict[game_event_id]['description'] = description
    adict[game_event_id]['player_in_id'] = player_in_id
    adict[game_event_id]['player_assist_id'] = player_assist_id     


##dump the dictionary to a json file        
json.dump(adict, outfile, indent=4, sort_keys=True) 
##close the files
outfile.close() 
infile.close()


##data looks like this
##game_event_id,date,game_id,minute,type,club_id,player_id,description,player_in_id,player_assist_id