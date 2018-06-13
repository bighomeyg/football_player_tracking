import numpy as np
import pandas as pd
import random

class OLine(object):
    """An offensive lineman. He has two responsibilities: pass block
    and run block. Takes pre-snap coordinates as input (easiest implementation
    for LT, LG, C, RG, RT)
    """

    def __init__(self, x_coord, y_coord):
        """Return a player """
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.x_trajectory = []
        self.y_trajectory = []

    def pass_block(self):
        """Return the x and y trajectories for a pass block
        (OL hovers around LOS)"""
        for n in range(0, 1000):
            self.x_coord += np.random.normal()/10
            self.y_coord += np.random.normal()/10
            self.x_trajectory.append(self.x_coord)
            self.y_trajectory.append(self.y_coord)
        return self.x_trajectory, self.y_trajectory

    def run_block(self, assignment):
        """Return the x and y trajectories for a stock run block
        (just running forward)"""
        if assignment == 'reach':
            ## Offensive lineman takes 45 degree angle upfield 
            for n in range(0, 1000):
                self.x_coord += 0.1 + np.random.normal()/10
                self.y_coord += 0.1 + np.random.normal()/10
                self.x_trajectory.append(self.x_coord)
                self.y_trajectory.append(self.y_coord)
        elif assignment == 'BOB':
            ## Same as pass block
            for n in range(0, 1000):
                self.x_coord += np.random.normal()/10
                self.y_coord += np.random.normal()/10
                self.x_trajectory.append(self.x_coord)
                self.y_trajectory.append(self.y_coord)
        return self.x_trajectory, self.y_trajectory
    
class QB(object):
    ## QB. Can drop back 3, 7, or 0 steps.


    def __init__(self, x_coord, y_coord):
        """Return a player """
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.x_trajectory = []
        self.y_trajectory = []

    def three_step(self):

        for n in range(0, 1000):
            self.x_coord += np.random.normal()/10
            self.y_coord -= 0.05 - np.random.normal()/10
            self.x_trajectory.append(self.x_coord)
            self.y_trajectory.append(self.y_coord)
        #return list(zip(self.x_trajectory, self.y_trajectory))
        return self.x_trajectory, self.y_trajectory
        
    def seven_step(self):

        for n in range(0, 1000):
            self.x_coord += np.random.normal()/10
            self.y_coord -= 0.1 - np.random.normal()/10
            self.x_trajectory.append(self.x_coord)
            self.y_trajectory.append(self.y_coord)
        return self.x_trajectory, self.y_trajectory
    
    def quick(self):

        for n in range(0, 1000):
            self.x_coord += np.random.normal()/10
            self.y_coord += np.random.normal()/10
            self.x_trajectory.append(self.x_coord)
            self.y_trajectory.append(self.y_coord)
        return self.x_trajectory, self.y_trajectory

