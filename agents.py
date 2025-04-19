from mesa import Agent
import math
import numpy as np

class SchellingAgent(Agent):
    ## Initiate agent instance, inherit model trait from parent class
    def __init__(self, model, agent_type):
        super().__init__(model)
        ## Set agent type
        self.type = agent_type
    ## Define basic decision rule
    def move(self):
        ## Get list of neighbors within range of sight
        neighbors = self.model.grid.get_neighbors(pos=self.pos,moore=True)
        ## Count neighbors of same type as self
        ## If an agent has any neighbors (to avoid division by zero), calculate share of neighbors of same type
        if neighbors:
            sum_neighbor = 0
            for neighbor in neighbors:

                ## Flow logic: if dim 2 true, then this:
                if 0 < self.model.dim_two_share < 1:    
                    if neighbor.type[0] == self.type[0]:
                        sum_neighbor += 0.5
                    if neighbor.type[1] == self.type[1]:
                        sum_neighbor += 0.5
                ## else: revert to original Schelling
                else:
                    if neighbor.type[0] == self.type[0]:
                        sum_neighbor += 1
            share_alike = sum_neighbor / len(neighbors)
        else:
            share_alike = self.model.desired_share_alike
        ## If unhappy with neighbors, move to random empty slot. Otherwise add one to model count of happy agents.
        if share_alike < self.model.desired_share_alike:
            self.model.grid.move_to_empty(self)
        else:
            self.model.happy += 1