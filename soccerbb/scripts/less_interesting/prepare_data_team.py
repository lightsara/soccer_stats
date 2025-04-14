#!/usr/bin/env python3

##prepare data 
import json

##Prepare team/club data.

##dirprep
outdir = '/home/sara/main/FrontEnd_2025/Projects/soccer_stats/data/'
rawdata = '/home/sara/main/FrontEnd_2025/Projects/soccer_stats/data/clubs.csv'
output = '/home/sara/main/FrontEnd_2025/Projects/soccer_stats/data/clubs.json'

##fileprep
outfile = open(output, 'w')
infile = open(rawdata, 'r')

adict = {}
for aline in infile:
    aline = aline.strip()
    if aline.startswith('0'):    ##wondering about this line
        continue
    fields = aline.split(',')
    team_id = fields[0]
    team_code = fields[1]
    team_name = fields[2]
    short_name = fields[3]
    country_id = fields[4]
    country_name = fields[5]
    league_id = fields[6]
    league_name = fields[7]
    league_season = fields[8]
    league_country_id = fields[9]
    league_country_name = fields[10]
    
    adict[team_id] = {
        'team_code': team_code,
        'team_name': team_name,
        'short_name': short_name,
        'country_id': country_id,
        'country_name': country_name,
        'league_id': league_id,
        'league_name': league_name,
        'league_season': league_season,
        'league_country_id': league_country_id,
        'league_country_name': league_country_name
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



