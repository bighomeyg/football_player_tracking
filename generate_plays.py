import numpy as np
import pandas as pd
import random
from sqlalchemy import create_engine
from playbook import *

'''
Executes plays at random from the playbook and stores the 10 hz data in 
a mysql db.
'''

if __name__ == '__main__':

    engine = create_engine('mysql+pymysql://USERNAME:PASSWORD@127.0.0.1:3306/Seahawks')

    game_id = 1 
    game_year = 2018
    play_id = 1
    for game in range(0,16):
        opponent = random.choice(['SF', 'ARI', 'LAR'])
        for snap in range(0,80):
            formation = random.choice(['two_by_two', 'three_by_one_left', 'three_by_one_right'])
            plays = {0:'four_verts', 1:'run', 2:'smash', 3:'crosses', 4:'all_slant', 5:'hitches'}
            playlist = [Playbook(formation).four_verts, Playbook(formation).run, Playbook(formation).smash,
                        Playbook(formation).crosses, Playbook(formation).all_slant, Playbook(formation).hitches]
            
            play = random.choice([0,1,2,3,4,5])
            playcall = plays[play]
            play = playlist[play]
            play = run_play(play)
            play['game_id'] = game_id
            play['game_year'] = game_year
            play['play_id'] = play_id
            play['team_offense'] = 'SEA'
            play['team_defense'] = opponent
            play['q_id'] = 3
            play['f_id'] = 43
            play['x_id'] = 89
            play['h_id'] = 16
            play['y_id'] = 81
            play['z_id'] = 15
            play['lt_id'] = 79
            play['lg_id'] = 77
            play['c_id'] = 68
            play['rg_id'] = 78
            play['rt_id'] = 76
            play['formation'] = formation
            play['playcall'] = playcall
            play = play.reset_index()
            play.rename(columns={'index':'timestep'}, inplace=True)
            play.to_sql('PlayData', engine, if_exists = 'append', index=False)
            play_id+=1
        
        
        print("Game {} inserted".format(str(game_id)))
        game_id+=1

    print("Completed.")

