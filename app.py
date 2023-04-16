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
    return {'total_movies':elt.get_score_count(platform, scored, year)}

@app.get('/get_count_platform/{platform}')
def get_count_platform(platform:str):
    return {'total_movies':elt.get_count_platform(platforms[platform])}

@app.get('/get_actor/{platform}/{year}')
def get_actor(platform:str, year:int):
    return {'actor': elt.get_actor(platforms[platform], year)}

@app.get('/prod_per_country/{content_type}/{country}/{year}')
def prod_per_country(content_type:str, country:str, year:int):
    return elt.prod_per_country(content_type, country, year)

@app.get('/get_contents/{rating}')
def get_contents(rating:str):
    return elt.get_contents(rating)