class WR(object):
    """WR. Can run multiple different routes (slant, hitch, corner, out, 
    post, go). WRs are formation aware: if on the left side of the formation, 
    the post route will be to the right, but if on the right, post will 
    be to the left (always to middle of field). Can also run block.
    """

    def __init__(self, x_coord, y_coord):
        """Return a player """
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.x_trajectory = []
        self.y_trajectory = []

    def run_block(self):

        for n in range(0, 1000):
            self.x_coord += np.random.normal()/10
            self.y_coord += np.random.normal()/10
            self.x_trajectory.append(self.x_coord)
            self.y_trajectory.append(self.y_coord)
        return self.x_trajectory, self.y_trajectory
    
    def slant(self):

        if self.x_coord < 0:
            ##WR on left side of formation
            for n in range(0, 200):
                self.x_coord += np.random.normal()/30
                self.y_coord += 0.1 + np.random.normal()/30
                self.x_trajectory.append(self.x_coord)
                self.y_trajectory.append(self.y_coord)
                
            for n in range(200, 1000):
                self.x_coord += 0.1 + np.random.normal()/30
                self.y_coord += 0.05 + np.random.normal()/30
                self.x_trajectory.append(self.x_coord)
                self.y_trajectory.append(self.y_coord)
            return self.x_trajectory, self.y_trajectory
                
        elif self.x_coord > 0:
            ##WR on right side of formation
            for n in range(0, 200):
                self.x_coord += np.random.normal()/30
                self.y_coord += 0.1 + np.random.normal()/30
                self.x_trajectory.append(self.x_coord)
                self.y_trajectory.append(self.y_coord)
                
            for n in range(200, 1000):
                self.x_coord -= 0.1 + np.random.normal()/30
                self.y_coord += 0.05 + np.random.normal()/30
                self.x_trajectory.append(self.x_coord)
                self.y_trajectory.append(self.y_coord)
                
            return self.x_trajectory, self.y_trajectory
    
    def hitch(self):

        for n in range(0, 500):
            self.x_coord += np.random.normal()/30
            self.y_coord += 0.1 + np.random.normal()/30
            self.x_trajectory.append(self.x_coord)
            self.y_trajectory.append(self.y_coord)
        for n in range(500, 1000):
            self.x_coord += np.random.normal()/30
            self.y_coord += np.random.normal()/30
            self.x_trajectory.append(self.x_coord)
            self.y_trajectory.append(self.y_coord)
        return self.x_trajectory, self.y_trajectory
    
    def out(self):

        if self.x_coord < 0:
            for n in range(0, 500):
                self.x_coord += np.random.normal()/30
                self.y_coord += 0.1 + np.random.normal()/30
                self.x_trajectory.append(self.x_coord)
                self.y_trajectory.append(self.y_coord)
            for n in range(500, 1000):
                self.x_coord -= 0.1 + np.random.normal()/30
                self.y_coord += np.random.normal()/30
                self.x_trajectory.append(self.x_coord)
                self.y_trajectory.append(self.y_coord)
            return self.x_trajectory, self.y_trajectory
        elif self.x_coord > 0:
            for n in range(0, 500):
                self.x_coord += np.random.normal()/30
                self.y_coord += 0.1 + np.random.normal()/30
                self.x_trajectory.append(self.x_coord)
                self.y_trajectory.append(self.y_coord)
            for n in range(500, 1000):
                self.x_coord += 0.1 + np.random.normal()/30
                self.y_coord += np.random.normal()/30
                self.x_trajectory.append(self.x_coord)
                self.y_trajectory.append(self.y_coord)
            return self.x_trajectory, self.y_trajectory
    
    
    def post(self):

        if self.x_coord < 0:
            for n in range(0, 500):
                self.x_coord += np.random.normal()/30
                self.y_coord += 0.1 + np.random.normal()/30
                self.x_trajectory.append(self.x_coord)
                self.y_trajectory.append(self.y_coord)
            for n in range(500, 1000):
                self.x_coord += 0.1 + np.random.normal()/30
                self.y_coord += 0.1 + np.random.normal()/30
                self.x_trajectory.append(self.x_coord)
                self.y_trajectory.append(self.y_coord)
            return self.x_trajectory, self.y_trajectory
        elif self.x_coord > 0:
            for n in range(0, 500):
                self.x_coord += np.random.normal()/30
                self.y_coord += 0.1 + np.random.normal()/30
                self.x_trajectory.append(self.x_coord)
                self.y_trajectory.append(self.y_coord)
            for n in range(500, 1000):
                self.x_coord -= 0.1 + np.random.normal()/30
                self.y_coord += 0.1 + np.random.normal()/30
                self.x_trajectory.append(self.x_coord)
                self.y_trajectory.append(self.y_coord)
            return self.x_trajectory, self.y_trajectory
    
    
    def corner(self):

        if self.x_coord < 0:
            for n in range(0, 500):
                self.x_coord += np.random.normal()/30
                self.y_coord += 0.1 + np.random.normal()/30
                self.x_trajectory.append(self.x_coord)
                self.y_trajectory.append(self.y_coord)
            for n in range(500, 1000):
                self.x_coord -= 0.1 + np.random.normal()/30
                self.y_coord += 0.1 + np.random.normal()/30
                self.x_trajectory.append(self.x_coord)
                self.y_trajectory.append(self.y_coord)
            return self.x_trajectory, self.y_trajectory
        
        elif self.x_coord > 0:
            for n in range(0, 500):
                self.x_coord += np.random.normal()/30
                self.y_coord += 0.1 + np.random.normal()/30
                self.x_trajectory.append(self.x_coord)
                self.y_trajectory.append(self.y_coord)
            for n in range(500, 1000):
                self.x_coord += 0.1 + np.random.normal()/30
                self.y_coord += 0.1 + np.random.normal()/30
                self.x_trajectory.append(self.x_coord)
                self.y_trajectory.append(self.y_coord)
            return self.x_trajectory, self.y_trajectory
    
    def go(self):

        for n in range(0, 1000):
            self.x_coord += np.random.normal()/50
            self.y_coord += 0.1 + np.random.normal()/30
            self.x_trajectory.append(self.x_coord)
            self.y_trajectory.append(self.y_coord)
        return self.x_trajectory, self.y_trajectory
    

