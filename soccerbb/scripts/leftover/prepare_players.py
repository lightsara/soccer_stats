#!/usr/bin/env python3


##Modifying script to have the name as key rather than ID.
##Abandoning that approach. Taking the last defined with the same name.
##prepare data 
import json


##Prepare player data.

##dirprep
rawdata = '/home/sara/main/FrontEnd_2025/soccer_stats_python/data/csv_files/players.csv'
##dirprep
output = '/home/sara/main/FrontEnd_2025/soccer_stats_python/output/players_0414.json'

##fileprep
outfile = open(output, 'w')
infile = open(rawdata, 'r')

adict = {}
for aline in infile:
    aline = aline.strip()
    if aline.startswith('0'):    
        continue
    fields = aline.split(',')
    player_id = fields[0]
    first_name = fields[1]
    last_name = fields[2]
    name = fields[3]
    last_season = fields[4]
    current_club_id = fields[5]
    player_code = fields[6]
    country_of_birth = fields[7]
    city_of_birth = fields[8]
    country_of_citizenship = fields[9]
    date_of_birth = fields[10]
    sub_position = fields[11]
    position = fields[12]
    foot = fields[13]
    height_in_cm = fields[14]
    contract_expiration_date = fields[15]
    agent_name = fields[16]
    image_url = fields[17]
    url = fields[18]
    current_club_domestic_competition_id = fields[19]
    current_club_name = fields[20]
    market_value_in_eur = fields[21]
    highest_market_value_in_eur = fields[22]

    adict[player_id] = {
        'first_name': first_name,
        'last_name': last_name,
        'name':name,
        'last_season': last_season,
        'current_club_id': current_club_id,
        'player_code': player_code,
        'country_of_birth': country_of_birth,
        'city_of_birth': city_of_birth,
        'country_of_citizenship': country_of_citizenship,
        'date_of_birth': date_of_birth,
        'sub_position': sub_position,
        'position': position,
        'foot': foot,
        'height_in_cm': height_in_cm,
        'contract_expiration_date': contract_expiration_date,
        'agent_name': agent_name,
        'image_url': image_url,
        'url': url,
        'current_club_domestic_competition_id': current_club_domestic_competition_id,
        'current_club_name': current_club_name,
        'market_value_in_eur': market_value_in_eur,
        'highest_market_value_in_eur': highest_market_value_in_eur
    } 

##dump the dictionary to a json file
json.dump(adict, outfile, indent=4, sort_keys=True) 
##close the files
outfile.close() 
infile.close()



##Data looks like this: 
## 0 player_id
## 1 first_name
## 2 last_name
## 3 name
##last_season,current_club_id,player_code,country_of_birth,city_of_birth,country_of_citizenship,date_of_birth,sub_position,position,foot,height_in_cm,contract_expiration_date,agent_name,image_url,url,current_club_domestic_competition_id,current_club_name,market_value_in_eur,highest_market_value_in_eur



