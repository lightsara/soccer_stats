#!/usr/bin/env python3

##prepare data 
import json

##Prepare team/club data.

##dirprep
outdir = '/home/sara/main/FrontEnd_2025/Projects/soccer_stats/data/'
rawdata = '/home/sara/main/FrontEnd_2025/Projects/soccer_stats/data/games.csv'
output = '/home/sara/main/FrontEnd_2025/Projects/soccer_stats/data/games.json'

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
    competition_id = aline[1]
    season = aline[2]
    round = aline[3]
    date = aline[4]
    home_club_id = aline[5]
    away_club_id = aline[6]
    home_club_goals = aline[7]
    away_club_goals = aline[8]
    home_club_position = aline[9]
    away_club_position = aline[10]
    home_club_manager_name = aline[11]
    away_club_manager_name = aline[12]
    stadium = aline[13]
    attendance = aline[14]
    referee = aline[15]
    url = aline[16]
    home_club_formation = aline[17]
    away_club_formation = aline[18]
    home_club_name = aline[19]
    away_club_name = aline[20]
    aggregate = aline[21]
    competition_type = aline[22]
    ##create a dictionary for the game      
    adict[game_id] = {}
    adict[game_id]['competition_id'] = competition_id
    adict[game_id]['season'] = season
    adict[game_id]['round'] = round
    adict[game_id]['date'] = date
    adict[game_id]['home_club_id'] = home_club_id
    adict[game_id]['away_club_id'] = away_club_id
    adict[game_id]['home_club_goals'] = home_club_goals
    adict[game_id]['away_club_goals'] = away_club_goals         
    adict[game_id]['home_club_position'] = home_club_position
    adict[game_id]['away_club_position'] = away_club_position
    adict[game_id]['home_club_manager_name'] = home_club_manager_name
    adict[game_id]['away_club_manager_name'] = away_club_manager_name
    adict[game_id]['stadium'] = stadium
    adict[game_id]['attendance'] = attendance
    adict[game_id]['referee'] = referee
    adict[game_id]['url'] = url
    adict[game_id]['home_club_formation'] = home_club_formation
    adict[game_id]['away_club_formation'] = away_club_formation
    adict[game_id]['home_club_name'] = home_club_name
    adict[game_id]['away_club_name'] = away_club_name
    adict[game_id]['aggregate'] = aggregate
    adict[game_id]['competition_type'] = competition_type
    
##dump the dictionary to a json file        
json.dump(adict, outfile, indent=4, sort_keys=True) 
##close the files
outfile.close() 
infile.close()


##data looks like this
##game_id,competition_id,season,round,date,home_club_id,away_club_id,home_club_goals,away_club_goals,home_club_position,away_club_position,home_club_manager_name,away_club_manager_name,stadium,attendance,referee,url,home_club_formation,away_club_formation,home_club_name,away_club_name,aggregate,competition_type
