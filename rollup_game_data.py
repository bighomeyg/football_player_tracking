import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import random
from datetime import datetime, timedelta
from generate_training_data import get_data

'''
Logs important metadata for each game, like weather, time of kickoff, location, etc.
Could be useful for analysis on playcall tendencies, player performance, etc.
'''

def rollup_game_to_gamedata(game_id):
    game_data = get_data("SELECT * FROM Seahawks.PlayData WHERE game_id = {} LIMIT 1".format(game_id))
    game_data.columns = ['play_id', 'game_id','game_year','play_id','timestep', 'team_offense', 'team_defense', 
                         'qb_x', 'qb_y', 'f_x', 'f_y', 'x_x', 'x_y', 'h_x', 'h_y',
                         'y_x', 'y_y', 'z_x', 'z_y', 'lt_x', 'lt_y', 'lg_x', 'lg_y', 'c_x',
                         'c_y', 'rg_x', 'rg_y', 'rt_x', 'rt_y',  'q_id', 'f_id', 'x_id', 'h_id', 'y_id', 'z_id', 
                         'lt_id', 'lg_id', 'c_id', 'rg_id', 'rt_id', 'formation', 'playcall']
    teams = [game_data.team_offense.unique()[0], game_data.team_defense.unique()[0]]
    home_team = random.choice(teams)
    visiting_team = [x for x in teams if x != home_team][0]
    home_score = random.choice(range(2,50))
    visitor_score = random.choice(range(2,50))
    kickoff_hour_pst = random.choice([10, 13, 17])
    kickoff_temp = random.choice(range(10,80))
    game_date = datetime.strptime("2018-09-09", "%Y-%m-%d").date()+timedelta(days = 7*(game_id - 1))
    game_week = game_id
    game_year = 2018
    df = pd.DataFrame([[game_id, home_team, visiting_team, home_score, visitor_score,
                        kickoff_hour_pst, kickoff_temp, game_date, game_week, game_year]])
    df.columns = ['game_id', 'home_team', 'visiting_team', 'home_score', 'visitor_score',
                  'kickoff_hour_pst', 'kickoff_temp', 'game_date', 'game_week', 'game_year']
    return df

if __name__ == '__main__':
    for game in range(1,17):
        df = rollup_game_to_gamedata(game)
        df.to_sql('GameInfo', engine, if_exists = 'append', index=False)
