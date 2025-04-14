#!/usr/bin/env python3


##Modifying script to have the name as key rather than ID.
##Abandoning that approach. Taking the last defined with the same name.
##prepare data 
import json, copy


##Prepare player data.

##dirprep



player_file = open('/home/sara/main/FrontEnd_2025/soccer_stats_python/output/players_0414.json', 'r')
player_dict = json.load(player_file)
del(player_dict["player_id"])
player_file.close()

appearance_file = open('/home/sara/main/FrontEnd_2025/soccer_stats_python/output/appearances_0414.json', 'r')
appearance_dict = json.load(appearance_file)
del(appearance_dict["appearance_id"])
appearance_file.close()

##Go through appearance_dict, associate_with player, add to player_dict
player_appearance_dict = {}
for appear in appearance_dict:

    player_id = appearance_dict[appear]["player_id"]
    #print(player_id)
    if player_id not in player_dict:
        #print('not in player_dict', player_id)
        pass
    elif "appearances" not in player_dict[player_id]:
        player_dict[player_id]["appearances"] = 0
        player_dict[player_id]["appearances"] += 1 ##starting at one appear
    else:
        player_dict[player_id]["appearances"] += 1

##for player in player_dict:
##    print(player, player_dict[player])
        

##Noting the following:
##These are in appearances but not in players
##They occur twice. Ignore.
##not in player_dict 255495
##not in player_dict 411294
##not in player_dict 380365
##not in player_dict 380365
##not in player_dict 255495
##not in player_dict 411294

##Next step - remove the player ids with the same name with the lowest #appear
non_unique_player_name = {}
for player_id in player_dict:
    player_name = player_dict[player_id]["name"]
    last_season = player_dict[player_id]["last_season"]

    if "appearances" in player_dict[player_id]:
        appearances = player_dict[player_id]["appearances"]
    else:
        appearances = 0

    ##print
    ##print(player_id, player_name, last_season, appearances)
    if not player_name in non_unique_player_name:
        non_unique_player_name[player_name] = []
        non_unique_player_name[player_name].append((int(appearances), int(last_season), player_id))
    else:
        non_unique_player_name[player_name].append((int(appearances), int(last_season), player_id))

        
##remove non-uniques
nons = {}
for name in non_unique_player_name:
    if len(non_unique_player_name[name]) > 1:
        #print(name, non_unique_player_name[name])
        nons[name] = non_unique_player_name[name]
        
#print(len(nons))        

before = len(player_dict)

d = 0
for player_name in nons:
    #print(player_name, sorted(nons[player_name], reverse=True))
    listan = sorted(nons[player_name], reverse=True)
    for removed_player in listan[1:]: ##remove all but the first
        player_id = removed_player[-1] ##last item is player_id
        del player_dict[player_id]
        #print(player_id)
        d += 1

        
##Prepping jsonfile with only the correct names
after = len(player_dict)
differ = before-after
if differ == d:
    print(d)
    jsonfile = open('/home/sara/main/FrontEnd_2025/soccer_stats_python/output/' + 'reducing_same_names.json', 'w')
    json.dump(player_dict, jsonfile)
    jsonfile.close()