class RB(object):
    """A running back. He has two responsibilities: run (to the right)
    or pass block.
    """

    def __init__(self, x_coord, y_coord):
        """Return a player """
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.x_trajectory = []
        self.y_trajectory = []

    def run(self):
        # Smash LOS!
        for n in range(0, 1000):
            self.x_coord += 0.025 + np.random.normal()/30
            self.y_coord += 0.1 + np.random.normal()/30
            self.x_trajectory.append(self.x_coord)
            self.y_trajectory.append(self.y_coord)
        return self.x_trajectory, self.y_trajectory
    
    def pass_block(self):

        for n in range(0, 1000):
            self.x_coord += np.random.normal()/20
            self.y_coord += np.random.normal()/20
            self.x_trajectory.append(self.x_coord)
            self.y_trajectory.append(self.y_coord)
        return self.x_trajectory, self.y_trajectory
    

    
class Playbook(object):
    
    def __init__(self, formation):
        
        self.LT = [-4,0]
        self.LG = [-2,0]
        self.C = [0,0]
        self.RG = [2,0]
        self.RT = [4,0]
        self.X = [-15, 0]
        self.Z = [15, 0]
        self.QB = [0,-2]
        self.F = [0,-4]
        if formation == 'two_by_two':
            self.H = [-8, -1]
            self.Y = [8, -1]
        elif formation == 'three_by_one_left':
            self.H = [-12, -1]
            self.Y = [-8, -1]
        elif formation == 'three_by_one_right':
            self.H = [12, -1]
            self.Y = [8, -1]


    def four_verts(self):
        x = WR(self.X[0], self.X[1]).go()
        h = WR(self.H[0], self.H[1]).go()
        y = WR(self.Y[0], self.Y[1]).go()
        z = WR(self.Z[0], self.Z[1]).go()
        q = QB(self.QB[0], self.QB[1]).seven_step()
        f = RB(self.F[0], self.F[1]).pass_block()
        lt = OLine(self.LT[0], self.LT[1]).pass_block()
        lg = OLine(self.LG[0], self.LG[1]).pass_block()
        c = OLine(self.C[0], self.C[1]).pass_block()
        rg = OLine(self.RG[0], self.RG[1]).pass_block()
        rt = OLine(self.RT[0], self.RT[1]).pass_block()
        return x, h, y, z, q, f, lt, lg, c, rg, rt
    
    def run(self):
        x = WR(self.X[0], self.X[1]).run_block()
        h = RB(self.H[0], self.H[1]).run()
        y = WR(self.Y[0], self.Y[1]).run_block()
        z = WR(self.Z[0], self.Z[1]).run_block()
        q = QB(self.QB[0], self.QB[1]).three_step()
        f = RB(self.F[0], self.F[1]).run()
        lt = OLine(self.LT[0], self.LT[1]).run_block('reach')
        lg = OLine(self.LG[0], self.LG[1]).run_block('reach')
        c = OLine(self.C[0], self.C[1]).run_block('BOB')
        rg = OLine(self.RG[0], self.RG[1]).run_block('reach')
        rt = OLine(self.RT[0], self.RT[1]).run_block('reach')
        return x, h, y, z, q, f, lt, lg, c, rg, rt
    
    def smash(self):
        x = WR(self.X[0], self.X[1]).hitch()
        h = WR(self.H[0], self.H[1]).corner()
        y = WR(self.Y[0], self.Y[1]).corner()
        z = WR(self.Z[0], self.Z[1]).hitch()
        q = QB(self.QB[0], self.QB[1]).seven_step()
        f = RB(self.F[0], self.F[1]).pass_block()
        lt = OLine(self.LT[0], self.LT[1]).pass_block()
        lg = OLine(self.LG[0], self.LG[1]).pass_block()
        c = OLine(self.C[0], self.C[1]).pass_block()
        rg = OLine(self.RG[0], self.RG[1]).pass_block()
        rt = OLine(self.RT[0], self.RT[1]).pass_block()
        return x, h, y, z, q, f, lt, lg, c, rg, rt
    
    def hitches(self):
        x = WR(self.X[0], self.X[1]).hitch()
        h = WR(self.H[0], self.H[1]).hitch()
        y = WR(self.Y[0], self.Y[1]).hitch()
        z = WR(self.Z[0], self.Z[1]).hitch()
        q = QB(self.QB[0], self.QB[1]).three_step()
        f = RB(self.F[0], self.F[1]).pass_block()
        lt = OLine(self.LT[0], self.LT[1]).pass_block()
        lg = OLine(self.LG[0], self.LG[1]).pass_block()
        c = OLine(self.C[0], self.C[1]).pass_block()
        rg = OLine(self.RG[0], self.RG[1]).pass_block()
        rt = OLine(self.RT[0], self.RT[1]).pass_block()
        return x, h, y, z, q, f, lt, lg, c, rg, rt
       
    def crosses(self):
        x = WR(self.X[0], self.X[1]).slant()
        h = WR(self.H[0], self.H[1]).out()
        y = WR(self.Y[0], self.Y[1]).out()
        z = WR(self.Z[0], self.Z[1]).slant()
        q = QB(self.QB[0], self.QB[1]).three_step()
        f = RB(self.F[0], self.F[1]).pass_block()
        lt = OLine(self.LT[0], self.LT[1]).pass_block()
        lg = OLine(self.LG[0], self.LG[1]).pass_block()
        c = OLine(self.C[0], self.C[1]).pass_block()
        rg = OLine(self.RG[0], self.RG[1]).pass_block()
        rt = OLine(self.RT[0], self.RT[1]).pass_block()
        return x, h, y, z, q, f, lt, lg, c, rg, rt
    
    
    def all_slant(self):
        x = WR(self.X[0], self.X[1]).slant()
        h = WR(self.H[0], self.H[1]).slant()
        y = WR(self.Y[0], self.Y[1]).slant()
        z = WR(self.Z[0], self.Z[1]).slant()
        q = QB(self.QB[0], self.QB[1]).three_step()
        f = RB(self.F[0], self.F[1]).pass_block()
        lt = OLine(self.LT[0], self.LT[1]).pass_block()
        lg = OLine(self.LG[0], self.LG[1]).pass_block()
        c = OLine(self.C[0], self.C[1]).pass_block()
        rg = OLine(self.RG[0], self.RG[1]).pass_block()
        rt = OLine(self.RT[0], self.RT[1]).pass_block()
        return x, h, y, z, q, f, lt, lg, c, rg, rt

def parse_play(play, position, coordinate):
    # Define some dictionaries for positions and coordinates
    keys_to_positions = {'x':0,'h':1,'y':2,'z':3,
                         'q':4,'f':5,'lt':6,'lg':7,
                         'c':8,'rg':9,'rt':10}
    coordinates = {'x':0, 'y':1}
    return play[keys_to_positions[position]][coordinates[coordinate]]

def run_play(play):
    ## Build a DataFrame with x,y coordinates for each player at 10 hz
    all11 = []
    play = play()
    for player in ['q','f','x','h','y','z','lt','lg','c','rg','rt']:
        for coord in ['x','y']:
            all11.append(parse_play(play, player, coord))
    df = pd.DataFrame(all11).T
    df.columns = ['qb_x', 'qb_y', 'f_x', 'f_y', 'x_x', 'x_y', 'h_x', 'h_y', 'y_x', 'y_y', 'z_x', 'z_y', 
                  'lt_x', 'lt_y', 'lg_x', 'lg_y', 'c_x', 'c_y', 'rg_x', 'rg_y', 'rt_x', 'rt_y']
    return df