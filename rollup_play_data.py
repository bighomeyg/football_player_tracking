import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from generate_training_data import get_data

'''
Creates rollup table for play metadata. Here, I log which players are on the 
field and how far they have run on each snap. 
'''


positions = ['qb', 'f', 'x', 'h', 'y', 'z', 'lt', 'lg', 'c', 'rg', 'rt']
engine = create_engine('mysql+pymysql://USERNAME:PASSWORD@127.0.0.1:3306/Seahawks')


def get_play_data(play_num):
    play_data = get_data("SELECT * FROM Seahawks.PlayData WHERE play_id = {}".format(play_num))
    play_data.columns = ['row_id', 'game_id','game_year','play_id','timestep', 'team_offense', 'team_defense', 
                         'qb_x', 'qb_y', 'f_x', 'f_y', 'x_x', 'x_y', 'h_x', 'h_y',
                         'y_x', 'y_y', 'z_x', 'z_y', 'lt_x', 'lt_y', 'lg_x', 'lg_y', 'c_x',
                         'c_y', 'rg_x', 'rg_y', 'rt_x', 'rt_y',  'q_id', 'f_id', 'x_id', 'h_id', 'y_id', 'z_id', 
                         'lt_id', 'lg_id', 'c_id', 'rg_id', 'rt_id', 'formation', 'playcall']
    player_ids = play_data.loc[:, 'q_id':'rt_id'].iloc[0].tolist()
    return play_data


def calc_total_distance(play_df, position):
    
    time_steps = [x for x in range(0,1000,100)] + [999]
    total_distance = 0
    t0 = 0
    position_x = position + '_x'
    position_y = position + '_y'
    for n in range(0,10):
        dx = play_df.loc[time_steps[t0+1]][position_x] - play_df.loc[t0][position_x]
        dy = play_df.loc[time_steps[t0+1]][position_y] - play_df.loc[t0][position_y]
        distance = np.sqrt(dx**2 + dy**2)
        total_distance += distance
        t0 += 1
    
    return total_distance


if __name__ == '__main__':
    for play in range(1,1281):
        play_df = get_play_data(play)
        game_id = play_df['game_id'].unique()[0]
        play_info = [play, game_id]
        for pos in positions:
            distances = [calc_total_distance(play_df, pos) for pos in positions]
        play_rollup_df = pd.DataFrame([play_info + distances + 
                                    list(map(int, play_df.loc[:, 'q_id':'rt_id'].iloc[0].tolist()))])
        play_rollup_df.columns = ['play_id', 'game_id'] + ['qb_distance', 'f_distance', 'x_distance', 'h_distance',
                                'y_distance', 'z_distance', 'lt_distance', 'lg_distance', 
                                'c_distance', 'rg_distance', 'rt_distance'] + play_df.loc[:, 'q_id':'rt_id'].columns.tolist() 
        play_rollup_df.to_sql('PlayInfo', engine, if_exists = 'append', index=False)



