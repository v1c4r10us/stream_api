from fastapi import FastAPI
import interface as elt
import json

app=FastAPI()
platforms={'amazon':elt.amazon, 'disney':elt.disney, 'hulu':elt.hulu, 'netflix':elt.netflix}

@app.get('/get_max_duration/{year}/{platform}/{duration_type}')
def get_max_duration(year:int, platform:str, duration_type:str):
    return {'movie':elt.get_max_duration(year, platforms[platform], duration_type)}

@app.get('/get_score_count/{platform}/{scored}/{year}')
def get_score_count(platform:str, scored:float, year:int):
    return {'platform':platform, 'quantity':elt.get_score_count(platform, scored, year),'year':year, 'score':scored}

@app.get('/get_count_platform/{platform}')
def get_count_platform(platform:str):
    return {'platform':platform, 'movies':elt.get_count_platform(platforms[platform])}

@app.get('/get_actor/{platform}/{year}')
def get_actor(platform:str, year:int):
    resp=elt.get_actor(platforms[platform], year)
    return {'platform':platform, 'year':year, 'actor': resp[0], 'appearances':resp[1]}

@app.get('/prod_per_country/{content_type}/{country}/{year}')
def prod_per_country(content_type:str, country:str, year:int):
    return elt.prod_per_country(content_type, country, year)

@app.get('/get_contents/{rating_class}')
def get_contents(rating_class:str):
    return elt.get_contents(rating_class)

