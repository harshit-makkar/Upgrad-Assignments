# Import routines

import numpy as np
import math
import random
from itertools import product

# Defining hyperparameters
m = 5 # number of cities, ranges from 1 ..... m
t = 24 # number of hours, ranges from 0 .... t-1
d = 7  # number of days, ranges from 0 ... d-1
C = 5 # Per hour fuel and other costs
R = 9 # per hour revenue from a passenger


class CabDriver():

    def __init__(self):
        """initialise your state and define your action space and state space"""
        #self.actions = [ (i,j) for i,j in product(np.arange(5)+1,np.arange(5)+1) if i!=j ]
        self.action_space = [(0,0),(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)]
        self.state_space = list(product(np.arange(5)+1,np.arange(24),np.arange(7)))
        self.state_init = random.sample(self.state_space,1)[0]

        # Start the first round
        self.reset()


    ## Encoding state (or state-action) for NN input

    def state_encod_arch2(self, state):
        """convert the state into a vector so that it can be fed to the NN. This method converts a given state into a vector format. Hint: The vector is of size m + t + d."""
        location_vector = np.zeros(5)
        time_vector = np.zeros(24)
        day_vector = np.zeros(7)
        location_vector[ state[0] - 1 ] = 1
        time_vector[ state[1] ] = 1
        day_vector[ state[2] ] = 1
        
        state_encod = np.concatenate((location_vector,time_vector,day_vector),axis=None)
        
        return state_encod


    # Use this function if you are using architecture-1 
    def state_encod_arch1(self, state, action):
                
    #     """convert the (state-action) into a vector so that it can be fed to the NN. This method converts a given state-action pair into a vector format. Hint: The vector is of size m + t + d + m + m."""

        state_location_vector = np.zeros(5)
        state_time_vector = np.zeros(24)
        state_day_vector = np.zeros(7)
        action_pickup_vector = np.zeros(5)
        action_drop_vector = np.zeros(5)
        state_location_vector[ state[0] - 1 ] = 1
        state_time_vector[ state[1] ] = 1
        state_day_vector[ state[2] ] = 1
        action_pickup_vector[ action[0] - 1 ] = 1
        action_drop_vector[ action[1] - 1 ] = 1
        
        state_encod = np.concatenate((state_location_vector,state_time_vector,state_day_vector,action_pickup_vector,action_drop_vector),axis=None)
        
        return state_encod

        
    ## Getting number of requests

    def requests(self, state):
        """Determining the number of requests basis the location. 
        Use the table specified in the MDP and complete for rest of the locations"""
        location = state[0]
        if location == 1:
            requests = np.random.poisson(2)
        
        elif location == 2:
            requests = np.random.poisson(12)
         
        elif location == 3:
            requests = np.random.poisson(4)
            
        elif location == 4:
            requests = np.random.poisson(7)
            
        else:
            requests = np.random.poisson(8)
            
        if requests >15:
            requests = 15
        
        possible_actions_idx = random.sample(range(1, (m-1)*m+1), requests) # (0,0) is not considered as customer request
        
        actions = [self.action_space[i] for i in possible_actions_idx]

        possible_actions_idx.insert(0,0)
        actions.insert(0,(0,0))

        return possible_actions_idx,actions   



    def reward_func(self, state, action, Time_matrix):
        """Takes in state, action and Time-matrix and returns the reward"""
        if action == (0,0):
            
            reward = -C
            
        else:
            time_taken_curr_to_pickup = Time_matrix[ state[0] - 1 ][ action[0] - 1 ][state[1]][state[2]]
            
            if state[1] + time_taken_curr_to_pickup > 23:
                time_taken_pickup_to_drop = Time_matrix[ action[0] - 1 ][ action[1] - 1 ][ state[1] + int(time_taken_curr_to_pickup) - 24 ][(state[2]+1)%7]
            
            else:
                time_taken_pickup_to_drop = Time_matrix[ action[0] - 1 ][ action[1] - 1 ][ state[1] + int(time_taken_curr_to_pickup) ][state[2]]
            
            total_time_taken = time_taken_curr_to_pickup + time_taken_pickup_to_drop
            
            reward = ( R * time_taken_pickup_to_drop ) - ( C * total_time_taken )
            
        return reward




    def next_state_func(self, state, action, Time_matrix):
        """Takes state and action as input and returns next state"""
        if action == (0,0):
            if state[1]+1 > 23:
                next_state = (state[0],(state[1]+1)-24,(state[2]+1)%7)
            else:
                next_state = (state[0],state[1]+1,state[2])
        else:
            time_taken_curr_to_pickup = Time_matrix[ state[0] - 1 ][ action[0] - 1 ][ state[1] ][ state[2] ]
            
            if state[1] + time_taken_curr_to_pickup > 23:
                time_taken_pickup_to_drop = Time_matrix[ action[0] - 1 ][ action[1] - 1 ][ state[1] + int(time_taken_curr_to_pickup) - 24 ][(state[2]+1)%7]
            
            else:
                time_taken_pickup_to_drop = Time_matrix[ action[0] - 1 ][ action[1] - 1 ][ state[1] + int(time_taken_curr_to_pickup) ][ state[2] ]
            
            total_time_taken = time_taken_curr_to_pickup + time_taken_pickup_to_drop
            
            if state[1] + total_time_taken > 23:
                curr_time = int( state[1] + total_time_taken - 24 )
                next_state = (action[1],curr_time,(state[2]+1)%7)
            
            else:
                curr_time = int( state[1] + total_time_taken )
                next_state = (action[1],curr_time,state[2])
            
        return next_state




    def reset(self):
        return self.action_space, self.state_space, self.state_init
