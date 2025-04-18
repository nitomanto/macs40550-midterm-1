from mesa import Agent
from scipy.spatial.distance import cosine
import math
import numpy as np

class SchellingAgent(Agent):
    ## Initiate agent instance, inherit model trait from parent class
    def __init__(self, model, agent_type):
        super().__init__(model)
        ## Set agent type
        self.type = agent_type
        #print(self.type)
    ## Define basic decision rule

    def move(self):
        ## Get list of neighbors within range of sight
        neighbors = self.model.grid.get_neighbors(pos=self.pos,moore=True)
        ## Count neighbors of same type as self
        ## If an agent has any neighbors (to avoid division by zero), calculate share of neighbors of same type
        if neighbors:
            sum_neighbor = 0
            for neighbor in neighbors:
                neighbor_arr = np.array(neighbor.type)
                self_arr = np.array(self.type)
                sum_neighbor += 1 - abs(np.sum(neighbor_arr - self_arr) / 2)
            share_alike = sum_neighbor / len(neighbors)
        else:
            share_alike = self.model.desired_share_alike
        ## If unhappy with neighbors, move to random empty slot. Otherwise add one to model count of happy agents.
        if share_alike < self.model.desired_share_alike:
            self.model.grid.move_to_empty(self)
        else:
            self.model.happy += 1