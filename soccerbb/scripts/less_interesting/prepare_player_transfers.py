#!/usr/bin/env python3

##prepare data 
import json

##Prepare team/club data.

##dirprep
outdir = '/home/sara/main/FrontEnd_2025/Projects/soccer_stats/data/'
rawdata = '/home/sara/main/FrontEnd_2025/Projects/soccer_stats/data/transfers.csv'
output = '/home/sara/main/FrontEnd_2025/Projects/soccer_stats/data/transfers.json'

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
    player_id = aline[0]
    transfer_date = aline[1]
    transfer_season = aline[2]
    from_club_id = aline[3]
    to_club_id = aline[4]   
    from_club_name = aline[5]
    to_club_name = aline[6]  
    transfer_fee = aline[7]
    market_value_in_eur = aline[8]
    player_name = aline[9]
   
    ##create a dictionary
    adict[player_id] = {}
    adict[player_id]['transfer_date'] = transfer_date
    adict[player_id]['transfer_season'] = transfer_season
    adict[player_id]['from_club_id'] = from_club_id
    adict[player_id]['to_club_id'] = to_club_id
    adict[player_id]['from_club_name'] = from_club_name
    adict[player_id]['to_club_name'] = to_club_name
    adict[player_id]['transfer_fee'] = transfer_fee
    adict[player_id]['market_value_in_eur'] = market_value_in_eur
    adict[player_id]['player_name'] = player_name

##dump the dictionary to a json file    
json.dump(adict, outfile, indent=4, sort_keys=True) 
##close the files
outfile.close() 
infile.close()



##Data looks like this
##player_id,transfer_date,transfer_season,from_club_id,to_club_id,from_club_name,to_club_name,transfer_fee,market_value_in_eur,player_name
