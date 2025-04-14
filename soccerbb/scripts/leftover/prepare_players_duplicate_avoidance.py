#!/usr/bin/env python3


##Modifying script to have the name as key rather than ID.
##Abandoning that approach. Taking the last defined with the same name.
##prepare data 
import json


##Prepare player data.

##dirprep
rawdata = '/home/sara/main/FrontEnd_2025/soccer_stats_python/data/csv_files/players.csv'
##dirprep
output = '/home/sara/main/FrontEnd_2025/Misc/alldata/csv_files/players_namekey.json'
##fileprep
outfile = open(output, 'w')
infile = open(rawdata, 'r')

duplicates = 0
code_duplicates = 0
name_duplicates = 0
adict = {}
player_code_dict = {}
player_name_dict = {}
coll_name_dups_dict = {}
coll_id_name_dict = {}
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

    ##Check if the player_code is already in the dictionary
    if player_code in player_code_dict:
        #print ("player_code already in dict: ", name, player_code, player_id, aline)
        code_duplicates += 1

    ##Check if the player_id is already in the dictionary
    if player_id in adict:
        #print ("id already in adict: ", name, player_id, aline)
        duplicates += 1
        
    ##Check if player name in dictionary
    if not name in coll_name_dups_dict:
        coll_name_dups_dict[name] = [(last_season, height_in_cm)]
    else:
        coll_name_dups_dict[name].append((last_season, height_in_cm))
        #print ("player_code already in dict: ", name, player_code, player_id, aline)
        name_duplicates += 1

    player_code_dict[player_code] = name
    player_name_dict[name] = player_code
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


##Checked the duplicate names, best to include the one with the
##largest number of appearances, or the last season one.

##Decided best to check the appearances
##dirprep
rawdata_appear = '/home/sara/main/FrontEnd_2025/Misc/alldata/csv_files/appearances.csv'
##dirprep
output = '/home/sara/main/FrontEnd_2025/Misc/alldata/csv_files/appearances_mod.json'
##fileprep
outfile = open(output, 'w')
infile = open(rawdata_appear, 'r')

player_appearance = {}
appearances_dict = {}
for aline in infile:
    ##strip the line
    aline = aline.strip()
    ##split the line  
    #print(aline)
    aline = aline.split(',')
    ##get the data
    appearance_id = aline[0]
    game_id = aline[1]
    player_id = aline[2]
    #print(player_id)
    player_club_id = aline[3]
    player_current_club_id = aline[4]
    date = aline[5]
    player_name = aline[6]
    competition_id = aline[7]
    yellow_cards = aline[8]
    red_cards = aline[9]
    goals = aline[10]
    assists = aline[11]
    minutes_played = aline[12]
    ##create a dictionary for the data
    appearances_dict[appearance_id] = {
        'game_id': game_id,
        'player_id': player_id,
        'player_club_id': player_club_id,
        'player_current_club_id': player_current_club_id,
        'date': date,
        'player_name': player_name,
        'competition_id': competition_id,
        'yellow_cards': yellow_cards,
        'red_cards': red_cards,
        'goals': goals,
        'assists': assists,
        'minutes_played': minutes_played
    }


    ##Check if player_id in dictionary
    if not player_id in player_appearance:
        player_appearance[player_id] = 1
    else:
        player_appearance[player_id] += 1
     
##dump the dictionary to a json file
json.dump(appearances_dict, outfile, indent=4, sort_keys=True)

outfile.close()
infile.close()

print(len(player_appearance))

print('player_id_dups: ', duplicates, '\n', '#unique_player_ids: ', len(adict), '\n', 'Player_code_dups: ', code_duplicates, '\n', '#unique player codes: ', len(player_code_dict), '\n', 'name_dups: ', name_duplicates, '\n', '#unique player names: ', len(player_name_dict))


##prep output
##check coll and appearance intersection
c = 0
for player_id in player_appearance:
    if player_appearance[player_id] > 10:
        #print(player_id, player_appearance[player_id])
        c += 1
print(c)
        
