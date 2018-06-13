import pandas as pd
import numpy as np
from sqlalchemy import create_engine

'''
Converts 10 hz data to 2d matrix of player traces for machine learning. 
Essentially, eliminates time component and reduces to Xs and Os.
'''


def get_data(query):
    ## Connection for mysql db. Returns DataFrame.
    engine = create_engine('mysql+pymysql://USERNAME:PASSWORD@127.0.0.1:3306/Seahawks')
    connection = engine.connect().connection 
    df = pd.DataFrame(pd.read_sql(query, connection).values.tolist())
    connection.close()
    return df
    

def prep_data(query):
    ## Grabs data and labels DataFrame columns
    df = get_data(query)
    df.columns = ['play_id', 'game_id','game_year','play_id','timestep', 
                  'team_offense', 'team_defense', 'qb_x', 'qb_y', 'f_x', 
                  'f_y', 'x_x', 'x_y', 'h_x', 'h_y', 'y_x', 'y_y', 'z_x', 
                  'z_y', 'lt_x', 'lt_y', 'lg_x', 'lg_y', 'c_x', 'c_y', 'rg_x', 
                  'rg_y', 'rt_x', 'rt_y',  'q_id', 'f_id', 'x_id', 'h_id', 
                  'y_id', 'z_id', 'lt_id', 'lg_id', 'c_id', 'rg_id', 'rt_id', 
                  'formation', 'playcall']
    return df


def format_data(df):
    ## Flattens DataFrame from time series to matrix of locations 
    ## where any player has been. 
    play_data = df[['qb_x', 'qb_y', 'f_x', 'f_y', 'x_x', 'x_y',          
                    'h_x', 'h_y','y_x', 'y_y', 'z_x', 'z_y', 'lt_x', 'lt_y',
                     'lg_x', 'lg_y', 'c_x','c_y', 'rg_x', 'rg_y', 'rt_x', 'rt_y']]
    playcall = df['playcall'].unique()[0]
    formation = df['formation'].unique()[0]
    paths = pd.DataFrame(0, index=range(-125,125),columns=range(-100,100))

    for index, row in play_data.iterrows():
        for n in range(0,22,2):
            x = play_data.columns[n]
            y = play_data.columns[n+1]
            x = row[x]
            y = row[y]
            paths.set_value(np.round(y), np.round(x), 1)
    paths['playcall'] = playcall
    paths['formation'] = formation
    return paths


if __name__ == '__main__':
    
    ## Run for all games
    for game in range(1,17):
        
        for n in range(1,81):
            play_count =  (game-1) * 80 + n
            query = '''SELECT * FROM Seahawks.PlayData WHERE play_id = {}           
                    AND game_id = {};'''.format(str(play_count), str(game))
            df = prep_data(query)
            play_data = format_data(df)
            filename = 'data/game_{}_play_{}.csv'.format(str(game), str(play_count))
            play_data.to_csv(filename, index = False)

        