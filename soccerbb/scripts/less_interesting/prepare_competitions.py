#!/usr/bin/env python3

##prepare data 
import json

##Prepare team/club data.

##dirprep
outdir = '/home/sara/main/FrontEnd_2025/Projects/soccer_stats/data/'
rawdata = '/home/sara/main/FrontEnd_2025/Projects/soccer_stats/data/competitions.csv'
output = '/home/sara/main/FrontEnd_2025/Projects/soccer_stats/data/competitions.json'

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
    competition_id = aline[0]
    competition_code = aline[1]
    name = aline[2]
    sub_type = aline[3]
    type = aline[4]
    country_id = aline[5]
    country_name = aline[6]
    domestic_league_code = aline[7]
    confederation = aline[8]
    url = aline[9]
    is_major_national_league = aline[10]
    ##create the dictionary
    adict[competition_id] = {}
    adict[competition_id]['competition_code'] = competition_code
    adict[competition_id]['name'] = name
    adict[competition_id]['sub_type'] = sub_type
    adict[competition_id]['type'] = type
    adict[competition_id]['country_id'] = country_id
    adict[competition_id]['country_name'] = country_name
    adict[competition_id]['domestic_league_code'] = domestic_league_code
    adict[competition_id]['confederation'] = confederation
    adict[competition_id]['url'] = url
    adict[competition_id]['is_major_national_league'] = is_major_national_league


##dump the dictionary to a json file    
json.dump(adict, outfile, indent=4, sort_keys=True) 
##close the files
outfile.close() 
infile.close()

##Data looks like this
##competition_id,competition_code,name,sub_type,type,country_id,country_name,domestic_league_code,confederation,url,is_major_national_league
