from gym import spaces
import numpy as np
import random
from itertools import groupby
from itertools import product
import copy
random.seed(42)


class TicTacToe():

    def __init__(self):
        """initialise the board"""
        
        # initialise state as an array
        self.state = [np.nan for _ in range(9)]  # initialises the board position, can initialise to an array or matrix
        # all possible numbers
        self.all_possible_numbers = [i for i in range(1, len(self.state) + 1)] # , can initialise to an array or matrix

        self.reset()


    def is_winning(self, curr_state):
        
        row_1 = curr_state[:3]
        row_2 = curr_state[3:6]
        row_3 = curr_state[6:]
        
        col_1 = [curr_state[0],curr_state[3],curr_state[6]]
        col_2 = [curr_state[1],curr_state[4],curr_state[7]]
        col_3 = [curr_state[2],curr_state[5],curr_state[8]]
        
        diag_1 = [curr_state[0],curr_state[4],curr_state[8]]
        diag_2 = [curr_state[2],curr_state[4],curr_state[6]]
        
        len_row_1 = sum([1 for i in row_1 if not np.isnan(i)])
        len_row_2 = sum([1 for i in row_2 if not np.isnan(i)])
        len_row_3 = sum([1 for i in row_3 if not np.isnan(i)])
        
        len_col_1 = sum([1 for i in col_1 if not np.isnan(i)])
        len_col_2 = sum([1 for i in col_2 if not np.isnan(i)])
        len_col_3 = sum([1 for i in col_3 if not np.isnan(i)])
        
        len_diag_1 = sum([1 for i in diag_1 if not np.isnan(i)])
        len_diag_2 = sum([1 for i in diag_2 if not np.isnan(i)])
        
        if ((sum(row_1)==15 and len_row_1==3) or (sum(row_2)==15 and len_row_2==3) or (sum(row_3)==15 and len(row_3)==3) \
        or (sum(col_1)==15 and len_col_1==3) or (sum(col_2)==15 and len_col_2==3) or (sum(col_3)==15 and len(col_3)==3) \
        or (sum(diag_1)==15 and len_diag_1==3) or (sum(diag_2)==15 and len_diag_2==3)):
            return True
        
        else:
            return False
        
        
            
        """Takes state as an input and returns whether any row, column or diagonal has winning sum
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan]
        Output = False"""
 

    def is_terminal(self, curr_state):
        # Terminal state could be winning state or when the board is filled up

        if self.is_winning(curr_state) == True:
            return True, 'Win'

        elif len(self.allowed_positions(curr_state)) == 0:
            return True, 'Tie'

        else:
            return False, 'Resume'


    def allowed_positions(self, curr_state):
        """Takes state as an input and returns all indexes that are blank"""
        return [i for i, val in enumerate(curr_state) if np.isnan(val)]


    def allowed_values(self, curr_state):
        """Takes the current state as input and returns all possible (unused) values that can be placed on the board"""

        used_values = [val for val in curr_state if not np.isnan(val)]
        agent_values = [val for val in self.all_possible_numbers if val not in used_values and val % 2 !=0]
        env_values = [val for val in self.all_possible_numbers if val not in used_values and val % 2 ==0]

        return (agent_values, env_values)


    def action_space(self, curr_state):
        """Takes the current state as input and returns all possible actions, i.e, all combinations of allowed positions and allowed values"""

        agent_actions = product(self.allowed_positions(curr_state), self.allowed_values(curr_state)[0])
        env_actions = product(self.allowed_positions(curr_state), self.allowed_values(curr_state)[1])
        return (agent_actions, env_actions)



    def state_transition(self, curr_state, curr_action):
                   
        curr_state[ curr_action[0] ] = curr_action[1]
         
        return curr_state
      

    def step(self, curr_state, curr_action):
        
        flag=0
        reward = -1
        terminal_state = False
        output_state = []
        #state after agent has taken the curr_action 
        state_after_agent_1 = self.state_transition(curr_state,curr_action)
        
        # check if this is the terminal state --> either a win or a tie
        terminal = self.is_terminal(state_after_agent_1)[0]
        
        if terminal:
            
            terminal_state = True
            
            # in case of win, reward = 10
            if self.is_terminal(state_after_agent_1)[1] == 'Win':
                reward = 10
            
            # in case of tie, reward = 0    
            else:
                reward = 0
            
        if not terminal_state:
            
            # check the actions the environment can take
            _,env_actions = self.action_space( state_after_agent_1 )
            
            # take that action by the environment, where it wins
            for env_action in list( env_actions ):
                # take a copy of the state_after_agent_1 so that it is preserved
                state_after_agent_1_copy = copy.deepcopy(state_after_agent_1)
                # state after environment has taken one of its valid actions
                state_after_env_1 = self.state_transition( state_after_agent_1_copy , env_action )
                # if it leads to winning, set this as the action taken by environment
                # agent loses, reward = -10 and state is terminal
                if self.is_winning(state_after_env_1):
                                        
                    output_state = state_after_env_1
                    reward = -10
                    terminal_state = True
                    
                    break
            # if no action by environment leads to its winning (agent losing)
            # take such an action so that a consequent action by agent does not lead to the agent winning (make env. smart)
            if reward != -10:
                _,env_actions = self.action_space( state_after_agent_1 )
                env_actions = list( env_actions )
                
                random.shuffle(env_actions)
                
                for env_action in env_actions:
                    
                    state_after_agent_1_copy = copy.deepcopy(state_after_agent_1)                    
                    
                    state_after_env_1 = self.state_transition( state_after_agent_1_copy , env_action )
                    
                    agent_actions,_ = self.action_space( state_after_env_1 )
                    
                    agent_actions = list( agent_actions )
                    
                    if len(agent_actions)!=0:
                    
                        random.shuffle(agent_actions)
                        
                        for agent_action in agent_actions:
                            
                            state_after_env_1_copy = copy.deepcopy(state_after_env_1)
                        
                            state_after_agent_2 = self.state_transition (state_after_env_1_copy, agent_action )
                            # select such action by env so that subsequent action by agent does not lead to its winning
                            if ( not self.is_winning(state_after_agent_2) ) :
                                
                                output_state = state_after_env_1
                                flag=1
                                break                        
                    
                    # a case where there are no actions left for the agent to take(after last step i.e. after 5th step by agent)
                    else:
                        return state_after_env_1,reward,True                        
                   
                    if flag==1:
                        break
            
            
            if len(output_state) != 0:
                                                          
                return output_state,reward,terminal_state
            
            # case where the env was ought to lose and hence it could not find any action where it was not losing
            # hence select any random valid action for environment and update the output state
            else:
                _,env_actions = self.action_space( state_after_agent_1 )
                
                env_actions = list( env_actions )
                
                state_after_agent_1_copy = copy.deepcopy(state_after_agent_1)                    
                    
                output_state = self.state_transition( state_after_agent_1_copy , env_actions[0] )
                
                
                return output_state,reward,terminal_state
        else:
            
            return state_after_agent_1,reward,terminal_state




    def reset(self):
        return self.state
